from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chat = ChatOpenAI(
    model="gpt-4o",
)

result = chat.invoke(  # __call__の代わりにinvokeメソッドを使用
    [
        HumanMessage(content="こんにちは！"),
    ]
)
print(result.content)
