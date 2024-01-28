from os import path, remove
from typing import List

import reflex as rx


class DataLoading(rx.State):
    excel_path: List[str]

    def _check_if_exists_file(self, file_path: str) -> None:
        if path.exists(file_path):
            remove(file_path)
            print(f"Remove: {file_path}")

    async def handle_upload(self, files: List[rx.UploadFile]):
        for file in files:
            upload_data = await file.read()
            outline = rx.get_asset_path(file.filename)
            self._check_if_exists_file(outline)
            with open(outline, "wb") as file_object:
                file_object.write(upload_data)

            self.excel_path.append(file.filename)
