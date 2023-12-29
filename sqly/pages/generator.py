import reflex as rx

from sqly.states.state_data_generator import DataGenerator
from sqly.components.layout.main import main

def generator() -> rx.Component:
    return(
        main(
            rx.vstack(
                rx.text_area(
                    value=DataGenerator().identification_generator(),
                    is_read_only=True
                )
            )
        )
    )