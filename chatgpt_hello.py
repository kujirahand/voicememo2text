import openai

# OpenAIクライアントを生成 --- (*1)
client = openai.OpenAI()

# ChatGPTのAPIを呼び出す関数を定義 --- (*2)
def create(prompt, model="gpt-4o-mini", max_tokens=1000):
    try:
        # APIを呼び出す --- (*3)
        response = client.chat.completions.create(
            model=model,  # 利用したいモデルを指定
            messages=[{"role": "user", "content": prompt}],
            temperature=0.8,  # ランダム性の制御
            max_completion_tokens=max_tokens,  # 応答の最大長
        )
        # 応答内容を取得
        message = response.choices[0].message.content
        return message
    except Exception as e:
        return f"エラーが発生しました: {e}"

# 実行して結果を表示 --- (*4)
if __name__ == "__main__":
    # ChatGPTに送信するプロンプト
    prompt = "みんなが知らないExcelの裏技を一言で教えてください。"
    print(f"> {prompt}")
    print(create(prompt))
