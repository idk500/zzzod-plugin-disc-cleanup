# 驱动盘清理标记（disc_cleanup）

按规则层决策（.debug/cleanup_decisions.json）在仓库内逐盘指纹匹配并标记弃置；余位≥门槛自动跳过，满级盘永不标记。依赖仓库扫描器插件的解析模块。

- 版本：1.0.0（versionCode 1）
- 作者：[idk500](https://github.com/idk500)
- 仓库：https://github.com/idk500/zzzod-plugin-disc-cleanup

## 安装

在 ZZZOD 一条龙的「插件商店」中搜索 **驱动盘清理标记** 订阅安装；或从 Releases 下载 `disc_cleanup.zip` 手动导入。

## 配置

应用配置见一条龙 GUI 的应用设置页；`probe` 类开关默认开启（只读出报告，不执行真实动作）。

## 许可

见 [LICENSE](LICENSE)（GPL-3.0）。
