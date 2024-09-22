import flet as ft

def update_categories(page: ft.page):
    print(1)
    text_field = ft.Row(
        controls=[
            ft.TextField(value="Hello!!!"),
        ]
    )
    page.add(text_field)
    page.update()
    
def main(page: ft.Page):
    update_categories(page)
