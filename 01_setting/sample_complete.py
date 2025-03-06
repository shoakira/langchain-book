import json
from openai import OpenAI

# クライアントのインスタンスを作成
client = OpenAI()

# 新しい形式でAPIを呼び出す
response = client.completions.create(
    model="gpt-3.5-turbo-instruct",  # engineではなくmodelを使用
    prompt="今日の天気がとても良くて、気分が",
    stop="。",
    max_tokens=100,
    n=2,
    temperature=0.5
)

# 出力方法も変更
print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))