from typing import List, Any

from service.impl.IRSystem import IRSystem
import os
from model.response import Response


# read, organize the data, then another function should search an organized piece of data
# Controller should get called after UI finishes building to pre-process the data
class Controller1:
    """
    Controller stores business logic between Word
    and the Kivy Interface
    """

    def __init__(self) -> None:
        self.irsystem = IRSystem()
        """
        Special method that replaces a constructor/__new()__
        """

    def process_files(self):
        """
        Pre Process a list of files using the IRSystem
        :return: None
        """
        arr = os.listdir('data/')
        self.irsystem.build_system(arr)

    def retrieve_data(self, word: str) -> str:
        """
        Given word from input, returns available data to user
        :return:
        """
        query = list(self.irsystem.query_search(word))
        freq = self.irsystem.word_frequency(word)
        response = Response(query, freq, word)
        print("RESPONSE:", response)
        return response.toJSON()

