import reflex as rx
from typing import List, Dict
from random import randrange
import math
import traceback


class DataGenerator(rx.State):
    """ Data Generator like names, surnames, identification numbers, phone numbers, ... """
    dni_number: Dict[str, str] = {
        "dni": "",
        "passport": ""
    }
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
        except:
            raise Exception(traceback.format_exc())

    def identification_generator(self):
        """
        Identification Generator
        :params = None
        :description = Generate identification numbers for examples
        """
        try:
            self.is_processing = True
            while True:
                dni_numbers = randrange(0, 99_999_999)
                remainder = dni_numbers % 23
                if (0 < remainder < 23) and (int(math.log10(dni_numbers)) + 1) == 8:
                    break
            self.dni_number["dni"] = f"{dni_numbers}{self.equivalency_list[remainder]}"
        except:
            self.is_processing = False
            raise Exception(traceback.format_exc())
        finally:
            self.is_processing = False
            self.is_finished = True
