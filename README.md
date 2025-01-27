# voicememo2text

OpenAIのAPIを利用して、ボイスメモをテキストに変換して要約するプログラムです。
スマートフォンなどで録音したボイスメモ「voice_files」フォルダに保存してください。
そして、以下のコマンドを実行すると、ボイスメモがテキストに変換され、要約されます。

```sh
python voicememo2text.py
```

## インストール

- Pythonをインストールしてください。
- また、ChatGPTのAPIを使うために、環境変数`OPENAI_API_KEY`にAPIキーを設定してください。
- 下記のコマンドを実行して依存ライブラリをインストールします。

```sh
pip install -r requirements.txt
```


