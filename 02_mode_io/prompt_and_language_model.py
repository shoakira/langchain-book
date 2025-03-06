from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chat = ChatOpenAI(
    model="gpt-4o",
)

prompt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか？",
    input_variables=[
        "product"
    ]
)

result = chat.invoke(  # invokeメソッドを使用
    [
        HumanMessage(content=prompt.format(product="iPhone")),
    ]
)
print(result.content)