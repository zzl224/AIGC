# Infinite Canvas 项目启动说明

## 项目状态

✅ **项目已成功克隆到本地**
📍 **位置**: `E:\AI code\infinite-canvas`

## 🚨 当前环境限制

经过测试，发现以下问题：

1. ❌ **Docker 未安装** - 无法使用 Docker 方式启动
2. ⚠️ **npm 依赖安装超时** - 由于依赖包较大，在虚拟环境中安装超时

## 🎯 推荐的启动方案

### 方案一：在本地 Windows 系统中运行（推荐）

由于你的项目在 `E:\AI code\infinite-canvas`，你可以直接在 Windows 命令行或 PowerShell 中运行：

#### 步骤 1：安装依赖
打开命令提示符或 PowerShell，执行：

```bash
cd "E:\AI code\infinite-canvas\web"
npm install --legacy-peer-deps
```

#### 步骤 2：启动开发服务器
```bash
npm run dev
```

#### 步骤 3：访问应用
浏览器打开: `http://localhost:3000`

---

### 方案二：安装 Bun（更快的包管理器）

项目推荐使用 Bun，速度更快且兼容性更好：

#### 步骤 1：安装 Bun
- 访问: https://bun.sh
- 下载 Windows 版本并安装

#### 步骤 2：安装依赖并运行
```bash
cd "E:\AI code\infinite-canvas\web"
bun install
bun run dev
```

#### 步骤 3：访问应用
浏览器打开: `http://localhost:3000`

---

### 方案三：安装 Docker Desktop（适合长期使用）

#### 步骤 1：安装 Docker Desktop
- 访问: https://www.docker.com/products/docker-desktop
- 下载 Windows 版本并安装
- 安装后重启电脑

#### 步骤 2：启动项目
打开命令提示符或 PowerShell：
```bash
cd "E:\AI code\infinite-canvas"
docker compose up -d
```

#### 步骤 3：访问应用
浏览器打开: `http://localhost:3000`

#### Docker 优势
- ✅ 无需安装 Node.js 环境
- ✅ 环境隔离，不影响系统
- ✅ 一键启动和停止

---

## 🔧 首次配置

启动成功后，需要配置 AI 接口：

1. 打开 `http://localhost:3000`
2. 点击右上角**配置图标**
3. 填入以下信息：
   - **Base URL**: OpenAI 兼容的 API 地址
   - **API Key**: 你的 API 密钥

### 推荐的 API 服务商

项目 README 中提到了多个赞助商提供的 API 服务：

- **APIMart**: GPT-Image-2 低至 $0.006/张
- **Atlas Cloud**: 多模态 AI 推理平台
- **秘塔科技**: MiniMax H3 视频生成
- **88API**: 支持 GPT-Image、Gemini、Grok 等
- **Infistar.ai**: 低至官方 1 折的 API 中转
- **HeyRoute**: 多模态 API 服务商

或者使用免费方案：
- **chatgpt2api**: https://github.com/basketikun/chatgpt2api

---

## 📚 项目功能特性

### 核心功能
- 🎨 **无限画布**: 多画布项目、节点拖拽、连线、撤销重做
- 🤖 **AI 创作**: 文生图、图生图、参考图编辑、视频生成
- 💬 **画布助手**: 智能对话、自动生成并插入结果
- 🔌 **本地 Agent**: 连接 Codex / Claude Code
- 🧩 **插件系统**: 动态安装远程节点插件
- 📝 **提示词库**: 内置 7 个开源提示词来源

### 数据存储
所有数据（API Key、画布、素材、生成记录）都保存在**浏览器本地**，保护隐私。

---

## 🆘 常见问题

### Q: npm install 很慢怎么办？
A: 可以使用国内镜像源：
```bash
npm config set registry https://registry.npmmirror.com
npm install --legacy-peer-deps
```

### Q: 为什么需要 --legacy-peer-deps？
A: 项目使用的 Ant Design 版本存在 peer dependency 冲突，这个参数可以绕过检查。

### Q: 如何停止服务？
- **npm/bun**: 按 `Ctrl+C`
- **Docker**: `docker compose down`

### Q: 端口 3000 被占用怎么办？
修改配置：
- **npm/bun**: 编辑 `web/package.json`，将 `--port 3000` 改为其他端口
- **Docker**: 编辑 `docker-compose.yml`，修改端口映射

---

## 📖 更多资源

- **GitHub 仓库**: https://github.com/basketikun/infinite-canvas
- **功能文档**: `docs/content/docs/overview/features.mdx`
- **快速开始**: `docs/content/docs/overview/quick-start.mdx`
- **画布操作手册**: `docs/content/docs/canvas/canvas-node-manual.mdx`
- **QQ 交流群**: https://qm.qq.com/q/HRt2kUnYiG

---

## ✨ 下一步

1. **在 Windows 命令行中运行项目**（推荐方案一或方案二）
2. **配置 API 接口**
3. **开始创作你的 AI 漫画！**

祝你使用愉快！🎉
