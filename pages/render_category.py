import flet as ft
from typing import List

def render_cat_and_subcat(page:ft, items_list:List, selection_idx=2):
    for item in items_list:
        title = " ".join(' '.join(item.title.split('-')).split('_')).upper()
        if item.id != selection_idx:
            t = ft.Text(value=title)
        else:
            t = ft.Text(value=title, color='green')

        card = ft.Card(
                content=ft.Row(
                    controls=[
                        ft.ListTile(
                            title=t,
                        ), 
                    ],
                ),
                width=400,
                height=50,
                surface_tint_color=None,
            )
        
        page.controls.append( card )
    page.update()