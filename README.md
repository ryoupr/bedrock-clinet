
# Bedrock Client

このプロジェクトは、Fletフレームワークを使用してAWS BedrockのClaudeモデルと対話するためのシンプルなクライアントアプリケーションです。ユーザーがメッセージを入力し、送信すると、Claudeモデルが応答を生成し、チャット画面に表示されます。

## 機能

- ユーザーからの入力メッセージをAWS BedrockのClaudeモデルに送信
- Claudeモデルからの応答をチャット画面に表示
- 送信ボタンのクリックまたはCtrl + Enterキーでメッセージを送信
- メッセージ送信後に入力フィールドをクリア
- メッセージ送信中に進行状況バーを表示

## 使用方法

### 必要条件

- Python 3.x
- `flet`ライブラリ
- `boto3`ライブラリ
- AWS認証情報 (適切なIAM権限が設定されていること)

### インストール

1. 必要なライブラリをインストールします。

```bash
pip install flet boto3
```

2. AWS認証情報を設定します。AWS CLIを使用して設定するか、環境変数に設定します。

### 実行

以下のスクリプトを実行します。

```python
import flet as ft
import boto3
import json


def submitMessage(message):
    bedrock = boto3.client(
        service_name="bedrock-runtime", region_name='us-east-1')

    body = json.dumps({
        "max_tokens": 256,
        "messages": [{"role": "user", "content": message}],
        "anthropic_version": "bedrock-2023-05-31"
    })

    response = bedrock.invoke_model(
        body=body, modelId="anthropic.claude-3-5-sonnet-20240620-v1:0")

    response_body = json.loads(response.get("body").read())
    return response_body.get("content")[0]["text"]


def main(page: ft.Page):
    page.title = "Bedrock Client"
    page.update()
    
    def submit(e):
        if tb1.value == "":
            return
        chat.controls.append(ft.Text(tb1.value))
        page.add(chat)
        page.add(progress_bar)
        
        text = tb1.value
        tb1.value = ""
        page.update()

        chat.controls.append(
            ft.Markdown(
                submitMessage(text),
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                on_tap_link=lambda e: page.launch_url(e.data),
            )
        )
        
        page.controls.remove(progress_bar)
        page.add(chat)
        tb1.focus()

    def on_keyboard(e: ft.KeyboardEvent):
        if tb1.value != "":
            if e.key == "Enter" and e.ctrl:
                submit(e)

    page.on_keyboard_event = on_keyboard

    tb1 = ft.TextField(multiline=True, autofocus=True, expand=True)
    chat = ft.ListView(auto_scroll=True)
    progress_bar = ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")
    
    row = ft.Row(spacing=0, controls=[tb1, ft.ElevatedButton(text="△", on_click=submit)])
    page.add(row)
    pass

ft.app(target=main)
```

### 使い方

1. スクリプトを実行すると、`Bedrock Client`ウィンドウが開きます。
2. テキストフィールドにメッセージを入力し、送信ボタン（△）をクリックするか、Ctrl + Enterキーを押してメッセージを送信します。
3. メッセージが送信されると、Claudeモデルからの応答がチャット画面に表示されます。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。
