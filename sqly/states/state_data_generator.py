import reflex as rx
from typing import List, Dict
from random import randrange

class DataGenerator(rx.State):
    """ Data Generator like names, surnames, identification numbers, phone numbers, ... """
    
    def get_identification_number(self, start: int, end: int) -> int:
        """
        Get identification number
        :params = start: int, end: int
        :description = Get random numbers for identification
        """
        return randrange(start, end)
    
    def identification_generator(self) -> Dict[str, str]:
        """
        Identification Generator
        :params = None
        :description = Generate identification numbers for examples
        """
        equivalency_list: List[str] = ["T", "R", "W", "A", "G", "M", "Y", 
                                       "F", "P", "D", "X", "B", "N", "J", 
                                       "Z", "S", "Q", "V", "H", "L", "C", 
                                       "K", "E"]
        dni_numbers: int = self.get_identification_number(0, 99_999_999)
        remainder: int = dni_numbers % 23
        try:
            while 0 < remainder > 22:
                dni_numbers = self.get_identification_number(0, 99_999_999)
                remainder = dni_numbers % 23
            return {
                "dni": f"{dni_numbers}{equivalency_list[remainder]}",
                "passport": "Comming soon..."
            }
        except Exception as err:
            return rx.window_alert(f"Error in the processing: {err}")