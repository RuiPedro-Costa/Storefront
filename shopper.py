class Shopper:

    @classmethod
    def create_buyer(cls):
        return cls(balance=0, expenses=0)

    __balance: float
    __expenses: float

    def __init__(self, balance: float, expenses: float) -> None:
        self.__balance = balance
        self.__expenses = expenses

    def add_balance(self, amount: float) -> None:
        self.__balance += float(amount)

    def purchase(self, amount: float) -> None:
        self.__balance -= float(amount)
        self.__expenses += float(amount)

    def get_balance(self) -> float:
        return self.__balance

    def get_expenses(self) -> float:
        return self.__expenses
