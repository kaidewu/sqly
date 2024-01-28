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
        rx.box(
            rx.upload(
                rx.vstack(
                    rx.button("Select File", color="rgb(107,99,246)", bg="white", border="1px solid rgb(107,99,246)"),
                    rx.text("Drag and drop files here or click to select files"),
                ),
                multiple=False,
                max_files=1,
                border="1px dotted",
                padding="2.5em",
                pd="5"
            ),
            rx.hstack(
                rx.spacer(),
                rx.button(
                    "Generate",
                    on_click=lambda: DataLoading.handle_upload(rx.upload_files()),
                )
            ),
            rx.foreach(DataLoading.excel_path, lambda path: rx.text(path)),
        ),
        class_name="mr-5"
    )