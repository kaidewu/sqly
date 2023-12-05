import reflex as rx
from typing import Dict, List

class Separator(rx.State):
    """ Separator page state. """
    results: str = ""
    results_processing: bool = False
    results_finish: bool = False

    def get_results(self, form_data: Dict[str, str]) -> str:
        """
        :params form_data: Dict[str, str]
        :description Tranform into a list depends on the actions it's given
        """
        promt_text: List[str] = form_data["prompt_text"].splitlines()
        actions: str = form_data["actions"]
        temp_var: list = []
        self.results_finish = False
        self.results_processing = True
        yield
        try:
            if actions == "simple_commas":
                for text in promt_text:
                    temp_var.append(f"'{text}'")
                self.results = ", ".join(text for text in temp_var)
            elif actions == "double_commas":
                for text in promt_text:
                    temp_var.append(f"\"{text}\"")
                self.results = ", ".join(text for text in temp_var)
            elif actions == "none":
                self.results = ", ".join(text for text in promt_text)
            else:
                raise Exception("Internal Error!")
            self.results_processing = False
            self.results_finish = True
        except Exception as err:
            print(err)
            self.results_processing = False
            yield rx.window_alert(f"Error in the processing: {err}")