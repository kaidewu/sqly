import reflex as rx
import time
from typing import List
from random import randrange

class DataGenerator(rx.State):
    """ Data Generator like names, surnames, identification numbers, phone numbers, ... """
    is_finished: bool = False
    is_processing: bool = False
    
    def get_identification_number(self, start: int, end: int) -> int:
        """
        Get identification number
        :params = start: int, end: int
        :description = Get random numbers for identification
        """
        return randrange(start, end)
    
    def identification_generator(self):
        """
        Identification Generator
        :params = None
        :description = Generate identification numbers for examples
        """
        start_time: float = time.perf_counter()
        equivalency_list: List[str] = ["T", "R", "W", "A", "G", "M", "Y", 
                                       "F", "P", "D", "X", "B", "N", "J", 
                                       "Z", "S", "Q", "V", "H", "L", "C", 
                                       "K", "E"]
        dni_numbers: int = self.get_identification_number(0, 99_999_999)
        remainder: int = dni_numbers % 23
        self.is_processing = True
        self.is_finished = False
        try:
            while 0 < remainder > 22:
                dni_numbers = self.get_identification_number(0, 99_999_999)
                remainder = dni_numbers % 23
            print(time.perf_counter() - start_time)
            return f"{dni_numbers}{equivalency_list[remainder]}"
        except Exception as err:
            self.is_finished = True
            return f"Error in the processing: {err}"