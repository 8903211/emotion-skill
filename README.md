# 情绪.skill

> 从授权微信聊天记录，到个人关系画像、关系意义分析、边界地图、聊天建议、可改编话术和 Obsidian 关系知识库。

![License Non-Commercial](https://img.shields.io/badge/License-Non--Commercial-red.svg)
![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-6aa84f)
![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-1f77b4)
![Runtime](https://img.shields.io/badge/Runtime-Claude%20Code%20%7C%20Codex%20%7C%20Cursor%20%7C%20OpenClaw%20%7C%20Hermes-7b2cbf)

## 它解决什么问题

很多关系里的内耗，不是因为你不会回消息，而是因为你看不清聊天背后的结构，也看不清自己在关系里的模式：

- 从聊天记录反推：你在关系里是什么样的人？
- 这段关系对你意味着什么：陪伴、确认、依赖、补偿，还是消耗？
- 对方是在表达想念，还是在用指责要确认？
- 你是在正常解释，还是已经进入自证和补救循环？
- 一段聊天为什么会从轻松变成审问？
- 哪些话现在能发，哪些话只会让关系更重？

情绪.skill 把授权微信聊天记录变成可分析的证据层，再输出个人关系画像、关系意义判断、关系动态、边界建议和可直接改编的聊天表达。

更推荐的用法不是只问一次“现在怎么回”，而是把每次分析保存成自己的 Obsidian / Markdown 知识库：长期记录关系模式、触发点、边界变化、有效话术和复盘结论。

## 完整流程

```text
准备授权聊天记录
        ↓
选择会话和时间范围
        ↓
标准化 JSON / JSONL / CSV / TXT
        ↓
建立证据地图
        ↓
分析关系结构和聊天动态
        ↓
输出行动建议、回复草稿、话术参考
        ↓
保存到 Obsidian / Markdown 知识库
```

## 能输出什么

### 关系复盘

- 时间范围和数据范围
- 双方消息节奏变化
- 情绪触发点
- 边界被突破的位置
- 冲突、修复、冷淡、靠近的循环
- 当前关系阶段判断
- 未来 24 到 72 小时建议

### 个人关系画像

- 你在聊天里的表达习惯
- 你容易被什么触发
- 你什么时候会进入解释、自证或补救
- 你在关系里的付出方式和边界模式
- 你对亲密、确认、陪伴和安全感的需求

### 关系意义分析

- 这段关系对你提供了什么心理功能
- 它为什么会牵动你的情绪
- 它是在支持你，还是消耗你
- 哪些期待来自对方，哪些期待来自你自己
- 你真正想要的是关系推进、稳定陪伴，还是情绪确认

### 聊天建议

- 当前这句话该不该回
- 推荐回复
- 更软版本
- 更轻松版本
- 不建议发送的话
- 为什么这样回更稳

### 话术库

- 早安、晚安、没回消息
- 对方指责时的低压回应
- 拒绝和冷淡后的收回方式
- 调动聊天氛围的方法
- 从一问一答转成有画面的小场景

### Obsidian 知识库沉淀

- 每段关系的阶段复盘
- 个人关系画像的长期变化
- 触发点、边界和消耗来源
- 可复用回复和禁用话术
- 周复盘、月复盘和关系对比
- 可继续追踪的下一步观察点

推荐目录：

```text
Relationship-KB/
├─ 00_inbox/                 # 临时聊天片段和待分析材料
├─ people/                   # 每个联系人或关系对象的长期笔记
├─ reports/                  # 单次分析报告
├─ phrase-library/           # 可改编话术库
├─ weekly-review/            # 每周关系复盘
└─ boundaries.md             # 自己的边界原则和提醒
```

## 使用建议

1. **先小范围分析**：一次只选一个联系人、一个时间段或一个事件窗口，不要一上来把所有聊天记录都丢进去。
2. **保存结论，不保存原始隐私**：Obsidian 里优先存证据摘要、模式判断和行动建议，不要长期堆完整私密聊天原文。
3. **把“现在怎么回”和“我为什么这样反应”分开看**：前者解决当下沟通，后者才会减少反复内耗。
4. **每周做一次关系复盘**：记录这一周哪些互动让你舒服，哪些互动让你解释、自证、焦虑或失去生活重心。
5. **沉淀自己的话术库**：把真的发出去且有效的话存下来，按“降压、边界、修复、轻松开启话题、结束对话”分类。
6. **对比不同关系里的自己**：看你在谁面前更轻松，在谁面前更容易补救、讨好、过度解释或失去边界。
7. **把建议当草稿，不当命令**：skill 给的是结构判断和表达参考，真正发送前要改成你自己的语气。

## 安装

把整个目录复制到你的 agent skills 目录：

```bash
~/.agents/skills/wechat-relationship-analysis
```

或项目级目录：

```bash
<your-project>/.agents/skills/wechat-relationship-analysis
```

然后在 Codex、Claude Code、Cursor、OpenClaw、Hermes 等支持 Agent Skills 的 runtime 中使用。

> 说明：公开展示名是「情绪.skill」。当前目录和调用名暂时保留为 `wechat-relationship-analysis`，方便兼容英文 runtime 和已有安装方式。

## 使用示例

```text
用 $wechat-relationship-analysis 分析我导出的微信聊天记录。
对象是某个联系人，时间范围是最近三天。
重点看我在这段关系里是什么状态、这段关系对我意味着什么，以及现在怎么回。
输出一份适合保存到 Obsidian 的 Markdown 复盘。
```

```text
用 $wechat-relationship-analysis 看这段聊天。
我想知道对方这句话是在表达需要，还是在用指责要确认。
给我 3 个自然一点的回复，不要像模板。
顺便帮我把可复用的话术整理进话术库格式。
```

## 输入格式

推荐 JSON：

```json
{
  "chat": "display name",
  "exported_at": "2026-01-03 09:32:25",
  "date_first_msg": "2026-01-01 00:14:54",
  "date_last_msg": "2026-01-03 09:01:21",
  "messages": [
    {
      "timestamp": "2026-01-03 08:12:00",
      "sender": "me",
      "type": "text",
      "content": "message text"
    }
  ]
}
```

也支持：

- JSON array
- JSONL
- CSV
- TXT copied transcript

可以先用脚本标准化：

```bash
python scripts/normalize_chat_export.py exported_chats --output normalized.jsonl
```

## 隐私边界

这个 skill 只处理本人或已授权提供的聊天记录。

它不会帮助你：

- 访问他人账号
- 绕过微信安全机制
- 破解设备或数据库
- 窃取密码、密钥或隐私数据
- 输出完整私密聊天原文作为公开内容

默认做法是：保留证据摘要，不在最终回答里倾倒完整聊天记录。

## 项目结构

```text
wechat-relationship-analysis/       # 展示名：情绪.skill
├─ SKILL.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ data-preparation.md
│  ├─ analysis-framework.md
│  ├─ phrase-frameworks.md
│  └─ output-templates.md
└─ scripts/
   └─ normalize_chat_export.py
```

## 工作原理

分析不是只看一句话，而是先把聊天拆成五层：

1. **事实层**：谁在什么时候说了什么，哪里有断点、指责、解释、修复。
2. **自我层**：你在这段聊天里呈现出什么关系模式、情绪需求和边界习惯。
3. **结构层**：交换、权力、边界、阶段、叙事是否失衡。
4. **表达层**：现在应该降压、修复、收住，还是轻轻把氛围聊起来。
5. **沉淀层**：把一次性建议保存成 Obsidian / Markdown 笔记，长期追踪自己的关系模式。

它不会鼓励操控式 PUA，而是把聊天变成更清楚、更尊重边界、更能落地的表达。

## License / 使用授权

本项目仅允许个人学习、研究和非商业使用。

未经作者书面许可，不得将本项目或其衍生版本用于任何商业产品、付费服务、企业内部工具、培训课程、SaaS 服务、咨询交付、关系分析服务、情绪分析服务、聊天分析服务或其他商业场景。

Commercial use is not permitted without prior written permission from the copyright holder.

See [LICENSE](LICENSE) for details.
