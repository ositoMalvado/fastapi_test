import flet as ft
import flet_fastapi
import random

class PokeImage(ft.Container):


    async def change_pokemon(self, e):
        if e.control.data == 'anterior':
            if self.poke_index == 1:
                self.poke_index = self.max_index
            else:
                self.poke_index -= 1
        elif e.control.data == 'siguiente':
            if self.poke_index == self.max_index:
                self.poke_index = 1
            else:
                self.poke_index += 1
        elif e.control.data == 'random':
            self.poke_index = random.randint(1, self.max_index)
            
        await self.update_pokemon()

    async def update_pokemon(self):
        self.imagen_switcher.content = ft.Image(
            src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{self.poke_index}.svg",
            width=300,
            height=300
        )
        await self.imagen_switcher.update_async()

    def __init__(self):
        super().__init__()
        self.poke_index = 1
        self.max_index = 600
        self.imagen = ft.Image(
            src=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{self.poke_index}.svg",
            width=300,
            height=300
        )
        self.imagen_switcher = ft.AnimatedSwitcher(
            self.imagen,
            transition=ft.AnimatedSwitcherTransition.SCALE,
            duration=1000,
            reverse_duration=800,
            switch_in_curve=ft.AnimationCurve.FAST_OUT_SLOWIN,
            switch_out_curve=ft.AnimationCurve.FAST_OUT_SLOWIN,
        )
        self.content = ft.Column(
            [
                self.imagen_switcher,
                ft.Row(
                    [
                        ft.IconButton(
                            ft.icons.ARROW_BACK_IOS,
                            data="anterior",
                            on_click=self.change_pokemon
                        ),
                        # random button
                        ft.IconButton(
                            ft.icons.REFRESH,
                            data="random",
                            on_click=self.change_pokemon
                        ),
                        ft.IconButton(
                            ft.icons.ARROW_FORWARD_IOS,
                            data="siguiente",
                            on_click=self.change_pokemon
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        self.width = 300
        # self.height = 500
        self.border = ft.border.all(5, ft.colors.RED)
        # self.alignment = ft.alignment.center


async def main(page: ft.Page):
    page.spacing = 0
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    await page.add_async(
        PokeImage()
    )

app = flet_fastapi.app(main)
# ft.app(target=main)
