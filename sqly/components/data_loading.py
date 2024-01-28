import reflex as rx
from sqly.states.state_data_loading import DataLoading


def data_loading() -> rx.Component:
    return rx.box(
        rx.heading(
            "Data Loading",
            as_="h3",
            class_name="text-3xl font-medium mb-2 mt-1 text-primary p-2"
        ),
        rx.divider(),
        rx.form(
            rx.box(
                rx.text("Query"),
                rx.text_area(
                    id="query",
                    placeholder="Enter the query. It's required",
                    class_name="resize-none rounded-[7px] border p-10 font-sans text-sm font-normal outline outline-0",
                    height="250px"
                ),
                class_name="relative w-full"
            ),
            rx.box(
                rx.text("Audi Query"),
                rx.text_area(
                    id="audi_query",
                    placeholder="Enter the audi query. Can be empty",
                    class_name="resize-none rounded-[7px] border p-10 font-sans text-sm font-normal outline outline-0",
                    height="250px"
                ),
                class_name="relative w-full"
            ),
            rx.box(
                rx.upload(
                    rx.vstack(
                        rx.button("Select File", color="rgb(107,99,246)", bg="white", border="1px solid rgb(107,99,246)"),
                        rx.text("Drag and drop the Excel here or click to select"),
                    ),
                    multiple=False,
                    max_files=1,
                    border="1px dotted",
                    padding="2.5em",
                    pt="5"
                ),
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    "Generate",
                    type_="submit",
                    on_click=lambda: DataLoading.handle_upload(rx.upload_files())
                )
            ),
            rx.box(
                rx.cond(
                    DataLoading.is_processing,
                    rx.circular_progress(is_indeterminate=True),
                    rx.cond(
                        DataLoading.is_finished,
                        rx.text_area(
                            value=DataLoading.results_query,
                            class_name="resize-none rounded-[7px] border p-10 font-sans text-sm font-normal outline outline-0",
                            height="150px",
                            is_read_only=True
                        )
                    )
                ),
            ),
            on_submit=DataLoading.trigger_data_loading
        ),
        class_name="mr-5"
    )