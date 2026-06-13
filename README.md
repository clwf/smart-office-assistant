<div align='center'>
  <h1>智能办公助手</h1>
  <h3>🤖 基于 LangGraph 的多功能办公助手</h3>
  <p><em>知识库问答、数学计算、时间查询、文件读写、文本分析，一站式解决办公需求</em></p>
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/LangGraph-Agent-4CAF50?style=flat" alt="LangGraph"/>
  <img src="https://img.shields.io/badge/DeepSeek-API-0066FF?style=flat" alt="DeepSeek"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License"/>
</div>

---

## 🎯 项目介绍

&emsp;&emsp;日常办公中，你是否经常需要查找公司制度、做数学计算、分析文本？这个智能助手帮你整合所有需求！

&emsp;&emsp;智能办公助手是一个基于 LangGraph 构建的 AI Agent 应用，集成了知识库问答（RAG）、数学计算、时间查询、文件读写、文本分析等多项功能。通过 ReAct 模式，AI 可以自主调用合适的工具完成复杂任务。

## ✨ 功能特点

- 📚 **知识库问答** - 基于 RAG 技术，回答公司制度、政策、流程等问题
- 🔢 **数学计算** - 支持复杂表达式计算，如 `(5000+3000)*12`
- ⏰ **时间查询** - 获取当前日期和时间
- 📁 **文件读写** - 读取和保存文件内容
- 📊 **文本分析** - 字数统计、关键词提取等
- 🤖 **智能编排** - 自动组合多个工具完成复杂任务

## 📚 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API 密钥

在项目根目录创建 `.env` 文件：

```env
DEEPSEEK_API_KEY=your_api_key_here
```

### 3. 添加知识库文档

将公司制度、政策等文档放入 `documents/` 目录，支持 txt、md 等格式。

### 4. 运行程序

```bash
python app.py
```

## 📖 使用示例

```
=======================================================
   智能办公助手 v1.0
   功能：知识库问答 | 计算 | 时间 | 文件读写 | 文本分析
=======================================================

我能做什么：
  - 回答公司制度问题（如：请假制度是什么？）
  - 数学计算（如：帮我算 (5000+3000)*12）
  - 查询时间（如：现在几点了？）
  - 读写文件（如：把内容保存到文件）
  - 分析文本（如：这段话有多少字）
  - 复合任务（如：查一下报销制度，整理成要点保存）

输入 quit 退出

你：公司的请假制度是什么？

助手：根据公司制度，请假规定如下：
1. 年假：工作满1年享有5天年假，满10年享有10天
2. 病假：需提供医院证明，每年累计不超过30天
...
```

## 📁 项目结构

```
smart-office-assistant/
├── app.py              # 主程序（Agent 核心逻辑）
├── knowledge_base.py   # 知识库管理（RAG）
├── tools.py            # 工具定义
├── requirements.txt    # 依赖列表
├── documents/          # 知识库文档目录
├── chroma_db/          # 向量数据库
├── models/             # 模型相关文件
├── output/             # 输出文件目录
├── README.md           # 项目说明
└── .env                # API 密钥配置
```

## 🔧 技术栈

- **Python 3.8+** - 主要编程语言
- **LangChain** - LLM 应用开发框架
- **LangGraph** - Agent 编排框架
- **ChromaDB** - 向量数据库
- **DeepSeek API** - 大语言模型服务

## 💡 如何学习

&emsp;&emsp;本项目是学习 LangGraph Agent 开发的绝佳实践。通过这个项目，你将学习到：

- 如何使用 LangGraph 构建 Agent
- 如何实现 RAG（检索增强生成）
- 如何设计和注册自定义工具
- 如何实现多工具协作

&emsp;&emsp;建议你先阅读 `tools.py` 了解工具的定义方式，再阅读 `app.py` 理解 Agent 的编排逻辑。

## 🤝 如何贡献

欢迎任何形式的贡献！

- 🐛 **报告 Bug** - 发现问题请提交 Issue
- 💡 **提出建议** - 有更好的想法欢迎讨论
- 📝 **完善功能** - 提交你的 Pull Request
- 📚 **丰富知识库** - 添加更多公司制度文档

## 📜 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。