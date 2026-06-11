"""
tools.py
定义 Agent 可以使用的所有工具
"""

import os
from datetime import datetime
from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """计算数学表达式。支持加减乘除、括号、幂运算等。
    当用户需要做数学计算时使用此工具。

    Args:
        expression: 数学表达式，例如 "(5000+3000)*12" 或 "2**10"
    """
    try:
        import numexpr
        result = numexpr.evaluate(expression)
        return f"计算结果：{expression} = {result.item()}"
    except Exception as e:
        return f"计算出错：{str(e)}"


@tool
def get_current_datetime() -> str:
    """获取当前的日期和时间，包含星期几。
    当用户问"现在几点"、"今天星期几"、"今天几号"时使用此工具。
    """
    now = datetime.now()
    weekdays = ["一", "二", "三", "四", "五", "六", "日"]
    weekday = weekdays[now.weekday()]
    return (
        f"当前时间：{now.strftime('%Y年%m月%d日')} "
        f"星期{weekday} "
        f"{now.strftime('%H:%M:%S')}"
    )


@tool
def read_file(file_path: str) -> str:
    """读取指定文件的内容。当用户要求查看或读取某个文件时使用。

    Args:
        file_path: 文件路径，例如 "output/report.md"
    """
    try:
        # 安全检查：只允许读取项目目录下的文件
        abs_path = os.path.abspath(file_path)
        if not abs_path.startswith(os.path.abspath(".")):
            return "安全限制：只能读取项目目录下的文件。"

        if not os.path.exists(file_path):
            return f"文件不存在：{file_path}"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if len(content) > 5000:
            content = content[:5000] + "\n\n... (文件内容过长，已截断)"

        return f"文件 {file_path} 的内容：\n\n{content}"
    except Exception as e:
        return f"读取文件出错：{str(e)}"


@tool
def write_file(input_string: str) -> str:
    """将内容写入文件。当用户要求保存内容、生成报告、写文件时使用。

    Args:
        input_string: 格式为 "文件路径|||文件内容"，例如 "output/report.md|||# 报告内容..."
        注意：文件路径和内容之间用 ||| 分隔。
    """
    try:
        if "|||" not in input_string:
            return "格式错误。请使用 '文件路径|||文件内容' 的格式。"

        file_path, content = input_string.split("|||", 1)
        file_path = file_path.strip()

        # 安全检查
        abs_path = os.path.abspath(file_path)
        if not abs_path.startswith(os.path.abspath(".")):
            return "安全限制：只能写入项目目录下的文件。"

        # 确保目录存在
        os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"文件已保存：{file_path}（共 {len(content)} 个字符）"
    except Exception as e:
        return f"写入文件出错：{str(e)}"


@tool
def text_analyzer(text: str) -> str:
    """分析文本的基本信息：字数、行数、段落数。
    当用户要求统计字数或分析文本时使用。

    Args:
        text: 需要分析的文本内容
    """
    char_count = len(text)
    char_no_space = len(text.replace(" ", "").replace("\n", ""))
    line_count = len(text.split("\n"))
    word_count = len(text.split())
    paragraph_count = len([p for p in text.split("\n\n") if p.strip()])

    return (
        f"文本分析结果：\n"
        f"  总字符数：{char_count}\n"
        f"  字符数（不含空格换行）：{char_no_space}\n"
        f"  行数：{line_count}\n"
        f"  词数（按空格分割）：{word_count}\n"
        f"  段落数：{paragraph_count}"
    )


# 所有工具的列表
ALL_TOOLS = [calculator, get_current_datetime, read_file, write_file, text_analyzer]
