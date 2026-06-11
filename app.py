"""
app.py
智能办公助手 - 主程序

功能：
1. 知识库问答（RAG）
2. 数学计算
3. 时间查询
4. 文件读写
5. 文本分析
6. 多步任务自动编排
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

from knowledge_base import KnowledgeBase
from tools import ALL_TOOLS

load_dotenv()


def create_assistant():
    """创建智能办公助手"""

    # ============================================
    # 1. 构建知识库
    # ============================================
    kb = KnowledgeBase(docs_dir="./documents")

    # ============================================
    # 2. 把知识库检索封装成工具
    # ============================================
    from langchain_core.tools import tool

    @tool
    def search_knowledge_base(query: str) -> str:
        """搜索公司内部知识库。当用户询问公司制度、政策、流程、组织架构等
        公司内部信息时，必须使用此工具。例如：请假制度、报销流程、考勤规定等。

        Args:
            query: 搜索关键词或问题
        """
        return kb.search(query)

    # ============================================
    # 3. 组装所有工具
    # ============================================
    all_tools = ALL_TOOLS + [search_knowledge_base]

    # ============================================
    # 4. 创建 Agent
    # ============================================
    llm = ChatOpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com",
        model="deepseek-chat",
        temperature=0,
    )

    agent = create_react_agent(
        model=llm,
        tools=all_tools,
    )

    return agent


def main():
    """主函数：交互式对话"""
    print("=" * 55)
    print("   智能办公助手 v1.0")
    print("   功能：知识库问答 | 计算 | 时间 | 文件读写 | 文本分析")
    print("=" * 55)
    print()
    print("我能做什么：")
    print("  - 回答公司制度问题（如：请假制度是什么？）")
    print("  - 数学计算（如：帮我算 (5000+3000)*12）")
    print("  - 查询时间（如：现在几点了？）")
    print("  - 读写文件（如：把内容保存到文件）")
    print("  - 分析文本（如：这段话有多少字）")
    print("  - 复合任务（如：查一下报销制度，整理成要点保存）")
    print()
    print("输入 quit 退出")
    print()

    # 创建助手
    agent = create_assistant()

    while True:
        user_input = input("你：").strip()

        if user_input.lower() == "quit":
            print("\n再见！")
            break

        if not user_input:
            continue

        try:
            result = agent.invoke(
                {"messages": [HumanMessage(content=user_input)]}
            )
            answer = result["messages"][-1].content
            print(f"\n助手：{answer}\n")
        except Exception as e:
            print(f"\n出错了：{str(e)}\n")


if __name__ == "__main__":
    main()
