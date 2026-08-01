from abc import ABC, abstractmethod


class Transaction(ABC):

    def __init__(self, trans_id, amount, category):
        self._trans_id = trans_id
        self._amount = amount
        self._category = category

    @abstractmethod
    def display(self):
        pass