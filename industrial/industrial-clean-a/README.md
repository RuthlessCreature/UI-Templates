# 工业简洁A / Industrial Clean A

**Template ID:** `industrial-clean-a`  
**Version:** `1.0.0`  
**Positioning:** 浅色、高信息密度、工程导向、状态清楚、操作直接的工业软件界面。  
**Brand policy:** 完全中立。基础模板不承载任何公司、产品、客户或供应商品牌身份。

![Industrial Clean A neutral preview](./preview/overview.svg)

## 24 场景索引

![Industrial Clean A 24-scene contact sheet](./preview/contact-sheet.svg)

## 适用场景

- 工业机器视觉与检测软件
- 设备调试与工程配置工具
- HMI / 产线运行界面
- 配方、报警、日志、追溯、质量分析
- 机器人、相机、PLC、IO 等工程工具
- 对应产品的 Web 管理端、移动端和方案 PPT

## 核心视觉语言

- 白色与浅灰为主背景，蓝色仅承担交互强调与当前选中状态。
- 中性灰边框，少量轻阴影；不使用大面积渐变、炫光、玻璃拟态、霓虹和装饰性 3D。
- 典型桌面结构：顶部上下文区 + 左侧导航/任务树 + 中央主工作区 + 右侧属性区 + 底部状态/日志区。
- 高密度信息可以存在，但必须有明确层级、稳定对齐和可扫描性。
- 工业状态采用统一语义，不允许同一颜色在不同页面表达相反含义。

## 使用顺序

1. `SPEC.md` — 总规范与设计决策。
2. `SCREEN_CONTRACT.md` — 页面开工前先定义用户、任务、L1 信息、异常与主动作。
3. `layouts/LAYOUTS.md` — 选择工程工作台、运行 HMI、数据分析等布局配方。
4. `tokens/tokens.json` — 机器可读设计令牌。
5. `components/COMPONENTS.md` — 组件行为与状态。
6. `platforms/*.md` — Desktop / Web / Mobile / PPT 跨端适配。
7. `scenes/SCENES.md` — 24 个工业场景参考。
8. `prompts/UI_GENERATION.md` — 用于生成/实现界面的中立提示词。
9. `CHECKLIST.md` — 验收前检查。
10. `examples/demo.html` — 无品牌静态示例。

## 禁止事项

- 不放 Logo、商标、公司名、客户名、真实域名、真实账号。
- 不写“像某某品牌”“模仿某某产品”等依附式风格描述。
- 不以赛博朋克大屏代替可操作的工程软件。
- 不为“科技感”牺牲状态辨识度、表格扫描效率或参数编辑效率。

## Validation

Repository pushes and pull requests run `scripts/validate_template.py` through GitHub Actions. The validator checks required structure, the 24-scene registry, brand-neutral declarations, and forbidden identity contamination.
