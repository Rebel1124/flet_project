import flet as ft
from custom_checkbox import CustomCheckBox


def main(page: ft.Page):
    # --------------------------------------------------
    # COLORS
    # --------------------------------------------------

    BG = "#071F5B"
    FG = "#4667B1"
    PINK = "#F000E8"
    LIGHT_BLUE = "#AFC4FF"
    WHITE = "#FFFFFF"
    PAGE_BG = "#F4F6FB"

    # --------------------------------------------------
    # PAGE SETTINGS
    # --------------------------------------------------

    page.title = "Flet Task App"
    page.bgcolor = PAGE_BG
    page.padding = 0

    # --------------------------------------------------
    # PROFILE CIRCLE
    # --------------------------------------------------

    circle = ft.Stack(
        controls=[
            ft.Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor=ft.Colors.WHITE_12,
            ),
            ft.Container(
                gradient=ft.SweepGradient(
                    center=ft.Alignment.CENTER,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=[
                        "#00000000",
                        PINK,
                    ],
                ),
                width=100,
                height=100,
                border_radius=50,
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            padding=ft.Padding.all(5),
                            bgcolor=BG,
                            width=90,
                            height=90,
                            border_radius=50,
                            content=ft.Container(
                                bgcolor=FG,
                                height=80,
                                width=80,
                                border_radius=40,
                                content=ft.CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_src=(
                                        "https://images.unsplash.com/"
                                        "photo-1545912452-8aea7e25a3d3"
                                        "?auto=format&fit=crop&w=687&q=80"
                                    ),
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        ]
    )

    # --------------------------------------------------
    # OPEN / CLOSE SIDE MENU
    # --------------------------------------------------

    def shrink(e):
        page_2.controls[0].width = 120

        page_2.controls[0].scale = ft.Scale(
            scale=0.8,
            alignment=ft.Alignment.CENTER_RIGHT,
        )

        page_2.controls[0].border_radius = ft.BorderRadius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0,
        )

        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400

        page_2.controls[0].border_radius = 35

        page_2.controls[0].scale = ft.Scale(
            scale=1,
            alignment=ft.Alignment.CENTER_RIGHT,
        )

        page_2.update()

    # --------------------------------------------------
    # CREATE TASK VIEW
    # --------------------------------------------------

    create_task_view = ft.Container(
        expand=True,
        bgcolor=FG,
        padding=30,
        content=ft.Column(
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            "Create Task",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                            color=WHITE,
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=WHITE,
                            on_click=lambda _: page.navigate("/"),
                        ),
                    ],
                ),
                ft.Container(height=20),
                ft.TextField(
                    label="Task name",
                    hint_text="Enter a task",
                ),
                ft.TextField(
                    label="Description",
                    hint_text="Enter a description",
                    multiline=True,
                    min_lines=3,
                    max_lines=5,
                ),
            ]
        ),
    )

    # --------------------------------------------------
    # TASK LIST
    # --------------------------------------------------

    tasks = ft.Column(
        height=390,
        spacing=12,
        scroll=ft.ScrollMode.AUTO,
    )

    for _ in range(10):
        tasks.controls.append(
            ft.Container(
                height=68,
                width=360,
                bgcolor=BG,
                border_radius=22,
                padding=ft.Padding.symmetric(
                    horizontal=20,
                    vertical=16,
                ),
                content=CustomCheckBox(
                    color=PINK,
                    label="Create interesting content!",
                    font_size=16,
                    selection_fill=PINK,
                ),
            )
        )

    # --------------------------------------------------
    # CATEGORY CARDS
    # --------------------------------------------------

    categories_card = ft.Row(
        spacing=10,
        wrap=True,
    )

    categories = [
        "Business",
        "Family",
        "Friends",
    ]

    progress_values = [
        (100, 0),
        (78, 22),
        (55, 45),
    ]

    for i, category in enumerate(categories):
        filled, remaining = progress_values[i]

        categories_card.controls.append(
            ft.Container(
                width=170,
                height=105,
                border_radius=20,
                bgcolor=BG,
                padding=16,
                content=ft.Column(
                    spacing=8,
                    controls=[
                        ft.Text(
                            "40 Tasks",
                            color=LIGHT_BLUE,
                            size=14,
                        ),
                        ft.Text(
                            category,
                            size=17,
                            weight=ft.FontWeight.W_600,
                            color=WHITE,
                        ),
                        ft.Container(
                            height=5,
                            bgcolor="#29447E",
                            border_radius=20,
                            content=ft.Row(
                                spacing=0,
                                controls=[
                                    ft.Container(
                                        expand=filled,
                                        height=5,
                                        bgcolor=PINK,
                                        border_radius=20,
                                    ),
                                    ft.Container(
                                        expand=remaining,
                                        height=5,
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            )
        )

    # --------------------------------------------------
    # MAIN PAGE CONTENT
    # --------------------------------------------------

    first_page_contents = ft.Container(
        content=ft.Column(
            spacing=0,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.MENU,
                            icon_color=WHITE,
                            icon_size=28,
                            on_click=shrink,
                        ),
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.SEARCH,
                                    icon_color=WHITE,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.NOTIFICATIONS_OUTLINED,
                                    icon_color=WHITE,
                                ),
                            ],
                        ),
                    ],
                ),
                ft.Container(height=24),
                ft.Text(
                    "What's up, Olivia!",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=WHITE,
                ),
                ft.Container(height=22),
                ft.Text(
                    "CATEGORIES",
                    color=LIGHT_BLUE,
                    size=13,
                    weight=ft.FontWeight.W_600,
                ),
                ft.Container(height=12),
                categories_card,
                ft.Container(height=30),
                ft.Text(
                    "TODAY'S TASKS",
                    color=LIGHT_BLUE,
                    size=13,
                    weight=ft.FontWeight.W_600,
                ),
                ft.Container(height=14),
                ft.Stack(
                    controls=[
                        tasks,
                        ft.FloatingActionButton(
                            bottom=10,
                            right=10,
                            icon=ft.Icons.ADD,
                            bgcolor=PINK,
                            foreground_color=WHITE,
                            elevation=6,
                            on_click=lambda _: page.navigate("/create_task"),
                        ),
                    ]
                ),
            ],
        ),
    )

    # --------------------------------------------------
    # SIDE MENU
    # --------------------------------------------------

    page_1 = ft.Container(
        bgcolor=BG,
        border_radius=35,
        padding=ft.Padding.only(
            left=45,
            top=45,
            right=135,
        ),
        content=ft.Column(
            spacing=12,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK_IOS_NEW,
                            icon_color=WHITE,
                            on_click=restore,
                        )
                    ],
                ),
                ft.Container(height=10),
                circle,
                ft.Text(
                    "Olivia\nMitchel",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=WHITE,
                ),
                ft.Container(height=12),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.FAVORITE_BORDER_SHARP,
                            color=LIGHT_BLUE,
                        ),
                        ft.Text(
                            "Templates",
                            size=15,
                            color=WHITE,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.CARD_TRAVEL,
                            color=LIGHT_BLUE,
                        ),
                        ft.Text(
                            "Projects",
                            size=15,
                            color=WHITE,
                        ),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.CALCULATE_OUTLINED,
                            color=LIGHT_BLUE,
                        ),
                        ft.Text(
                            "Analytics",
                            size=15,
                            color=WHITE,
                        ),
                    ]
                ),
                ft.Container(height=15),
                ft.Image(
                    src="images/1.png",
                    width=220,
                    height=150,
                ),
                ft.Text(
                    "Good",
                    color=LIGHT_BLUE,
                    size=14,
                ),
                ft.Text(
                    "Consistency",
                    size=20,
                    color=WHITE,
                    weight=ft.FontWeight.W_600,
                ),
            ],
        ),
    )

    # --------------------------------------------------
    # FRONT PANEL
    # --------------------------------------------------

    page_2 = ft.Row(
        alignment=ft.MainAxisAlignment.END,
        controls=[
            ft.Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                animate=ft.Animation(
                    duration=600,
                    curve=ft.AnimationCurve.DECELERATE,
                ),
                animate_scale=ft.Animation(
                    duration=400,
                    curve=ft.AnimationCurve.DECELERATE,
                ),
                padding=ft.Padding.only(
                    top=38,
                    left=20,
                    right=20,
                    bottom=16,
                ),
                content=ft.Column(
                    controls=[
                        first_page_contents,
                    ]
                ),
            )
        ],
    )

    # --------------------------------------------------
    # APP SHELL
    # --------------------------------------------------

    container = ft.Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=ft.Stack(
            controls=[
                page_1,
                page_2,
            ]
        ),
    )

    # --------------------------------------------------
    # ROUTING
    # --------------------------------------------------

    def route_change(e=None):
        page.views.clear()

        page.views.append(
            ft.View(
                route="/",
                controls=[container],
                padding=0,
                bgcolor=PAGE_BG,
            )
        )

        if page.route == "/create_task":
            page.views.append(
                ft.View(
                    route="/create_task",
                    controls=[create_task_view],
                    padding=0,
                )
            )

        page.update()

    page.on_route_change = route_change

    route_change()


if __name__ == "__main__":
    ft.run(
        main,
        assets_dir="assets",
    )
