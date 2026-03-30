(function initPlacementCore(globalScope) {
  const DEFAULTS = {
    viewportMargin: 18,
    bottomOffset: 20,
    leftOffset: 20,
  };

  function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }

  function computeBubblePlacement(input) {
    const {
      viewportWidth,
      viewportHeight,
      bubbleWidth,
      bubbleHeight,
      viewportMargin = DEFAULTS.viewportMargin,
      bottomOffset = DEFAULTS.bottomOffset,
      leftOffset = DEFAULTS.leftOffset,
    } = input;

    const left = clamp(
      leftOffset,
      viewportMargin,
      viewportWidth - bubbleWidth - viewportMargin
    );

    const top = clamp(
      viewportHeight - bubbleHeight - bottomOffset,
      viewportMargin,
      viewportHeight - bubbleHeight - viewportMargin
    );

    if (!Number.isFinite(left) || !Number.isFinite(top)) {
      return null;
    }

    return { left, top };
  }

  const api = {
    DEFAULTS,
    computeBubblePlacement,
  };

  if (typeof module !== "undefined" && module.exports) {
    module.exports = api;
  }

  globalScope.SelectedTextCountPlacement = api;
})(typeof globalThis !== "undefined" ? globalThis : window);
