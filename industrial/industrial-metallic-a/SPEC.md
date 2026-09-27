# SPEC — 金属质感

## Background
钢灰、金属层次与精密制造气质结合的硬朗工业界面。

## Goals
- 三秒内明确位置、状态、重点、异常和下一步动作。
- 真实可操作的工业软件，不做纯展示皮肤。
- 使用钢灰阶、细金属分隔与轻微明暗层次，严禁拟物按钮和重度 2000 年代金属皮肤。
- Desktop / Web / Mobile / PPT 共享视觉语法但按平台重排。
- 完全品牌中立。

## Non-goals
不定义品牌，不复制厂商，不绑定技术栈，不以装饰替代工程信息。

## Information hierarchy
L1 Critical：Alarm、状态、核心 KPI、主动作；L2 Primary：当前任务主体；L3 Supporting：趋势/历史/参数；L4 Metadata：时间/ID/版本/操作者。L1 ≤ 6。

## Visual grammar
密度：medium-high；层次：beveled；Accent：#4D8FA6；Radius：3px。使用钢灰阶、细金属分隔与轻微明暗层次，严禁拟物按钮和重度 2000 年代金属皮肤。

## Typography & spacing
系统无衬线；正文 14–16px、表格 13px、标题 22–28px、KPI 28–44px。4px 网格：4/8/12/16/24/32/48。

## Status model
RUNNING / IDLE / READY / PAUSED / WARNING / ALARM / OFFLINE / DISABLED / UNKNOWN。状态不可只用颜色。

## Data
首屏 KPI 3–6；趋势折线、比较条形、少量组成可环形；数字足够回答的问题不画大图。

## Forms
参数名、值、单位、合法范围、修改状态明确；危险参数分组；批量修改显示影响范围。

## Feedback
Loading / Empty / No Permission / Disconnected / Error / Timeout / Partial Failure / Offline / No Results。

## Dangerous actions
停止、复位、删除、覆盖、下发必须标明对象和范围，高风险动作确认。

## Accessibility
键盘焦点、Hover/Focus/Selected/Disabled 完整；125%/150% 缩放不截断关键状态。

## Acceptance
三秒五问通过；无品牌身份；关键状态完整；主动作稳定；桌面 1366×768 / 1920×1080 可操作；Web 响应式；Mobile 任务重排。
