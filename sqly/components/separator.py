import reflex as rx
from sqly.states.state_separator import Separator


def separator() -> rx.Component:
    return rx.box(
        rx.heading(
            "Separator",
            as_="h3",
            class_name="text-3xl font-medium mb-2 mt-1 text-primary p-2"
        ),
        rx.divider(),
        rx.box(
            rx.form(
                rx.box(
                    rx.text_area(
                        id="prompt_text",
                        placeholder="Enter a prompt...",
                        class_name="resize-none rounded-[7px] border p-10 font-sans text-sm font-normal outline outline-0",
                        height="250px"
                    ),
                    class_name="relative w-full"
                ),
                rx.box(
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
                        id="actions",
                        class_name="h-full w-full rounded-[7px]"
                    ),
                    class_name="relative"
                ),
                rx.hstack(
                    rx.spacer(),
                    rx.button(
                        "Go",
                        type_="submit"
                    )
                ),
                rx.box(
                    rx.cond(
                        Separator.is_processing,
                        rx.circular_progress(is_indeterminate=True),
                        rx.cond(
                            Separator.is_finished,
                            rx.text_area(
                                value=Separator.promt_results,
                                class_name="resize-none rounded-[7px] border p-10 font-sans text-sm font-normal outline outline-0",
                                height="150px",
                                is_read_only=True
                            )
                        )
                    ),
                ),
                class_name="p-2",
                on_submit=Separator.get_results,
                m="10px"
            ),
        )
    )