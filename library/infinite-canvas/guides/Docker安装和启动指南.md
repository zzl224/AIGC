# 🐋 Docker 安装和启动 Infinite Canvas 完整指南

## 第一步：安装 Docker Desktop

### 1. 下载 Docker Desktop

访问官方网站下载：
**https://www.docker.com/products/docker-desktop**

选择 **Windows** 版本下载。

### 2. 安装 Docker Desktop

1. 双击下载的 `Docker Desktop Installer.exe`
2. 按照安装向导进行安装
3. 安装过程中可能需要：
   - 启用 WSL 2（Windows Subsystem for Linux 2）
   - 启用 Hyper-V（Windows 专业版）
4. 安装完成后**重启电脑**

### 3. 启动 Docker Desktop

1. 重启后，从开始菜单启动 **Docker Desktop**
2. 等待 Docker 启动完成（系统托盘图标变为绿色）
3. 首次启动可能需要几分钟

### 4. 验证 Docker 安装

打开命令提示符（Win + R，输入 `cmd`），执行：

```bash
docker --version
docker compose version
```

如果显示版本号，说明安装成功！

---

## 第二步：使用 Docker 启动 Infinite Canvas

### 1. 打开命令提示符

按 `Win + R`，输入 `cmd`，按回车

### 2. 进入项目目录

```bash
cd "E:\AI code\infinite-canvas"
```

### 3. 启动项目

```bash
docker compose up -d
```

**参数说明**：
- `up`：启动容器
- `-d`：后台运行（detached 模式）

### 4. 等待启动完成

首次启动会：
1. 下载 Docker 镜像
2. 构建容器
3. 安装项目依赖
4. 启动服务

整个过程可能需要 **5-10 分钟**，请耐心等待。

### 5. 访问应用

启动完成后，打开浏览器访问：

**http://localhost:3000**

---

## 常用 Docker 命令

### 查看容器状态
```bash
docker compose ps
```

### 查看容器日志
```bash
docker compose logs
```

### 实时查看日志（按 Ctrl+C 退出）
```bash
docker compose logs -f
```

### 停止服务
```bash
docker compose down
```

### 重启服务
```bash
docker compose restart
```

### 完全清理并重建
```bash
docker compose down
docker compose up -d --build
```

---

## 🎨 首次使用配置

### 1. 配置 API 接口

启动成功后，访问 `http://localhost:3000`：

1. 点击右上角的**配置图标**（⚙️）
2. 填入你的 API 配置：
   - **Base URL**：OpenAI 兼容的 API 地址
   - **API Key**：你的 API 密钥

### 2. 推荐的 API 服务商

根据项目文档，以下是一些推荐的服务商：

#### 🎨 图片生成 API
- **APIMart**（https://go.apimart.ai/gh-infinite-canvas）
  - GPT-Image-2 低至 $0.006/张
  - 1 美元可生成 160+ 张
  
- **88API**（https://88api.ai/sign-up?aff=zbs9）
  - 支持 GPT-Image、Gemini、Grok
  - 通过专属链接注册有优惠

#### 🎬 视频生成 API
- **秘塔科技**（https://metaso.cn/minimax-h3/?s=inf）
  - MiniMax H3 视频生成
  - 768P 仅 0.09 元/秒

#### 🌐 多模态 API
- **Infistar.ai**（https://www.infistar.cc/register?aff=4X3V9NA9）
  - 已原生集成无限画布
  - 低至官方 1 折的 API 中转

- **HeyRoute**（https://heyroute.ai/basketikun）
  - 新用户送 15 美元试用额度

#### 💰 免费方案
- **chatgpt2api**（https://github.com/basketikun/chatgpt2api）
  - 项目作者开发的免费生图项目

---

## 🎯 核心功能使用

### 1. 创建画布
- 点击"新建项目"
- 在无限画布上拖拽、缩放

### 2. AI 生图
- 选择节点
- 输入提示词
- 点击生成

### 3. 画布助手
- 选中画布节点
- 与 AI 助手对话
- 自动将结果插回画布

### 4. 提示词库
- 内置 7 个开源提示词库
- 可自定义添加

### 5. 素材管理
- 所有生成的图片自动保存
- 可重复使用和编辑

---

## ❓ 常见问题

### Q1: Docker Desktop 启动失败
**可能原因**：
- WSL 2 未正确安装
- Hyper-V 未启用（Windows 家庭版不支持）

**解决方案**：
1. 确保 Windows 版本为 Windows 10 版本 2004+ 或 Windows 11
2. 启用 WSL 2：
   ```bash
   wsl --install
   ```
3. 重启电脑

### Q2: docker compose 命令不存在
**解决方案**：
使用旧版命令：
```bash
docker-compose up -d
```

### Q3: 端口 3000 被占用
**解决方案**：
编辑 `E:\AI code\infinite-canvas\docker-compose.yml`，修改端口映射：
```yaml
ports:
  - "3001:3000"  # 改为 3001 或其他端口
```

然后访问 `http://localhost:3001`

### Q4: 容器启动后无法访问
**检查步骤**：
1. 检查容器状态：
   ```bash
   docker compose ps
   ```
2. 查看日志：
   ```bash
   docker compose logs
   ```
3. 确保 Docker Desktop 正在运行

### Q5: 修改代码后需要重启吗？
**不需要**！Docker 配置了热重载，修改代码会自动更新。

---

## 🔒 安全提示

- API Key 保存在浏览器本地，不会上传到服务器
- 定期备份画布数据
- 不要在公共网络下暴露端口

---

## 📚 更多资源

- **项目 GitHub**：https://github.com/basketikun/infinite-canvas
- **快速开始文档**：`E:\AI code\infinite-canvas\docs\content\docs\overview\quick-start.mdx`
- **功能介绍**：`E:\AI code\infinite-canvas\docs\content\docs\overview\features.mdx`
- **QQ 交流群**：https://qm.qq.com/q/HRt2kUnYiG

---

## ✅ 快速启动检查清单

- [ ] Docker Desktop 已安装
- [ ] Docker Desktop 正在运行（托盘图标为绿色）
- [ ] 已在命令行中进入项目目录
- [ ] 执行 `docker compose up -d`
- [ ] 等待启动完成（5-10 分钟）
- [ ] 访问 `http://localhost:3000`
- [ ] 配置 API Key
- [ ] 开始创作！

---

**祝你使用愉快！🎉**

如果遇到任何问题，请参考本指南的"常见问题"部分，或访问 GitHub 仓库寻求帮助。
