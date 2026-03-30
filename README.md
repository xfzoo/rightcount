# RightCount

[中文](#中文简介) | [English](#english)

RightCount is a minimal Chrome extension that shows a lightweight count bubble when you right-click selected text on a web page.



## 中文简介

### 这是什么

RightCount 是一个极简的 Chrome 插件。

当你在网页里选中一段文字并右击时，它会立刻在页面左下角显示一个小小的数字气泡，用来告诉你这段文字的数量。

### 这个插件的想法
由于现阶段ai无法很准确的生成特定字数的内容，而所有ai网页端均无实时字数统计功能，导致在日常工作流中需要复制粘贴至有字数统计的文本编辑工具，明确了生成的确切字数后，再返回网页端告诉ai字太多了删减一些，或者是字太少了再多写点。
所以 RightCount 想做的事情只有一件：

在尽量不打断阅读和工作操作流程的前提下，让“选中文字并快速查看字数”这件事变得足够轻、足够快、足够自然。

### 计数规则

- 中文按字数统计
- 英文按单词统计，而不是按字符统计
- 多位数数字按 1 个词统计，而不是按字符统计
- 标点符号忽略不计
- 中英文混排会分别识别后再合并成一个结果

例如：

- `你好，world! 2026` 的结果是 `4`

### 目前的交互方式

- 在网页中选中一段文字
- 右击
- 页面左下角出现一个轻量数字气泡
- 大约 2 秒后自动消失

### 安装方式

#### 开发者模式本地安装

1. 打开 `chrome://extensions`
2. 打开右上角 `Developer Mode`
3. 点击 `Load unpacked`
4. 选择本仓库目录

### 打包

```bash
./scripts/package_extension.sh
```

打包后会生成：

`dist/RightCount-<version>.zip`

### 隐私说明

RightCount 只会在你主动选中文字并右击时，临时读取当前网页上的选中文本来计算数量。

它不会：

- 上传你的文字内容
- 存储你的选中文本
- 跟踪你的浏览记录
- 使用分析或广告追踪

隐私政策页面在这里：

- `docs/privacy-policy.html`

如果你启用了 GitHub Pages，未来可以公开访问：

`https://xfzoo.github.io/rightcount/privacy-policy.html`

### 项目结构

- `manifest.json`, `content.js`, `placement-core.js`: 插件源码
- `icons/`: 插件图标
- `store-assets/`: Chrome Web Store 截图与宣传素材
- `docs/privacy-policy.html`: 隐私政策页面
- `scripts/package_extension.sh`: 打包脚本
- `STORE_LISTING.md`: 商店文案草稿

## English

### What it is

RightCount is a minimal Chrome extension.

When you select text on a web page and right-click, it shows a small count bubble in the lower-left corner of the page.

### The idea behind it

RightCount started from a very simple thought:

At this stage, AI cannot accurately generate content with a specific word count, and no AI web interfaces have a real-time word count function. This leads to a daily workflow where you have to copy and paste the text into a text editor with a word counter, determine the exact word count, and then return to the webpage to tell the AI to delete some words if it's too long, or write more if it's too short. 

Therefore, RightCount wants to do just one thing: 
making text counting feel instant, lightweight, and natural inside the normal reading flow.

### Counting rules

- Chinese is counted by character
- English is counted by word, not by character
- Numbers count as one token
- Punctuation is ignored
- Mixed Chinese and English text is detected separately and merged into one result

Example:

- `你好，world! 2026` returns `4`

### Current interaction

- Select text on a web page
- Right-click
- A lightweight number bubble appears in the lower-left corner
- The bubble disappears automatically after about 2 seconds

### Installation

#### Local install in Developer Mode

1. Open `chrome://extensions`
2. Turn on `Developer Mode`
3. Click `Load unpacked`
4. Select this repository folder

### Packaging

```bash
./scripts/package_extension.sh
```

This creates:

`dist/RightCount-<version>.zip`

### Privacy

RightCount only reads the text you actively selected on the current page when you right-click, and only for the purpose of counting it.

It does not:

- send selected text to a server
- store your selected text
- track browsing history
- use analytics or ad tracking

The privacy policy page lives here:

- `docs/privacy-policy.html`

If GitHub Pages is enabled, it can be published at:

`https://xfzoo.github.io/rightcount/privacy-policy.html`
