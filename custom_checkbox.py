import flet as ft


class CustomCheckBox(ft.Row):
    def __init__(
        self,
        color,
        label="",
        selection_fill="#183588",
        size=25,
        stroke_width=2,
        animation=None,
        checked=False,
        font_size=16,
        pressed=None,
    ):
        super().__init__()

        self.selection_fill = selection_fill
        self.checkbox_color = color
        self.label = label
        self.checkbox_size = size
        self.stroke_width = stroke_width
        self.checkbox_animation = animation
        self.checked = checked
        self.font_size = font_size
        self.pressed = pressed

        self.spacing = 12
        self.vertical_alignment = ft.CrossAxisAlignment.CENTER

        self.check_box = ft.Container(
            animate=self.checkbox_animation,
            width=self.checkbox_size,
            height=self.checkbox_size,
            border_radius=self.checkbox_size / 2,
        )

        self.label_text = ft.Text(
            value=self.label,
            size=self.font_size,
            weight=ft.FontWeight.W_400,
            color=ft.Colors.WHITE,
        )

        self.checkbox_container = ft.Container(
            on_click=self.checked_check,
            content=ft.Row(
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.check_box,
                    self.label_text,
                ],
            ),
        )

        self.controls = [self.checkbox_container]

        self._update_checkbox()

    def _update_checkbox(self):
        if self.checked:
            self.check_box.bgcolor = self.selection_fill
            self.check_box.border = None
            self.check_box.content = ft.Icon(
                ft.Icons.CHECK_ROUNDED,
                size=16,
                color=ft.Colors.WHITE,
            )
        else:
            self.check_box.bgcolor = None
            self.check_box.border = ft.Border.all(
                width=self.stroke_width,
                color=self.checkbox_color,
            )
            self.check_box.content = None

    def checked_check(self, e):
        self.checked = not self.checked

        self._update_checkbox()
        self.update()

        if self.pressed:
            self.pressed(self.checked)

    def is_checked(self):
        return self.checked
