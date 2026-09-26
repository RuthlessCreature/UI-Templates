# SPEC — 工业简洁A

## 1. Background

工业软件经常出现两个极端：一类是旧式控件堆叠，信息很多但难扫描；另一类是为了“科技感”做成大屏展示，漂亮但无法高效操作。本模板的目标是在工程信息密度与现代可读性之间建立稳定规则。

## 2. Goals

1. 首屏三秒内回答：位置、状态、重点、异常、下一步动作。
2. 让工程师在高信息密度页面中快速定位参数、结果与异常。
3. 让操作员在运行页面中无需阅读长文本即可判断是否正常。
4. 同一套设计语言可适配 Desktop、Web、Mobile 与 PPT。
5. UI 基础层完全品牌中立，可被不同项目复用。

## 3. Non-goals

- 不定义具体公司的品牌系统。
- 不提供营销官网视觉语言。
- 不追求娱乐化、游戏化、赛博化或强装饰视觉。
- 不规定某一前端框架或桌面框架。

## 4. Information hierarchy

仅使用四级视觉优先级：

| Level | Purpose | Examples |
|---|---|---|
| L1 Critical | 立即影响判断或动作 | Alarm、当前运行状态、核心 KPI、主动作 |
| L2 Primary | 当前任务主体 | 图像、工单、配方、检测结果、设备列表 |
| L3 Supporting | 辅助判断 | 趋势、历史、参数组、次级统计 |
| L4 Metadata | 上下文与审计 | 时间、ID、版本、操作者、更新时间 |

规则：一个视口内 L1 不超过 6 个焦点；同一操作区原则上只保留一个 Primary Action。

## 5. Three-second screen contract

每个主要页面必须显式提供：

1. **Location** — 产品/模块/页面上下文。
2. **State** — Running / Idle / Warning / Alarm / Offline 等。
3. **Priority** — 3–6 个核心指标或当前任务结果。
4. **Exception** — 异常数量、等级和入口。
5. **Action** — 当前最合理的下一步操作。

## 6. Desktop layout

默认 1920×1080 参考网格：

- Top Context Bar: 48–56 px
- Secondary Toolbar: 40–48 px（按需）
- Left Navigation / Task Tree: 220–280 px
- Main Workspace: 自适应，页面主要视觉区域
- Right Properties: 300–360 px（按需）
- Bottom Status / Log: 28–180 px，按场景折叠

工作区优先级：主视觉/主任务 > 参数 > 日志。禁止让日志或菜单长期抢占主工作区。

## 7. Color semantics

基础颜色与语义解耦于品牌：

- Accent Blue — 选中、链接、主按钮、当前对象
- Success Green — 正常、OK、通过、在线且健康
- Warning Amber — 注意、临界、需人工确认
- Danger Red — 报警、NG、故障、危险动作
- Neutral Gray — 离线、禁用、未配置、元数据

颜色不得成为唯一状态编码；必须配合文本、图标或形状。

## 8. Typography

- UI 字体使用系统无衬线字体栈，不在模板仓库绑定商业字体文件。
- 正文：14–16 px；高密度桌面表格可降至 13 px，但必须保持可读。
- 页面标题：22–28 px。
- KPI 数值：28–44 px，标签小于数值至少一级。
- 数字列使用等宽数字特性时优先启用 `font-variant-numeric: tabular-nums`。

## 9. Spacing

4 px 基础网格：`4 / 8 / 12 / 16 / 24 / 32 / 48`。

高密度不是压缩一切：可点击目标不得因视觉紧凑而失去可操作尺寸。

## 10. Borders, radius, elevation

- Border: 1 px 中性灰为主。
- Radius: 2–6 px；工业桌面控件避免过度圆润。
- Shadow: 仅浮层、Dialog、Drawer 使用；普通 Panel 依赖边框和背景层级。

## 11. Status model

推荐状态集合：

`RUNNING`, `IDLE`, `READY`, `PAUSED`, `WARNING`, `ALARM`, `OFFLINE`, `DISABLED`, `UNKNOWN`。

状态命名、颜色与图标在全系统一致。`UNKNOWN` 必须独立存在，不允许错误归入 `OFFLINE`。

## 12. Data display rules

- KPI 首屏只保留 3–6 个。
- 趋势用折线图；类别比较用条形图；组成仅在类别很少时用环形图。
- 单个百分比若数字本身足够回答问题，不额外占用大图表。
- 表格默认支持：筛选、排序、分页/虚拟滚动、列宽、状态标签、空态、加载态、错误态。
- 数字右对齐，文本左对齐；时间、ID、状态保持稳定列宽。

## 13. Forms and parameter editing

- 参数名、当前值、单位、合法范围、默认值、修改状态必须可辨。
- 危险参数与普通参数分组。
- 输入校验应在字段附近反馈，不把所有错误集中到页面顶部。
- 批量修改必须展示影响范围。

## 14. Feedback states

必须实现：`Loading`, `Empty`, `No Permission`, `Disconnected`, `Error`, `Timeout`, `Partial Failure`, `Offline`, `No Results`。

所有异步动作必须明确“进行中 / 成功 / 失败”，禁止按钮点下后无反馈。

## 15. Critical actions

停止、复位、清零、删除、覆盖配方、下发参数等操作：

- 与普通按钮视觉区分。
- 说明影响对象与影响范围。
- 对不可逆或高风险动作进行确认。
- 确认文案写清“将发生什么”，而不是只写“确定吗？”。

## 16. Accessibility and robustness

- 文本与背景满足常规可读对比度。
- 状态不可仅凭红绿区分。
- 支持键盘焦点、明确 Hover/Focus/Selected/Disabled 状态。
- 长文本、超长 ID、极端数值必须有溢出策略。
- 关键运行信息在 125%/150% 系统缩放下不得被截断。

## 17. Acceptance criteria

模板实现通过以下门槛才算完成：

- 3 秒测试五问均可回答。
- 页面无真实品牌/公司/客户身份。
- 所有核心组件具备 Default/Hover/Focus/Disabled/Error 或相应状态。
- 至少覆盖 Loading/Empty/Error/Offline。
- 状态颜色与文案符合统一语义。
- 主动作唯一且位置稳定。
- 桌面 1366×768 与 1920×1080 均可操作；Web 能在常见宽度自适应。
- 移动端不直接压缩桌面布局，而是重新排列任务优先级。
