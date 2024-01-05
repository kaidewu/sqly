import reflex as rx
from typing import List, Dict
from random import randrange
import math

class DataGenerator(rx.State):
    """ Data Generator like names, surnames, identification numbers, phone numbers, ... """
    dni_number: str = ""
    equivalency_list: List[str] = ["T", "R", "W", "A", "G", "M", "Y", 
                                    "F", "P", "D", "X", "B", "N", "J", 
                                    "Z", "S", "Q", "V", "H", "L", "C", 
                                    "K", "E"]
    is_processing = False
    is_finished = False
    
    def get_identification(self) -> Dict[str, str]:
        """
        Get Identification
        :params = None
        :description = Get identification numbers
        """
        try:
            while True:
                dni_numbers = randrange(0, 99_999_999)
                remainder = dni_numbers % 23
                if (0 < remainder < 23) and (int(math.log10(dni_numbers)) + 1) == 8:
                    break
            return {
                "dni": f"{dni_numbers}{self.equivalency_list[remainder]}",
                "passport": "Comming soon..."
            }
        except Exception as err:
            return rx.window_alert(f"Error in the processing: {err}")

    def identification_generator(self):
        """
        Identification Generator
        :params = None
        :description = Generate identification numbers for examples
        """
        yield
        try:
            self.is_processing = True
            while True:
                dni_numbers = randrange(0, 99_999_999)
                remainder = dni_numbers % 23
                if (0 < remainder < 23) and (int(math.log10(dni_numbers)) + 1) == 8:
                    break
            self.dni_number = f"{dni_numbers}{self.equivalency_list[remainder]}"
        except Exception as err:
            self.is_processing = False
            yield rx.window_alert(f"Error in the processing: {err}")
        finally:
            self.is_processing = False
            self.is_finished = True