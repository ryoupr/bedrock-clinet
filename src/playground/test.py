import flet as ft

def main(page: ft.Page):
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Enter" :
            if e.ctrl:
                # 処理
                pass

    page.on_keyboard_event = on_keyboard

ft.app(target=main)