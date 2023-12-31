import reflex as rx
from sqly.components.layout.main import main
from sqly.states.state_separator import Separator
from sqly.states.state_data_generator import DataGenerator

def index() -> rx.Component:
    return(
        main(
            rx.flex(
                rx.box(
                    rx.hstack(
                        rx.heading("Separator", size="md"),
                        rx.spacer(),
                        width="100%",
                        m="10px"
                    ),
                    rx.divider(),
                    rx.form(
                        rx.box(
                            rx.text_area(
                                id="prompt_text", 
                                placeholder="Enter a prompt...",
                                height="4em"
                            ),
                            rx.select(
                                rx.option(
                                    " ",
                                    value="none"
                                ),
                                rx.option(
                                    " '' ",
                                    value="simple_commas"
                                ),
                                rx.option(
                                    " \"\" ",
                                    value="double_commas",
                                ),
                                id="actions"
                            ),
                        ),
                        rx.hstack(
                            rx.spacer(), 
                            rx.button(
                                "Go", 
                                type_="submit"
                            ),
                            m="5px"
                        ),
                        on_submit=Separator.get_results,
                        width="100%",
                        m="10px"
                    ),
                    rx.cond(
                        Separator.is_processing,
                        rx.circular_progress(is_indeterminate=True),
                        rx.cond(
                            Separator.is_finished,
                            rx.text_area(
                                value=Separator.promt_results,
                                is_read_only=True
                            )
                        )
                    )
                ),
                rx.spacer(),
                rx.box(
                    rx.hstack(
                        rx.heading("Generator", size="md"),
                        rx.spacer(),
                        width="100%",
                        m="10px"
                    ),
                    rx.divider(),
                    rx.box(
                        rx.input_group(
                            rx.input(
                                value=DataGenerator().identification_generator()["dni"],
                                is_read_only=True
                            ),
                            m="10px"
                        ),
                        rx.hstack(
                            rx.spacer(), 
                            rx.button(
                                "Generate"
                            ),
                            m="5px"
                        ),
                    )
                ),
                min_width="max-content",
                gap="2"
            )
        )    
    )