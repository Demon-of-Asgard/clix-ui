import flet as ft

def main(page: ft.Page):
    page.title = "Change Icon on Click Example"

    # Initial icon state
    current_icon = ft.icons.PLAY_CIRCLE_FILL_OUTLINED

    # Function to handle button click
    def toggle_icon(e):
        nonlocal current_icon
        # Toggle between two icons
        if current_icon == ft.icons.PLAY_CIRCLE_FILL_OUTLINED:
            current_icon = ft.icons.STOP_OUTLINED
        else:
            current_icon = ft.icons.PLAY_CIRCLE_FILL_OUTLINED
        
        # Update the icon in the button
        icon_button.icon = current_icon
        page.update()  # Update the page to reflect changes

    # Create the IconButton with an initial icon
    icon_button = ft.IconButton(
        icon=current_icon,
        on_click=toggle_icon,
        tooltip="Click to change icon"
    )
    card = ft.Card(
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.ListTile(
                        # title=ft.Text("HI"),
                        trailing=icon_button,
                    ),
                ]
            ),
            width=page.width,
            height=50,
            padding=0,
        )
    )

    # Add the button to the page
    page.add(ft.Row(controls=[card]))

# Run the app
ft.app(main)