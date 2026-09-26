# UI Generation Prompts

## Base prompt — 中文

为一个通用工业软件界面设计可交付 UI。使用“工业简洁A”设计语言：浅色桌面工程软件，白色/浅灰背景，蓝色交互强调，中性灰边框；信息密度高但层级清楚。根据任务使用顶部上下文区、左侧导航或任务树、中央主工作区、右侧属性/参数面板、底部状态或日志区。控件应像真实工程软件：表格、分组、复选框、单选框、数值输入、下拉框、阈值、状态指示、趋势图与明确的运行状态。不要添加任何公司名、Logo、商标、客户名、真实域名或品牌化产品名。不要模仿任何特定厂商的专有界面。不要做赛博朋克、霓虹、游戏 HUD、营销 SaaS 首页或装饰性科技大屏。

## Base prompt — English

Design a production-ready, brand-neutral industrial software interface using the Industrial Clean A design language: light engineering UI, white and light-gray surfaces, blue interaction accents, neutral gray borders, high information density with clear hierarchy. Use context bar, navigation/task tree, primary workspace, contextual properties/parameters, and status/log regions only when the task needs them. Controls should feel operational and real: tables, grouped settings, checkboxes, radios, numeric inputs, dropdowns, thresholds, status indicators, trends, and explicit machine/application states. Do not include any company name, logo, trademark, customer identity, real domain, or branded product name. Do not imitate a specific vendor's proprietary interface. Avoid cyberpunk, neon, game HUD, marketing SaaS landing-page styling, and decorative sci-fi dashboards.

## Scene prompt formula

Use the base prompt, then append:

```text
当前场景：<scene name>
场景目标：<scene description>
优先信息：位置、状态、关键结果、异常、下一步动作。
仅展示完成当前任务所需的面板与控件。
```

## Scene references

### 01. 视觉检测软件主工作台

中央为实时图像视图，叠加检测 ROI、OK/NG 判定框、缺陷框和测量线；左侧为任务树，右侧为检测工具属性，底部为运行日志和通讯状态。

### 02. 工具目录 / Application Navigator

引导式工具选择界面，按检测目的分类：有无检测、尺寸测量、边缘、定位、颜色、字符识别、条码、AI 分类、AI 分割、机器人标定。

### 03. 检测流程 Task View

用纵向步骤列表或节点链路展示检测流程：图像采集、定位、预处理、工具执行、判定、数据输出、保存图像、PLC 通讯。

### 04. Image View 图像视图

大画布显示产品图像，叠加十字光标、坐标、ROI 框、边缘线、测量标注、缺陷标签、缩放控件和图像直方图。

### 05. Properties View 属性面板

右侧属性面板展示当前工具参数：阈值、搜索区域、边缘方向、灵敏度、最小面积、最大面积、判定条件、输出变量。

### 06. 相机连接与采集设置

设备列表、GigE/USB 相机连接、IP 地址、分辨率、帧率、曝光、增益、触发模式、软触发按钮、实时预览。

### 07. 光源控制与图像优化

多通道光源亮度、频闪、延时、极性、亮场/暗场模式、图像增强、自动曝光、最佳图像一键优化。

### 08. AI 缺陷检测配置

AI 检测工具配置界面，包含样本列表、训练状态、缺陷类别、置信度阈值、检测框、误检复判、AI 与规则工具组合。

### 09. 规则型缺陷检测配置

传统规则工具界面，包含模板匹配、边缘检测、面积筛选、颜色阈值、Blob 分析、计数、位置偏移和判定逻辑。

### 10. 2D 尺寸测量

显示长度、宽度、直径、间距、角度、圆度、同心度、位置度等测量项，图像上有测量线和明确的合格/不合格结果。

### 11. 3D 高度/轮廓测量

展示高度热力图、激光轮廓曲线、截面分析、台阶差、平面度、最大高度、最小高度和 OK/NG 阈值表。

### 12. OCR / 条码读取

字符识别和一维码/二维码读取界面，包含识别区域、读取结果、置信度、误读报警、历史记录、字符模板。

### 13. 机器人视觉标定

手眼标定界面，包含标定板图像、相机坐标、机器人坐标、抓取点、偏移补偿、标定误差和通讯状态。

### 14. 配方管理

产品型号配方列表，包含配方名、版本、相机参数、检测工具数量、启用状态、复制、导入、导出、权限确认。

### 15. 生产运行 HMI 首页

适合产线触摸屏，显示设备状态、当前配方、检测总数、OK 数、NG 数、良率、节拍、开始/停止/复位/清零按钮。

### 16. 报警中心

报警列表界面，按等级显示报警代码、发生时间、工位、原因、处理步骤、确认人、恢复状态和维护建议。

### 17. 质量分析 Yield Table

良率管理表格，显示按班次、工位、产品型号、缺陷类别统计的 OK率、NG率、缺陷数量、趋势和导出按钮。

### 18. 趋势图 / Quality Analysis Graph

质量趋势分析图，显示良率趋势、缺陷类别趋势、节拍变化、相机离线次数、报警频次和工位对比。

### 19. 追溯查询

按批次、SN、时间、工位、相机编号查询历史检测记录，包含原图、结果图、缺陷图、参数快照和导出报告。

### 20. 多工位设备总览

多相机多工位总览，展示工位1-8状态、相机在线、PLC通讯、光源状态、机器人状态、工位良率和报警灯。

### 21. 用户权限与操作记录

用户登录、角色权限、工程师/操作员/管理员权限矩阵、参数修改记录、审计日志和电子签名。

### 22. 离线仿真 / PC Simulation

在 PC 上导入历史图片进行离线调试，显示图片列表、批量运行、结果对比、参数调整、误判样本复盘。

### 23. 通讯 IO / PLC 映射

输入输出映射界面，包含触发输入、完成输出、OK/NG 输出、心跳、寄存器地址、通讯协议状态和测试按钮。

### 24. 数据导出与报表设置

配置 CSV、Excel、PDF、数据库、MES 上传字段，包含字段映射、上传周期、失败重试、文件路径和报表模板。

