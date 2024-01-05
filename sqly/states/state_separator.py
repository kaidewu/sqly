import reflex as rx
from typing import Dict, List

class Separator(rx.State):
    """ Separator page state. """
    promt_results: str = ""
    is_processing = False
    is_finished = False

    def get_results(self, form_data: Dict[str, str]):
        """
        Get results
        :params = form_data: Dict[str, str]
        :description = Tranform into a list depends on the actions it's given
        """
        if form_data["prompt_text"] is not None:
            promt_text: List[str] = form_data["prompt_text"].splitlines()
        else:
            promt_text = ""
        actions: str = form_data["actions"]
        self.is_finished = False
        self.is_processing = True
        yield
        try:
            if actions == "simple_commas":
                self.promt_results = ", ".join(f"'{text}'" for text in promt_text)
            elif actions == "double_commas":
                self.promt_results = ", ".join(f"\"{text}\"" for text in promt_text)
            elif actions == "none":
                self.promt_results = ", ".join(f"{text}" for text in promt_text)
            else:
                raise Exception("Internal Error!")
        except Exception as err:
            self.is_processing = False
            yield rx.window_alert(f"Error in the processing: {err}")
        finally:
            self.is_processing = False
            self.is_finished = True
