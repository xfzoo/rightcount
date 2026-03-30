# Chrome Web Store Listing Draft

## Store name
RightCount

## Category
Productivity

## Short description
Instantly show a lightweight count bubble when you right-click selected text on a web page.

## Detailed description
RightCount shows a clean count bubble the moment you right-click selected text on a web page.

It is designed for mixed Chinese and English text:

- Chinese is counted by character
- English is counted by word
- Numbers are counted as one token
- Punctuation is ignored

Everything runs locally in your browser. The extension does not send selected text anywhere, does not store it, and does not use analytics or tracking.

## Single purpose statement
This extension counts the currently selected text on web pages and shows the result in a lightweight bubble.

## Privacy tab answers draft
### Does the extension handle user data?
Yes. It temporarily reads the text the user has selected on the current web page in order to calculate the count and display the result.

### Is data sold?
No.

### Is data used or transferred for unrelated purposes?
No.

### Is data used for creditworthiness or lending purposes?
No.

### What data is handled?
Website content, limited to the user’s currently selected text on the active page.

### How is data handled?
Processed locally in the browser only. Not stored, transmitted, sold, or shared.

## Test instructions
1. Install the extension.
2. Open any regular `http` or `https` web page.
3. Select a passage of text.
4. Right-click the selection.
5. A count bubble should appear in the lower-left corner of the page for about 2 seconds.

Mixed-language example to test:
`你好，world! 2026`

Expected result:
`4`
