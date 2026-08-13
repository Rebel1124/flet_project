import flet as ft


def main(page: ft.Page):

    # --------------------------------------------------
    # PAGE SETTINGS
    # --------------------------------------------------

    # Title shown in the browser tab
    page.title = "Flet Counter App"

    # Light theme
    page.theme_mode = ft.ThemeMode.LIGHT

    # Center the page content
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --------------------------------------------------
    # APP BAR
    # --------------------------------------------------

    page.appbar = ft.AppBar(
        title=ft.Text("Flet Demo Home Page", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE,
        center_title=True,
    )

    # --------------------------------------------------
    # COUNTER TEXT
    # --------------------------------------------------

    # Displays the current counter value
    counter_text = ft.Text(value="0", size=40, weight=ft.FontWeight.BOLD)

    # --------------------------------------------------
    # COUNTER FUNCTION
    # --------------------------------------------------

    def increment_counter(e):
        """
        Increase the counter by 1 every time
        the floating action button is clicked.
        """

        counter_text.value = str(int(counter_text.value) + 1)

        # Refresh the UI
        page.update()

    # --------------------------------------------------
    # FLOATING ACTION BUTTON
    # --------------------------------------------------

    page.floating_action_button = ft.FloatingActionButton(
        content=ft.Icon(ft.Icons.ADD, color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE,
        shape=ft.CircleBorder(),
        on_click=increment_counter,
        tooltip="Increment",
    )

    # --------------------------------------------------
    # ADD CONTROLS TO PAGE
    # --------------------------------------------------

    page.add(ft.Text("You have pushed the button this many times:"), counter_text)


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

# Run Flet application in the web browser
ft.run(main, view=ft.AppView.WEB_BROWSER)
