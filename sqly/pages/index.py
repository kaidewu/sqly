import reflex as rx
from sqly.components.layout.main import main
from sqly.components.separator import separator
from sqly.components.identification_generator import identification_generator
from sqly.components.data_loading import data_loading


def index() -> rx.Component:
    return main(
        rx.box(
            separator(),
            rx.box(
                identification_generator(),
                data_loading(),
            ),
            class_name="grid gap-4 grid-cols-2"
        )
    )
