from transaction import Transaction


class Expense(Transaction):

    def __init__(self, trans_id, trans_type, amount, category):
        super().__init__(trans_id, amount, category)
        self.__trans_type = trans_type

    # Getter
    def get_transaction_type(self):
        return self.__trans_type

    # Setter
    def set_transaction_type(self, trans_type):
        self.__trans_type = trans_type

    def display(self):

        print("\n" + "=" * 60)
        print("              TRANSACTION DETAILS")
        print("=" * 60)
        print(f"Transaction ID : {self._trans_id}")
        print(f"Type           : {self.__trans_type}")
        print(f"Amount         : ₹{self._amount:.2f}")
        print(f"Category       : {self._category}")
        print("=" * 60)