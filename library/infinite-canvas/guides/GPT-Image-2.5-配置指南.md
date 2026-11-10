# GPT Image 2.5 配置指南

## 🎯 你的 API 信息

- **API 提供商**: 黑狐子 AI (https://code.heihuzi.ai/)
- **API Key**: `[REDACTED_API_KEY]`
- **模型**: GPT Image 2.5

---

## 📝 配置步骤

### 第 1 步：打开配置页面

1. 在浏览器中访问 `http://localhost:3000`
2. 点击右上角的**配置图标**（齿轮⚙️或三条横线菜单）

### 第 2 步：填写 API 配置

在配置弹窗中填入以下信息：

#### 基础配置

```
Base URL: https://code.heihuzi.ai
```

或者（如果上面不行，尝试添加 /v1）：
```
Base URL: https://code.heihuzi.ai/v1
```

#### API Key
```
[REDACTED_API_KEY]
```

#### 模型名称

尝试以下几个可能的模型名称（根据接口实际情况）：

- `gpt-image-2.5`
- `gpt-image`
- `dall-e-3`
- `gpt-4o-image`

**建议**：先尝试 `gpt-image-2.5`，如果不行再尝试其他名称。

### 第 3 步：可选配置

根据需要调整以下参数：

- **图片质量**: 标准 / 高清
- **图片比例**: 1:1 / 16:9 / 9:16 等
- **生成数量**: 1-4 张

### 第 4 步：测试模型

1. 点击配置页面中的**"拉取模型列表"**按钮
2. 如果成功，会显示可用的模型列表
3. 如果失败，说明 Base URL 或 API Key 配置有误

---

## 🎨 使用生图功能

### 方法一：直接在节点生成

1. 在画布上创建一个**文本节点**
2. 输入提示词，例如：
   ```
   一只可爱的橙色小猫，坐在窗台上，水彩画风格
   ```
3. 点击节点下方的**"生成"**按钮
4. 等待生成完成

### 方法二：使用生成配置节点

1. 创建**生成配置节点**
2. 连接上游的文本节点（提示词）
3. 在生成配置节点中选择模型和参数
4. 点击**"开始生成"**
5. 可以批量生成多张图片

### 方法三：使用画布助手

1. 点击右侧的**助手面板**
2. 在对话框中输入提示词
3. 选择**生图**功能
4. 生成的图片会自动插入画布

---

## ❗ 常见问题排查

### 问题 1：提示"无法连接到 API"

**可能原因**：
- Base URL 填写错误
- API Key 无效或过期
- 网络连接问题

**解决方案**：
1. 检查 Base URL 是否正确（尝试添加或删除 `/v1`）
2. 确认 API Key 是否复制完整
3. 在浏览器开发者工具（F12）的 Network 标签中查看请求详情

### 问题 2：提示"模型不存在"

**可能原因**：
- 模型名称填写错误
- 该 API 服务商使用的模型名称不同

**解决方案**：
1. 点击"拉取模型列表"查看可用模型
2. 尝试不同的模型名称：
   - `gpt-image-2.5`
   - `gpt-image`
   - `dall-e-3`
   - `gpt-4o-image`

### 问题 3：生成失败或超时

**可能原因**：
- 提示词过于复杂
- API 服务商限流
- 网络不稳定

**解决方案**：
1. 简化提示词
2. 等待几秒后重试
3. 检查 API 账户余额

### 问题 4：查看详细错误信息

1. 按 **F12** 打开浏览器开发者工具
2. 切换到 **Console（控制台）** 标签
3. 查看红色错误信息
4. 切换到 **Network（网络）** 标签
5. 找到失败的请求，查看响应内容

---

## 🔍 如何确认 Base URL 和模型名称

如果你不确定正确的配置，可以：

### 方法 1：联系 API 服务商

访问 `https://code.heihuzi.ai/` 的文档页面，查看：
- 正确的 Base URL（是否需要 `/v1`）
- 支持的模型列表
- API 调用示例

### 方法 2：使用浏览器测试

在浏览器开发者工具的 Console 中运行以下代码测试：

```javascript
// 测试 API 连接
fetch('https://code.heihuzi.ai/v1/models', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer [REDACTED_API_KEY]'
  }
})
.then(response => response.json())
.then(data => console.log('可用模型：', data))
.catch(error => console.error('错误：', error));
```

这会返回该 API 支持的所有模型列表。

---

## 📚 OpenAI 兼容接口说明

Infinite Canvas 使用以下 OpenAI 标准接口：

### 文生图
```
POST /v1/images/generations
```

### 图生图（参考图编辑）
```
POST /v1/images/edits
```

### 文本对话
```
POST /v1/chat/completions
```

### 模型列表
```
GET /v1/models
```

你的 API 服务商（黑狐子 AI）应该兼容这些接口。

---

## ✅ 配置成功标志

配置成功后，你应该能够：

1. ✅ 点击"拉取模型列表"能看到模型
2. ✅ 在文本节点输入提示词后能成功生成图片
3. ✅ 画布助手能正常生图
4. ✅ 生成配置节点能批量生成图片

---

## 🆘 仍然无法生图？

如果按照以上步骤仍然无法生图，请提供以下信息：

1. **浏览器 Console 的错误信息**（F12 → Console）
2. **Network 中失败请求的详细信息**（F12 → Network → 点击失败的请求 → Response）
3. **你填写的完整配置**（Base URL、模型名称）

我会根据具体错误信息帮你解决问题！

---

## 📞 技术支持

- **Infinite Canvas 项目 GitHub**: https://github.com/basketikun/infinite-canvas
- **QQ 交流群**: https://qm.qq.com/q/HRt2kUnYiG
- **黑狐子 AI 官网**: https://code.heihuzi.ai/

祝你使用愉快！🎉
