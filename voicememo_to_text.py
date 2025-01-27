import os
from pathlib import Path
from datetime import datetime
import openpyxl
from speech_to_text import speech_to_text
from chatgpt_hello import create

# フォルダ内にある音声ファイルを列挙して、文字起こしを行って、要約を作成してExcelファイルに保存する関数
def process_audio_files(input_folder, output_file):
    # 入力フォルダを取得
    input_path = Path(input_folder)
    if not input_path.exists():
        print(f"フォルダ {input_folder} が見つかりません。")
        return

    # 出力用のExcelファイル作成
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Transcription Report"

    # ヘッダーを設定
    headers = ["作成日時", "元ファイル名", "要約", "テキスト全文"]
    sheet.append(headers)

    # 対応する音声ファイルの拡張子
    audio_extensions = [".mp3", ".m4a", ".wav", ".webm"]

    # フォルダ内のファイルを処理
    for audio_file in input_path.iterdir():
        if audio_file.suffix.lower() in audio_extensions:
            print(f"### 処理中: {audio_file.name}")
            try:
                # ファイルの作成日時
                created_time = datetime.fromtimestamp(audio_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                # 文字起こし
                transcription = speech_to_text(str(audio_file))
                print("> 文字起こし:", transcription)
                # 要約
                prompt = (
                    "指示: 入力を150文字以内に要約してください。誤字脱字があれば直してください。\n" 
                    f"入力: ```{transcription}```\n"
                )
                summary = create(prompt)
                print("> 要約:", summary)
                # テキストファイルに保存
                text_file = audio_file.with_suffix(".txt")
                with open(text_file, "w") as f:
                    f.write("### 要約:\n" + summary + "\n\n")
                    f.write("### テキスト:\n" + transcription + "\n")
                # シートに追加
                sheet.append([created_time, audio_file.name, summary, transcription])
            except Exception as e:
                print(f"エラーが発生しました: {audio_file.name} - {e}")

    # Excelファイルを保存
    workbook.save(output_file)
    print(f"レポートが作成されました: {output_file}")

if __name__ == "__main__":
    # 入力フォルダと出力ファイルを設定
    input_folder = "voice_files"
    output_file = "voice-memo.xlsx"

    # 音声ファイルを処理
    process_audio_files(input_folder, output_file)
