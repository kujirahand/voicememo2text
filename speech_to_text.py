from openai import OpenAI

# APIを利用するクライアントを作成する
client = OpenAI()

# 音声ファイルをテキストに変換する関数を定義
def speech_to_text(audio_file_path):
    # ファイルを開く
    with open(audio_file_path, "rb") as fp:
        # APIを呼び出す
        result = client.audio.transcriptions.create(
            model="whisper-1",
            file=fp)
        return result.text

if __name__ == "__main__":
    # オーディオファイルを指定して変換
    audio_file_path = "voice-memo/test.mp3"
    print(speech_to_text(audio_file_path))
