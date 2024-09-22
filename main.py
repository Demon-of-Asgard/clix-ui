import flet as ft 


def main(page:ft.Page):
    text_field = ft.Row(controls=[
            ft.TextField(value="Hello!!!")
        ]
    ) 
    page.add(text_field)
    page.update()

ft.app(main)
