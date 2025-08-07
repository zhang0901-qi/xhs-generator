from pydantic import BaseModel, Field
# 导入数据验证工具：BaseModel：创建数据模型的基类，用于定义数据结构；Field：给数据字段添加规则（比如"必须5个标题"）
from typing import List
# List 用于指定字段的数据类型为列表，这里用于定义 titles 字段是一个字符串列表

class Xiaohongshu(BaseModel):
    titles: List[str] = Field(description="小红书的5个标题", min_items=5, max_items=5)
    content: str = Field(description="小红书的正文内容")

#定义小红书文案的数据结构：
# titles: 这是一个包含 5 个字符串的列表，表示小红书文章的标题。
# content: 这是一个字符串，表示小红书文章的正文内容。
# Field 提供了字段的描述和验证规则
#相当于创建了一个"合格小红书文案"的检查标准