import flet as ft
import flet_fastapi


class TextInput(ft.TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


async def main(page: ft.Page):
    await page.add_async(
        TextInput(label="Hello, Flet!"),
        TextInput(label="Chau Flet!")
    )

app = flet_fastapi.app(main)