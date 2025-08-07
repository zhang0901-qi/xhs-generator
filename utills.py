
from langchain.output_parsers import PydanticOutputParser
# 导入一个"输出解析器"，它的作用是把AI生成的文本转换成结构化数据（就像把杂乱的文章整理成表格）这里我们使用它来确保模型的输出符合 Xiaohongshu 类的定义。
from prompt_template import system_template_text, user_template_text
# 从另一个文件导入两个预设的"对话模板"：
# system_template_text：告诉AI扮演什么角色（比如"你是一个小红书文案专家"）
# user_template_text：用户提问的格式模板
from langchain_community.chat_models import ChatTongyi
from langchain.prompts import ChatPromptTemplate
# 导入"对话模板工具"，用来组合系统提示和用户提示
from xhs_model import Xiaohongshu
import os

def generate_xhs(theme, qwen_api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatTongyi(model = "qwen-turbo", api_key = qwen_api_key)
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    #PydanticOutputParser 用于将模型的输出解析为符合 Xiaohongshu 模型的数据结构；pydantic_object=Xiaohongshu 指定了解析的目标模型。
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result
#(generate_xhs("螺蛳粉", os.getenv("DASHSCOPE_API_KEY")))