# SPEC — 国企数据驾驶舱

## Background
深蓝数据驾驶舱、宏观指标、地图与趋势结合的经营监控风格。

## Goals
- 正式、可信、可转发、可长期使用。
- 用于经营驾驶舱、生产经营态势和综合监控；允许深色氛围，但图表必须可核验，不能做空洞领导大屏。
- 支撑门户、经营管理、审批、项目、数据分析和移动办公。
- Web 主平台，Desktop/Mobile/PPT 保持统一。
- 完全品牌中立。

## Information hierarchy
L1：页面/单位/业务状态、关键指标、待办与异常；L2：业务主体；L3：辅助栏目/趋势/说明；L4：时间、编号、来源、审计。L1 ≤ 6。

## Visual grammar
密度 high；层次 command；强调色 #2CA8DF；圆角 4px。用于经营驾驶舱、生产经营态势和综合监控；允许深色氛围，但图表必须可核验，不能做空洞领导大屏。

## Layout
门户支持顶部主导航 + 栏目区；业务系统使用侧栏/二级导航 + 主工作区；经营数据采用范围 → KPI → 图表 → 表格。避免把所有模块塞进一屏。

## Components
正式按钮、表单、Table、Tree、Tabs、Steps、Approval Timeline、Notice、KPI、Chart、Attachment、Audit Log。状态语义固定。

## Forms & workflow
审批意见、经办人、时间、流程节点、附件和留痕必须清楚。提交/退回/撤回等动作说明后果。

## Accessibility & robustness
字体不小于常规业务可读标准；不只靠红绿；长标题/公文编号/单位名有溢出策略；打印/PDF 截图保持完整。

## Acceptance
三秒内明确位置、待办、状态和动作；Loading/Empty/Error/Permission 完整；无品牌污染；375–1440px 可用。
