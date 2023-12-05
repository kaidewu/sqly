import reflex as rx
from sqly.components.layout.main import main
from sqly.states.state_separator import Separator

def separator() -> rx.Component:
    return(
        main(
            rx.vstack(
                rx.hstack(
                    rx.heading("Separator", size="md"),
                    rx.spacer(),
                    width="100%",
                    mt="10px"
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
                    rx.hstack(rx.spacer(), rx.button("Go", type_="submit")),
                    on_submit=Separator.get_results,
                    width="100%"
                ),
                rx.divider(),
                rx.cond(
                    Separator.results_processing,
                    rx.circular_progress(is_indeterminate=True),
                    rx.cond(
                        Separator.results_finish,
                        rx.text_area(
                            value=Separator.results,
                            is_read_only=True
                        )
                    )
                ),
                width="100%",
            )
        )    
    )