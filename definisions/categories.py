import flet as ft
from ..definisions import path_definitions

def render_category_list(page: ft.page)->None:

    text_field = ft.Row(
        controls=[
            ft.TextField(value="Ello!!!"),
        ]
    )
    page.add(text_field)
    page.update()
    
def main(page: ft.Page):
    update_categories(page)
