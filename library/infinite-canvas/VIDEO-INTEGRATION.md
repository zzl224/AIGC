# 视频接口接入与验证记录

## Seedance

接口文档：https://docs.heihuzi.ai/cn/api-reference/videos/seedance/create

- 创建：`POST /api/v3/contents/generations/tasks`。
- 查询：`GET /api/v3/contents/generations/tasks/{id}`。
- 已接入模型：`doubao-seedance-2-0-260128`、`doubao-seedance-2-5-260628`。
- 最短时长 4 秒，支持 480p；首尾帧使用自适应比例。
- 已成功实测 Seedance 2.0 的虎角色首帧视频：4 秒、480p、4:3、24fps。
- 测试成品见 `examples/seedance/tiger-4s-480p.mp4`，首帧见同目录 PNG。
- Seedance 2.5 尚未进行真实生成测试。

## MiniMax

接口文档：https://docs.heihuzi.ai/cn/api-reference/videos/minimax-v2/create

- 创建：`POST /v2/video_generation`，JSON 请求。
- 查询：`GET /v2/query/video_generation/{task_id}`。
- H3 最短 4 秒，H3-Max 最短 5 秒；1 秒请求被接口拒绝。
- 已调整画布协议和调用脚本；实际生成尝试返回服务端 503，尚无成功视频，不应将协议接入等同于生成验证通过。

此处不保存密钥、带鉴权信息的请求头或临时签名下载地址。模型和参数支持范围以当前服务商文档为准。
