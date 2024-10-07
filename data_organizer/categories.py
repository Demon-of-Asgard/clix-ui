import flet as ft
from typing import List 



def create_subitem_display(page:ft.Page, subitems:List=[]):
    pass 

def create_item_display(page:ft.Page, cat:str, sub_cats:dict={}, selected:bool=False):
    
    # cat = " ".join(" ".join(str(cat).split("_")).split("_")).capitalize()

    # icon = None 
    # subitem_row = ft.Row([])
    # height = 50
    # if len(sub_cats.keys()) !=0: 
    #     if selected: 
    #         icon = ft.IconButton(ft.icons.EXPAND_MORE_OUTLINED, on_click=on_click)  
    #         # subitem_row = ft.ResponsiveRow(
    #         #     controls=[ft.Container(controls=[ft.OutlinedButton(text="hi", on_click=subcat_selection,)]) for item in sub_cats.items()],
    #         #     alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    #         # )
    #         height = 200
    #         subitem_row = ft.ResponsiveRow(
    #             [
    #                 ft.OutlinedButton(text=ky.split(".")[-1], col={"md": 5}) for ky, vl in sub_cats.items()
    #             ],
    #             alignment=ft.MainAxisAlignment.START,
    #         )
            
    #     else: icon = ft.IconButton(ft.icons.EXPAND_LESS_OUTLINED, on_click=on_click)

    #     def on_click(e):
    #         nonlocal selected
    #         selected = not selected
    #         print(selected)
    #         page.update()
         
    #     def subcat_selection(e):
    #         pass

    # card = ft.Card(
    #             content=ft.Container(
    #                 ft.Column(
    #                     controls=[
    #                         ft.ListTile(
    #                             trailing=icon,
    #                             title=ft.Text(f"{cat}"),
    #                         ),
    #                         subitem_row,
    #                     ]
    #                 ),
    #                 width=page.width,
    #                 height=height,
    #                 padding=0,
    #             ),
    #         )
    selected = True
    def on_click(e):
        nonlocal selected 
        selected = not selected 
        page.update()

    if selected:
        print("Here")
        card = ft.Card(
                    content=ft.Container(
                    ft.Column(
                    controls=[
                        ft.ListTile(
                            trailing=ft.IconButton(ft.icons.EXPAND_MORE_OUTLINED, on_click=on_click) ,
                            title=ft.Text(f"{cat}"),
                        ),
                    ]
                ),
                width=page.width,
                height=50,
                padding=0,
            ),
        )
    else:
        ft.Card(
            content=ft.Container(
                ft.Column(
                    controls=[
                        ft.ListTile(
                            trailing=ft.IconButton(ft.icons.EXPAND_LESS_OUTLINED, on_click=on_click) ,
                            title=ft.Text(f"{cat}"),
                        ),
                    ]
                ),
                width=page.width,
                height=50,
                padding=0,
            ),
        )
    
    page.add(ft.Row(controls=[card]))

def render_category_list(page: ft.page, cat_subcat:dict)->None:
    # rows = []
    for key, value in cat_subcat.items():
        cat = key
        subcats = list(value.keys()) if isinstance(value, dict) else []
        page.add(
            create_item_display(page=page, cat=key, sub_cats=value)
        )   
    page.update()
    
def main(page: ft.Page, cat_subcat:dict):
    render_category_list(page, cat_subcat=cat_subcat)
