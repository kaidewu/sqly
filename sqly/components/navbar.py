import reflex as rx

def navbar() -> rx.Component:
    return(
        rx.box(
            rx.box(
                rx.color_mode_button(
                    rx.color_mode_icon(),
                ),
                style={
                    "display": "inline-block",
                }
            ),
            display="flex",
            wrap="wrap",
            align="center",
            justify="space-between"
        )
    )
