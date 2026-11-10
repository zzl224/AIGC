# Infinite Canvas 安装指南

## 项目概述

**basketikun/infinite-canvas** 是一款面向AI创作的开源无限画布工作台，已成功克隆到本地。

**项目位置**: `E:\AI code\infinite-canvas`

## 核心功能

- ✅ 无限画布：多画布项目、节点拖拽缩放、连线、小地图、撤销重做
- ✅ AI 创作：支持文生图、图生图、参考图编辑、文本问答、音频和视频生成
- ✅ 画布助手：围绕选中节点和上游节点对话、生图
- ✅ 本地 Agent：通过 Canvas Agent 连接 Codex / Claude Code
- ✅ Codex App 插件：自动注册 MCP 并拉起本地 Agent
- ✅ 插件系统：支持动态安装/启用/更新远程节点插件
- ✅ 提示词库：内置 7 个开源提示词来源

## 技术栈

- **前端框架**: React 19.2.5
- **构建工具**: Vite 7.3.0
- **路由**: React Router 7
- **UI 组件**: Ant Design 6.4.2, shadcn
- **状态管理**: Zustand
- **样式**: Tailwind CSS 4

## 安装步骤

### 方法一：使用 Docker（推荐）

```bash
cd "E:\AI code\infinite-canvas"
docker compose up -d
```

访问: `http://localhost:3000`

### 方法二：本地开发环境

```bash
cd "E:\AI code\infinite-canvas\web"

# 使用 npm (需要使用 --legacy-peer-deps 解决依赖冲突)
npm install --legacy-peer-deps
npm run dev

# 或使用 bun (推荐，项目原生支持)
# 首先安装 bun: https://bun.sh
bun install
bun run dev
```

访问: `http://localhost:3000`

## 配置说明

首次打开后需要配置：

1. 点击右上角进入配置页面
2. 填入 OpenAI 兼容的 `Base URL` 和 `API Key`
3. 如果默认的 OpenAI 接口调用方式与您的 API 不同，可自定义生图/视频脚本调用

## 数据存储

- ✅ AI API Key、Base URL
- ✅ 画布数据
- ✅ 素材和生成记录

**所有数据默认保存在浏览器本地 (IndexedDB)**

## 当前安装状态

- ✅ 项目已克隆到本地
- ⚠️ npm 依赖安装遇到超时问题（可能由于网络或依赖包较大）

## 建议的下一步

1. **使用 Docker 运行**（最简单）：
   ```bash
   cd "E:\AI code\infinite-canvas"
   docker compose up -d
   ```

2. **或者安装 bun**（推荐的包管理器）：
   - 访问: https://bun.sh
   - 下载并安装 bun
   - 然后运行：
     ```bash
     cd "E:\AI code\infinite-canvas\web"
     bun install
     bun run dev
     ```

3. **或者继续使用 npm**：
   在命令行中手动运行：
   ```bash
   cd "E:\AI code\infinite-canvas\web"
   npm install --legacy-peer-deps
   npm run dev
   ```

## 相关资源

- **GitHub**: https://github.com/basketikun/infinite-canvas
- **快速开始文档**: docs/content/docs/overview/quick-start.mdx
- **功能介绍**: docs/content/docs/overview/features.mdx
- **画布操作手册**: docs/content/docs/canvas/canvas-node-manual.mdx
- **QQ 交流群**: https://qm.qq.com/q/HRt2kUnYiG

## 免费生图 API

如果需要免费的生图 API，可以查看项目作者的另一个项目：
https://github.com/basketikun/chatgpt2api

## 开源协议

MIT License - 可免费用于商业用途
