import reflex as rx

from sqly.components.navbar import navbar

def main(*args) -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            *args
        )
    )