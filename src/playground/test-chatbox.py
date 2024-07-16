import flet as ft

def main(page: ft.Page):
    page.title = "チャットボックス"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 10

    # チャットリストを作成
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=True,
    )

    def add_message(e):
        if message_input.value:
            chat_list.controls.append(ft.Text(value=message_input.value))
            message_input.value = ""
            page.update()

    # メッセージ入力フィールドと送信ボタンを作成
    message_input = ft.TextField(hint_text="メッセージを入力してください...", expand=True)
    send_button = ft.ElevatedButton(text="送信", on_click=add_message)

    # レイアウト調整
    input_row = ft.Row([message_input, send_button], alignment=ft.MainAxisAlignment.CENTER)
    chat_container = ft.Column([chat_list, input_row], expand=True)

    # ページに要素を追加
    page.add(chat_container)

ft.app(target=main)
