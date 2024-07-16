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
    def submit(e):
        chat.controls.append(ft.Text(tb1.value))

        page.add(chat)

        chat.controls.append(ft.Text(submitMessage(tb1.value)))
        page.add(chat)

    # add/update controls on Page
    tb1 = ft.TextField(multiline=True, autofocus=True)
    submitBtn = ft.ElevatedButton(text="送信", on_click=submit)

    page.add(tb1, submitBtn)
    chater = "You"
    repluier = "Claude"
    chat_log = []

    chat = ft.ListView(
        auto_scroll=True
    )

    pass


ft.app(target=main)
