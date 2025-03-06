from typing import Dict, Any
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# プロンプトの定義
prompt = PromptTemplate(
    template="{product}はどこの会社が開発した製品ですか？",
    input_variables=["product"]
)

# モデルの定義
model = ChatOpenAI(
    model="gpt-4o",
    temperature=0,  # より決定論的な回答のため
)

# LCEL (LangChain Expression Language) を使用した処理チェーンの作成
chain = prompt | model | StrOutputParser()

# チェーンの実行
response = chain.invoke({"product": "iPhone"})
print(response)

# 複数の入力を処理する例（オプション）
products = ["iPhone", "Xperia", "Galaxy"]
for product in products:
    result = chain.invoke({"product": product})
    print(f"{product}: {result}")