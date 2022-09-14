from shopper import Shopper


class Storefront:

    @classmethod
    def create_storefront(cls):
        return cls(
            shopper=Shopper.create_buyer(),
            stock={
                "apples": 200,
                "bananas": 200,
                "lemons": 200,
                "oranges": 200,
                "peaches": 200,
                "potatoes": 200,
            },
            profit=0
        )

    __shopper: Shopper
    __stock: dict
    __record: dict
    __profit: float
    __stock: dict

    PRICES: dict[str, float] = {
        "apples": 1.75,
        "bananas": 1.85,
        "lemons": 1.80,
        "oranges": 1.70,
        "peaches": 2.65,
        "potatoes": .50,
    }

    stock = {
        "apples": 200,
        "bananas": 200,
        "lemons": 200,
        "oranges": 200,
        "peaches": 200,
        "potatoes": 200,
    }

    def __init__(self, shopper: Shopper, stock: dict, profit: float) -> None:

        self.__shopper = shopper
        self.__stock = stock
        self.__profit = profit

    def add_stock(self, item_name: str, amount: int) -> None:
        for key in self.__stock.keys():
            if key == item_name.lower():
                self.__stock[item_name] += int(amount)
                self.__profit -= (self.PRICES[item_name.lower()] * float(amount) / 3)

    def sell(self, item_name: str, amount: float) -> None:
        price = self.PRICES[item_name.lower()] * float(amount)
        self.__stock[item_name.lower()] -= float(amount)
        self.__profit += price
        self.__shopper.purchase(price)

    def add_shopper_balance(self, amount: float) -> None:
        self.__shopper.add_balance(amount)

    def get_profit(self) -> float:
        return self.__profit

    def check_stock_for(self, item_name: str) -> int:
        return self.__stock[item_name]

    def get_available_items(self) -> str:
        available_items = "Currently available:"
        for key in self.__stock.keys():
            if self.__stock[key] > 0:
                available_items += f"\n- {key}"
        return available_items

    def get_prices(self) -> str:
        prices = "Current Prices:"
        for key, item in self.PRICES.items():
            prices += "\n- " + str(key) + ": " + str(item) + " €/Kg"
        return prices

    def get_shopper_balance(self) -> float:
        return self.__shopper.get_balance()

    def get_shopper_expenses(self) -> float:
        return self.__shopper.get_expenses()

    def sells_this(self, item_name) -> bool:
        return item_name in self.PRICES.keys()

    def has_item(self, item_name: str) -> bool:
        for key in self.__stock.keys():
            if key == item_name and self.__stock[key] > 0:
                return True
        return False

    def can_sell(self, item_name: str, amount: float) -> bool:
        return self.__shopper.get_balance() >= self.PRICES[item_name] * float(amount)
