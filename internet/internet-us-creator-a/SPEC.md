# SPEC — 美式创意工作台

## Background
柔和中性色、彩色工具标签和模块化工作区的美式创作工具风格。

## Goals
- Web 首屏 3 秒内明确页面身份、价值重点、当前状态和主动作。
- 模块化但轻盈，工具状态和对象选中可用紫色/彩色标签；适合内容、设计、AI 创作、营销工作流。
- 强调美式互联网产品常见的直接性、扁平层级、清晰 CTA 和可扫描信息。
- Web 为主，Desktop/Mobile/PPT 保持同一视觉语法。
- 基础模板完全品牌中立。

## Non-goals
不复制任何真实互联网公司；不把 Landing Page 当完整产品 UI；不依赖大面积渐变和无意义动效；不牺牲可访问性。

## Hierarchy
L1：页面标题/核心价值/主动作/关键状态；L2：主内容和主对象；L3：辅助数据、说明、筛选；L4：元数据和审计。L1 ≤ 6。

## Layout
最大内容宽度通常 1200–1440px；页面左右留白明显；导航稳定；主 CTA 在视觉和空间上唯一；复杂页面使用侧栏或二级导航，不用满屏卡片轰炸。

## Visual grammar
模块化但轻盈，工具状态和对象选中可用紫色/彩色标签；适合内容、设计、AI 创作、营销工作流。
密度：medium；层次：modular-soft；主色 #7C3AED；圆角 12px。

## Components
按钮、输入、Tabs、Table、Card、Banner、Toast、Dialog、Drawer、Pagination、Command/Search、Empty/Error 均需完整状态。

## Data
数字对齐稳定；趋势/比较/组成按任务选图；数据页面先给结论和范围，再给图表；图表不可只靠颜色区分。

## Forms
标签、帮助、错误、必填、单位、保存状态明确；长表单分段；危险动作和普通保存分离。

## Responsive
Mobile 不是桌面缩小；优先保留标题、状态、主内容和 CTA。桌面辅助栏在移动端转 Drawer/Sheet。

## Accessibility
键盘、Focus、对比度、44px 触控目标、Reduced Motion、语义状态完整。

## Acceptance
3 秒测试通过；无品牌污染；主 CTA 唯一；Loading/Empty/Error/Permission 覆盖；375px–1440px 可用。
