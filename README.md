# 驱动盘清理标记（disc_cleanup）

按内置规则矩阵（套装分类×死主词条）在仓库内逐盘指纹匹配并标记弃置；余位≥门槛自动跳过，满级盘永不标记。依赖仓库扫描器插件的解析模块。

## 功能状态对账

| 功能 | 状态 | 说明 |
|---|---|---|
| probe 探测（遍历+解析+决策） | ✅ 实机验证 | 548 格遍历、翻页滚动、安全跳过全通过（2026-11-06 实机） |
| 弃置标记（可逆，非拆解） | ✅ 实机验证 | 标记动作实机执行并核对（2026-11-06） |
| 拆解执行 | ➖ 不在本插件 | 拆解由官方「驱动盘拆解」应用承担，本插件只标记 |
| GUI 配置页 | ❌ 未开发 | 配置改 yml：`probe_mode` / `mark_limit`（单轮标记上限） / `capacity_free_min`（余位门槛，低于才清理） |

运行产物（可审计）：逐盘日志与汇总进 `.log/log.txt`；标记状态 `​.debug/cleanup_state.json`（即点即存，中断不丢）；结果汇总 `.debug/cleanup_result.json`；标记前后截图 `.debug/mark_debug/`。

- 版本：1.0.4（versionCode 5）
- 作者：[idk500](https://github.com/idk500)
- 仓库：https://github.com/idk500/zzzod-plugin-disc-cleanup

## 安装

在 ZZZOD 一条龙的「插件商店」中搜索 **驱动盘清理标记** 订阅安装；或从 Releases 下载 `disc_cleanup.zip` 手动导入。

## 配置

应用配置见一条龙 GUI 的应用设置页；`probe` 类开关默认开启（只读出报告，不执行真实动作）。

## 推荐工具（友链支持）

- **[WorkBuddy](https://www.workbuddy.cn/events/invite?inviteCode=bz944mufovr)** —— 腾讯出品的全场景 AI 工作台，本插件的设计、编码、测试与发版流程均在其 AI 助手协助下完成。
- **[ZCode](https://zcode.z.ai/invite/F9M8N3LD)** —— 智谱 GLM 编程助手，本项目的代码生成与重构主力。
- **[Kimi](https://kimi-bot.com/activities/zh-cn/invite/share?scenario=subscribe&from=share_poster&invitation_code=VFU7S5)** —— Moonshot AI 助手，长文档阅读与资料调研好帮手。

## 遇到问题？推荐 AI 自助排查 + 社区协作

本项目由 AI 协作开发，同样推荐你用 AI 自主解决问题，把维护精力留给真正的疑难：

1. **AI 自助排查**：把运行日志（`config/<实例>/log/log.txt`）与现象描述投喂给顺手的 AI 助手（WorkBuddy / ZCode / Kimi 均可，见上方友链），大多数环境与配置问题都能直接定位解决。
2. **提交 Issue**：AI 排查无法解决时再提 issue，请附运行日志、复现步骤，条件允许附录屏；标题带环境信息（基座版本 / 插件版本 / 游戏窗口分辨率）能显著加快定位。
3. **欢迎本地验证过的 PR**：修复类 PR 请先本地实测通过，描述中附验证环境与运行日志片段；由 AI 协助完成的修复同样欢迎，注明验证结论即可。

## 许可

见 [LICENSE](LICENSE)（GPL-3.0）。
