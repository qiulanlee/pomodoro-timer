# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

基于浏览器的桌面番茄钟应用。Python 启动本地 HTTP 服务，浏览器加载 `index.html` 作为 UI 界面。纯前端实现，无后端依赖。

## 启动 & 开发

```bash
# 启动（终端）
python3 番茄钟.py

# 双击启动（macOS Finder）
open 番茄钟.command
```

启动后在浏览器打开 `http://127.0.0.1:{随机端口}`，刷新页面即可看到代码修改。没有构建步骤，直接编辑 `index.html` 即可。

`番茄钟.py` 使用 Python stdlib 的 `http.server`，零 pip 依赖。端口从 8765 开始自动寻找空闲端口。`.command` 文件是对 macOS 双击启动的包装。

## 架构

所有应用逻辑集中在 `index.html` 这一个文件中（CSS + HTML + JS）。

**主题系统**：通过 `body[data-theme]` 切换 CSS 变量（`--bg`、`--card`、`--text` 等）。深色（`dark`）和浅色（`light`）各有一套变量值。JS 中 `RING` 对象存储每个模式（focus/shortBreak/longBreak）在深浅主题下的环形配色（bg、fg、glow），`updateUI()` 根据当前 mode + theme 查表设置 `--ring-bg`、`--ring-fg`、`--ring-glow` CSS 变量。

**计时逻辑**：`setTimeout` 递归实现倒计时（非 `setInterval`），状态机为 idle → running → paused/completed。完成专注后自动切到短休，休息结束后切回专注。

**统计持久化**：`localStorage` 存储 `pomodoro_stats`（total/today/streak/lastDate）和 `pomodoro_theme`。日期变更时自动重置今日计数并更新连续天数。

**通知**：Web Notification API + AudioContext 生成三音提示音（C5-E5-G5）。完成时页面标题闪烁 3 秒。

## 环境约束

- 用户在中国大陆，避免依赖需从 GitHub/外网下载的包（如 npm、pip install）
- Python 3 + stdlib 优先，不依赖 Homebrew
- macOS 平台，通知和音效依赖浏览器 Web API，不依赖系统调用
