import flet as ft


class Message(ft.Container):
    def __init__(self, author, body):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(author, weight=ft.FontWeight.BOLD),
                ft.Text(body),
            ],
        )
        self.border = ft.border.all(1, ft.colors.BLACK)
        self.border_radius = ft.border_radius.all(10)
        self.bgcolor = ft.colors.GREEN_200
        self.padding = 10
        self.expand = True
        self.expand_loose = True


def main(page: ft.Page):
    
    chater = "You"
    repluier="Claude"
    chat_log = [
        ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
                Message(
                    author=chater,
                    body="Hi, how are you?",
                ),
            ],
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                Message(
                    author=repluier,
                    body="Hi I am good thanks, how about you?",
                ),
            ],
        )
    ]
    
    chat = ft.ListView(
        padding=10,
        spacing=10,
        controls=chat_log,
    )

    page.window.width = 393
    page.window.height = 600
    page.window.always_on_top = False

    page.add(chat)


ft.app(target=main)
