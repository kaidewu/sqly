from os import path, remove
from typing import List, Dict

import pandas
import reflex as rx


class DataLoading(rx.State):
    excel_path: str = ""
    results_query: str = ""
    query: str = ""
    audi_query: str = ""
    transaction: bool = False
    
    is_processing: bool = False
    is_finished: bool = False

    def _check_if_exists_file(self, file_path: str) -> None:
        """_summary_

        Args:
            file_path (str): _description_
        """
        if path.exists(file_path):
            remove(file_path)
            print(f"Remove: {file_path}")
            
    async def handle_upload(self, files: List[rx.UploadFile]) -> None:
        """_summary_

        Args:
            files (List[rx.UploadFile]): _description_
        """
        for file in files:
            upload_data = await file.read()
            
            self.excel_path = rx.get_asset_path(file.filename)
            
            # Check if exists the file
            self._check_if_exists_file(self.excel_path)
            
            with open(self.excel_path, "wb") as file_object:
                file_object.write(upload_data)
                
    def _read_excel_dataframe(self):
        """
        Get DateFrame of Excel file with Pandas
        :return: DateFrame
        """
        return pandas.read_excel(self.excel_path)
    
    def _get_columns_names(self):
        """
        Get the columns names
        :return: I guess Index. Better go to the Pandas documents to read it
        """
        return self._read_excel_dataframe().columns
    
    def _list_content(self) -> List[List[str]]:
        """
        List content of each row of Excel file
        :return: List[List[str]]
        """
        return [row.tolist() for index, row in self._read_excel_dataframe().iterrows()]

    def _list_duplicate_query(self) -> List[List[str]]:
        """
        List duplicate content of each row of Excel file
        :return: List[List[str]]
        """
        return [query*2 for query in self._list_content()]
    
    def _results_query(self) -> List[str]:
        """
        Return list of SQL Query
        :return: List[str]
        """
        return [self.query % tuple(query) for query in self._list_content()]
    
    def _results_audi_query(self) -> List[str]:
        """
        List of AUDITORY query
        :return: List[str]
        """
        return [self.audi_query % tuple(audi_query) for audi_query in self._list_audi_query()]
    
    def _str_query_construction(
        self, 
        query: str,
        audi_query: str
    ) -> str:
        if self.transaction:
            return f"BEGIN TRANSACTION\n"\
               f"{query}\n"\
               f"{audi_query}\n"\
               f"ROLLBACK"
        return f"BEGIN TRANSACTION\n"\
               f"{query}\n"\
               f"{audi_query}\n"\
               f"COMMIT"
    
    def trigger_data_loading(
        self, 
        form_data: Dict[str, str]
    ) -> None:
        self.is_processing: bool = True
        self.query = form_data["query"]
        self.audi_query = form_data["audi_query"]
        
        for query, audi_query in zip(self._results_query, self._results_audi_query):
            self.results_query += self._str_query_construction(query, audi_query)
        
        print(self.results_query)    
        