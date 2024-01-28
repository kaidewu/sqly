import reflex as rx
from sqly.states.state_data_generator import DataGenerator


def identification_generator() -> rx.Component:
    return rx.box(
        rx.heading(
            "Identification Generator",
            as_="h3",
            class_name="text-3xl font-medium mb-2 mt-1 text-primary p-2"
        ),
        rx.divider(),
        rx.box(
            rx.input_group(
                rx.cond(
                    DataGenerator.is_processing,
                    rx.circular_progress(is_indeterminate=True),
                    rx.cond(
                        DataGenerator.is_finished,
                        rx.input(
                            value=DataGenerator.dni_number["dni"],
                            is_read_only=True
                        )
                    )
                ),
                m="10px",
                on_mount=DataGenerator.identification_generator
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    "Generate",
                    on_click=DataGenerator.identification_generator
                )
            ),
        ),
        class_name="mr-5"
    )