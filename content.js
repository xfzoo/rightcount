(() => {
  const placementApi = globalThis.SelectedTextCountPlacement;
  const TOKEN_REGEX = /\p{Script=Han}|[\p{Script=Latin}\p{Number}]+(?:[''\-][\p{Script=Latin}\p{Number}]+)*/gu;
  const BUBBLE_ID = "__selected_text_count_bubble__";
  const BUBBLE_STYLE_ID = "__selected_text_count_style__";
  const HIDE_DELAY_MS = 2000;
  const SHOW_DELAY_MS = 0;
  const VIEWPORT_MARGIN = 18;
  const VIEWPORT_LEFT_OFFSET = 20;
  const VIEWPORT_BOTTOM_OFFSET = 20;

  let hideTimer = null;
  let showTimer = null;
  let menuOpen = false;

  function countText(text) {
    const matches = text.match(TOKEN_REGEX);
    return matches ? matches.length : 0;
  }

  function selectedTextFromActiveElement() {
    const active = document.activeElement;
    if (!(active instanceof HTMLInputElement || active instanceof HTMLTextAreaElement)) {
      return "";
    }

    if (typeof active.selectionStart !== "number" || typeof active.selectionEnd !== "number") {
      return "";
    }

    if (active.selectionStart === active.selectionEnd) {
      return "";
    }

    return active.value.slice(active.selectionStart, active.selectionEnd);
  }

  function selectedTextFromPage() {
    const direct = selectedTextFromActiveElement().trim();
    if (direct) {
      return direct;
    }

    const selection = window.getSelection();
    if (!selection || selection.rangeCount === 0) {
      return "";
    }

    return selection.toString().trim();
  }

  function ensureStyle() {
    if (document.getElementById(BUBBLE_STYLE_ID)) {
      return;
    }

    const style = document.createElement("style");
    style.id = BUBBLE_STYLE_ID;
    style.textContent = `
      :root {
        --selected-text-count-bg: rgba(22, 24, 29, 0.92);
        --selected-text-count-fg: rgba(255, 255, 255, 0.96);
        --selected-text-count-border: rgba(255, 255, 255, 0.12);
        --selected-text-count-shadow: 0 18px 40px rgba(0, 0, 0, 0.3);
      }

      @media (prefers-color-scheme: dark) {
        :root {
          --selected-text-count-bg: rgba(255, 255, 255, 0.94);
          --selected-text-count-fg: #142033;
          --selected-text-count-border: rgba(15, 23, 42, 0.12);
          --selected-text-count-shadow: 0 16px 36px rgba(15, 23, 42, 0.18);
        }
      }

      #${BUBBLE_ID} {
        position: fixed;
        z-index: 2147483647;
        pointer-events: none;
        padding: 9px 13px;
        border-radius: 14px;
        border: 1px solid var(--selected-text-count-border);
        background: var(--selected-text-count-bg);
        color: var(--selected-text-count-fg);
        font: 600 14px/1.2 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        letter-spacing: 0.01em;
        box-shadow: var(--selected-text-count-shadow);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        color-scheme: light dark;
        user-select: none;
        opacity: 0;
        transform: translateY(6px) scale(0.98);
        transition: opacity 130ms ease, transform 130ms ease;
        white-space: nowrap;
      }

      #${BUBBLE_ID}[data-visible="true"] {
        opacity: 0.9;
        transform: translateY(0) scale(1);
      }
    `;
    document.documentElement.appendChild(style);
  }

  function ensureBubble() {
    ensureStyle();

    let bubble = document.getElementById(BUBBLE_ID);
    if (bubble) {
      return bubble;
    }

    bubble = document.createElement("div");
    bubble.id = BUBBLE_ID;
    bubble.setAttribute("role", "status");
    bubble.setAttribute("aria-live", "polite");
    document.documentElement.appendChild(bubble);
    return bubble;
  }

  function placeBubble(bubble) {
    // Render offscreen first to measure the real bubble dimensions
    bubble.style.left = "-9999px";
    bubble.style.top = "-9999px";
    bubble.setAttribute("data-visible", "false");

    const rect = bubble.getBoundingClientRect();
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const bw = rect.width;
    const bh = rect.height;
    const placement = placementApi.computeBubblePlacement({
      viewportWidth: vw,
      viewportHeight: vh,
      bubbleWidth: bw,
      bubbleHeight: bh,
      viewportMargin: VIEWPORT_MARGIN,
      leftOffset: VIEWPORT_LEFT_OFFSET,
      bottomOffset: VIEWPORT_BOTTOM_OFFSET,
    });

    if (!placement) {
      return;
    }

    bubble.style.left = `${placement.left}px`;
    bubble.style.top = `${placement.top}px`;
  }

  function hideBubble() {
    const bubble = document.getElementById(BUBBLE_ID);
    if (!bubble) {
      return;
    }

    bubble.setAttribute("data-visible", "false");
  }

  function clearHideTimer() {
    if (!hideTimer) {
      return;
    }

    window.clearTimeout(hideTimer);
    hideTimer = null;
  }

  function dismissMenuBubble() {
    if (!menuOpen) {
      return;
    }

    menuOpen = false;
    clearHideTimer();
    hideBubble();
  }

  function showBubble(message) {
    const bubble = ensureBubble();
    bubble.textContent = message;
    placeBubble(bubble);

    requestAnimationFrame(() => {
      bubble.setAttribute("data-visible", "true");
    });

    clearHideTimer();
    hideTimer = window.setTimeout(hideBubble, HIDE_DELAY_MS);
  }

  document.addEventListener("contextmenu", (event) => {
    if (showTimer) {
      window.clearTimeout(showTimer);
    }

    showTimer = window.setTimeout(() => {
      const text = selectedTextFromPage();
      if (!text) {
        return;
      }

      const count = countText(text);
      if (!count) {
        return;
      }

      showBubble(`${count}`);
    }, SHOW_DELAY_MS);
  }, true);

  document.addEventListener("contextmenu", () => {
    menuOpen = true;
  }, true);

  document.addEventListener("pointerdown", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("mousedown", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("mouseup", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("click", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("keydown", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("keyup", () => {
    dismissMenuBubble();
  }, true);

  document.addEventListener("wheel", () => {
    dismissMenuBubble();
  }, { capture: true, passive: true });
})();
