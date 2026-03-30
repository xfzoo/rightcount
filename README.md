# RightCount

RightCount is a minimal Chrome extension that shows a lightweight count bubble when you right-click selected text on a web page.

It is designed for mixed Chinese and English text:

- Chinese is counted by character
- English is counted by word
- Numbers are counted as one token
- Punctuation is ignored

## Files

- `manifest.json`, `content.js`, `placement-core.js`: extension source
- `icons/`: Chrome Web Store and extension icons
- `store-assets/`: screenshots and promo graphics for the Web Store listing
- `docs/privacy-policy.html`: privacy policy page
- `scripts/package_extension.sh`: creates an upload ZIP
- `STORE_LISTING.md`: draft Chrome Web Store copy

## Local install

1. Open `chrome://extensions`
2. Enable Developer Mode
3. Click `Load unpacked`
4. Select this repository folder

## Packaging

```bash
./scripts/package_extension.sh
```

This creates `dist/RightCount-<version>.zip`.

## Privacy policy

If you enable GitHub Pages for this repository, the privacy policy can be published at:

`https://xfzoo.github.io/rightcount/docs/privacy-policy.html`

You should replace the contact placeholder in `docs/privacy-policy.html` before publishing.
