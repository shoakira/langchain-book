import json
from openai import OpenAI  # 新しいインポート方法

# クライアントのインスタンスを作成
client = OpenAI()

# 新しい形式でAPIを呼び出す
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "iPhone8のリリース日を教えて"
        },
    ]
)

# 出力方法も変更が必要
print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))