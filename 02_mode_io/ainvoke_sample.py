import asyncio
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 非同期処理用のチェーン設定
prompt = PromptTemplate(template="{product}はどこの会社が開発した製品ですか？", input_variables=["product"])
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = prompt | model | StrOutputParser()

# 非同期関数の定義
async def process_products():
    products = ["iPhone", "Xperia", "Galaxy"]
    tasks = [chain.ainvoke({"product": product}) for product in products]
    # 全てのタスクを並行実行して結果を待つ
    results = await asyncio.gather(*tasks)
    
    for product, result in zip(products, results):
        print(f"{product}: {result}")

# 非同期関数の実行
if __name__ == "__main__":
    asyncio.run(process_products())
