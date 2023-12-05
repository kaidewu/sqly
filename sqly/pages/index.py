import reflex as rx
from sqly.components.layout.main import main

def index() -> rx.Component:
    return(
        main(
            rx.vstack(
                rx.hstack(
                    rx.heading("Home", size="md"),
                    rx.spacer(),
                    width="100%",
                    mt="3em"
                ),
                rx.divider(),
                rx.responsive_grid(
                    rx.link_box(
                        rx.box(
                            rx.stat(
                                rx.stat_label("Separator")
                            ),
                            border="1px solid #eaeaef",
                            padding="1rem",
                            border_radius=8,
                        ),
                        href="/separtor"
                    ),
                    columns=["5"],
                    margin_bottom="1rem",
                ),
                width="100%",
            )
        )    
    )