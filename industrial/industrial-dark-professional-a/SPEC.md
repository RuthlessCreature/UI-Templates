# SPEC — 工业深色专业

## 1. Background
深色石墨、低眩光、高密度、严肃克制的专业工业工作台。

## 2. Goals
- 三秒内明确位置、状态、重点、异常和下一步动作。
- 保持真实工业软件的可操作性与信息密度。
- 将“低眩光深色面板、细边框、克制高亮；适合长期工程调试与控制。”贯彻到组件、布局、图表和状态系统。
- Desktop / Web / Mobile / PPT 共享同一视觉语法但不强行共享布局。
- 基础模板完全品牌中立。

## 3. Non-goals
- 不定义任何公司品牌、Logo、客户身份或真实产品名称。
- 不以装饰效果替代工程信息。
- 不复制任何具体厂商专有界面。
- 不绑定前端技术栈。

## 4. Information hierarchy
L1 Critical：Alarm、运行状态、核心 KPI、主动作。  
L2 Primary：当前任务主体、图像、设备、工单、检测结果。  
L3 Supporting：趋势、历史、参数、辅助统计。  
L4 Metadata：时间、ID、版本、操作者、更新时间。  
一个视口内 L1 焦点不超过 6 个。

## 5. Three-second contract
页面必须回答：我在哪？现在什么状态？什么最重要？有没有异常？下一步做什么？

## 6. Visual grammar
- 定位：深色石墨、低眩光、高密度、严肃克制的专业工业工作台。
- 设计注记：低眩光深色面板、细边框、克制高亮；适合长期工程调试与控制。
- 信息密度：high
- 层次策略：flat
- 主强调色：#2FA8FF
- 圆角基准：3px
- 状态色保持语义稳定；不可只靠颜色传递状态。

## 7. Typography
系统无衬线字体栈；正文 14–16px，表格 13px，页面标题 22–28px，KPI 28–44px；数字优先使用 tabular numerals。

## 8. Spacing
4px 基础网格：4 / 8 / 12 / 16 / 24 / 32 / 48。

## 9. Components
普通面板、表格、表单、图表、报警、状态指示必须服从本模板视觉语法。主操作每个操作区只保留一个视觉主按钮。

## 10. Status model
RUNNING / IDLE / READY / PAUSED / WARNING / ALARM / OFFLINE / DISABLED / UNKNOWN。UNKNOWN 不得错误归并为 OFFLINE。

## 11. Data display
KPI 首屏 3–6 个；趋势用折线；比较用条形；组成仅在类别较少时使用环形图；能用数字回答的问题不要画大图。

## 12. Forms
参数名、值、单位、合法范围、修改状态必须明确。危险参数单独分组，批量修改必须展示影响范围。

## 13. Feedback
必须覆盖 Loading / Empty / No Permission / Disconnected / Error / Timeout / Partial Failure / Offline / No Results。

## 14. Dangerous actions
停止、复位、删除、覆盖、下发参数等动作必须说明对象和影响范围；不可逆或高风险动作必须确认。

## 15. Accessibility
键盘焦点、Hover/Focus/Selected/Disabled 清楚；红绿状态同时配合文字/图标；125%/150% 缩放不截断关键运行信息。

## 16. Acceptance criteria
- 三秒测试五问可回答。
- 无真实品牌/客户身份。
- 关键组件状态完整。
- Loading / Empty / Error / Offline 已覆盖。
- 主动作唯一且位置稳定。
- 1366×768 与 1920×1080 桌面可操作，Web 可响应式，Mobile 为任务重排而非缩小桌面。
