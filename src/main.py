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
    # Clear text field

    
    # return replay text.
    return response_body.get("content")[0]["text"]




def main(page: ft.Page):
    page.title = "Bedrock Client"
    
    
    page.update()
    
    # 送信処理を設定
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

    # キーボードイベントを受信
    def on_keyboard(e: ft.KeyboardEvent):
        if tb1.value != "":
            if e.key == "Enter" :
                if e.ctrl:
                    # 処理
                    submit(e)

    page.on_keyboard_event = on_keyboard

    tb1 = ft.TextField(multiline=True, autofocus=True,expand=True)
    
    chat = ft.ListView(
        auto_scroll=True
    )
    
    progress_bar = ft.ProgressBar(width=400, color="amber", bgcolor="#eeeeee")

    
    #####
    row = ft.Row(spacing=0,controls=[tb1,ft.ElevatedButton(text="△", on_click=submit)])
    
    page.add(row)

    pass


ft.app(target=main)
