import reflex as rx

from sqly.components.navbar import navbar

def main(*args) -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            *args
        ),
        class_name="w-full xl:w-8/11 px-4 mx-auto"
    )