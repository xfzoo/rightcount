# Chrome Web Store Submission Checklist

## Files prepared locally

- Package ZIP: `dist/RightCount-<version>.zip`
- Icons: `icons/`
- Store images: `store-assets/`
- Listing draft: `STORE_LISTING.md`
- Privacy policy draft: `docs/privacy-policy.html`

## Remaining manual steps

1. Upload the ZIP in the Chrome Web Store Developer Dashboard.
2. Fill in the Store Listing tab using the draft copy.
3. Upload at least one screenshot from `store-assets/`.
4. Upload the small promo tile if you want stronger listing visuals.
5. Host `privacy-policy.html` at a public URL and paste that URL into the Privacy tab.
6. In the Privacy tab, describe the extension’s single purpose as counting selected text on web pages.
7. Submit for review, preferably with deferred publishing enabled so you can release manually after approval.

## Recommended review notes

Use the following in the Test instructions tab:

1. Install the extension from the uploaded package.
2. Open any `http` or `https` page.
3. Select text and right-click.
4. Confirm that a count bubble appears in the lower-left corner.
5. Example text: `你好，world! 2026`
6. Expected result: `4`
