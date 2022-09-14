from storefront import Storefront
import DOCS

if __name__ == '__main__':

    command = ''
    storefront = Storefront.create_storefront()

    while command is not None:

        print(DOCS.MENU)

        command = input('Please choose an option: ')

        match command:

            case 's':

                print(DOCS.STORE_MENU)

                cmd = ''

                while cmd is not None:

                    cmd = input("Please choose an option: ")

                    match cmd:

                        case "cpf":

                            print("Current Profit = ", storefront.get_profit())

                        case "ci":

                            print(storefront.get_available_items())

                        case "cs":

                            item_name = input("Item Name: ")

                            if storefront.has_item(item_name):
                                print(storefront.check_stock_for(item_name))
                            else:
                                print(f"We do not sell {item_name} at the moment")

                        case "cpc":

                            print(storefront.get_prices())

                        case "as":

                            item_name = input("Item name: ")
                            amount = input("Amount: ")

                            if storefront.sells_this(item_name):
                                if float(amount) > 0:
                                    storefront.add_stock(item_name, amount)
                                    print("Inventory updated.")
                                else:
                                    print("Please insert a positive amount.")
                            else:
                                print(f"We do not sell {item_name} at the moment.")

                        case "m":

                            cmd = None

                        case "h":

                            print(DOCS.STORE_MENU)

                        case "e":
                            cmd = None
                            command = None

            case "b":

                print(DOCS.BUYER_MENU)

                cmd = ''

                while cmd is not None:

                    cmd = input("Please choose na option: ")

                    match cmd:

                        case "cb":

                            print("Current Balance = ", storefront.get_shopper_balance())

                        case "ce":

                            print("Total Expense = ", storefront.get_shopper_expenses())

                        case "d":

                            amount = input("Amount: ")
                            if float(amount) > 0:
                                storefront.add_shopper_balance(amount)
                            else:
                                print("Please insert a positive amount.")

                        case "cpc":

                            print(storefront.get_prices())

                        case "ci":

                            print(storefront.get_available_items())

                        case "cs":

                            item_name = input("Item Name: ")
                            if storefront.has_item(item_name):
                                print(storefront.check_stock_for(item_name))
                            else:
                                print(f"We do not sell {item_name} at the moment")

                        case "p":

                            item_name = input("Item Name: ")
                            amount = input("Amount (Kg): ")

                            if float(amount) >= 0:
                                if storefront.has_item(item_name):
                                    if float(amount) <= storefront.check_stock_for(item_name):
                                        if storefront.can_sell(item_name, amount):
                                            storefront.sell(item_name, amount)
                                            print("Thank you for you purchase :)")
                                        else:
                                            print("Not enough balance.")
                                    else:
                                        print(f"We don't have enough {item_name} in stock.")
                                else:
                                    print(f"We don't sell {item_name} at the moment.")
                            else:
                                print("Please insert a positive amount.")

                        case "m":

                            cmd = None

                        case "h":

                            print(DOCS.STORE_MENU)

                        case "e":

                            cmd = None
                            command = None

            case "h":

                print(DOCS.MENU)

            case "e":

                command = None
