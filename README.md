# 💼 AI 金融助手 (AI Financial Assistant)

基于大语言模型（LLM）与本地知识库的智能金融问答系统。

本项目从零开始实现了一套完整的 **RAG（检索增强生成）** 架构，支持本地私有化部署，旨在解决通用大模型在金融垂直领域存在的“知识幻觉”和“数据隐私”问题。通过外接私有金融知识库，让 AI 助手能够基于真实的金融文档、财报、研报等进行精准回答。

## ✨ 核心亮点

- **🔒 私有化与数据安全**：支持本地部署 `ChatGLM2-6B` 模型，金融敏感数据无需上传云端，保障数据隐私。
- **🧠 全流程 RAG 架构**：覆盖从中文数据处理、词向量模型训练、文档向量化到向量数据库检索的完整链路。
- **🔧 混合模型支持**：内置灵活切换机制，支持 OpenAI API 与本地 ChatGLM 模型无缝切换；支持 OpenAI Embedding 或自训练 Word2Vec 进行文本向量化。
- **📈 垂直领域优化**：针对金融语料进行清洗与处理，提升专业词汇的向量化匹配准确度。

## 🛠️ 技术架构与栈

- **大语言模型**：ChatGLM2-6B（本地部署）/ OpenAI (GPT-3.5/4)
- **词向量模型**：Word2Vec（支持自定义语料训练）/ OpenAI Embedding
- **向量数据库**：ChromaDB (默认，可通过配置更改)
- **核心框架**：Python, PyTorch, Transformers, LangChain (可选)
<img width="1412" height="1280" alt="微信图片_20261117200206" src="https://github.com/user-attachments/assets/83164dcd-149d-4948-818c-9069f9f65122" />
<img width="1412" height="1280" alt="微信图片_20261117200202" src="https://github.com/user-attachments/assets/2ee1fc9f-23db-4c7b-be5a-9407066300cc" />
<img width="1412" height="1280" alt="微信图片_20261117200156" src="https://github.com/user-attachments/assets/0efca15d-5d2a-4d10-ba0e-5467c1afea5a" />

## 📂 项目结构

```text
├── corpus/               # 存放金融领域的知识库文档 (txt/pdf等)
├── data/                 # 词向量模型训练相关的数据集与模型文件
├── doc/                  # 词向量训练源码、搭建教程与说明文档
├── llm_server/           # Web 应用服务端代码 (知识库应用)
├── bert_db/              # 知识库向量化与存储脚本
└── config.json           # 全局配置文件
