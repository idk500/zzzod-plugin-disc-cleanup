# 驱动盘清理标记（disc_cleanup）

按规则层决策（.debug/cleanup_decisions.json）在仓库内逐盘指纹匹配并标记弃置；余位≥门槛自动跳过，满级盘永不标记。依赖仓库扫描器插件的解析模块。

- 版本：1.0.0（versionCode 1）
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

## 许可

见 [LICENSE](LICENSE)（GPL-3.0）。
