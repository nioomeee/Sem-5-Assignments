# Build a Restaurant ordering system. Create classes for MenuItem and
# Order. Allow adding menu items and computing the total bill with tax. Access
# attributes via methods only (no direct attribute printing).

class MenuItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price


class Order:
    def __init__(self):
        self.__items=[]

    def add_item(self, menu_item):
        self.__items.append(menu_item)
        print(f"\n Added {menu_item.get_name()} to your order")

    def calculate_total(self, tax_rate_percent):
        subtotal = 0

        for item in self.__items:
            subtotal += item.get_price()

        tax_amount = subtotal * (tax_rate_percent / 100)

        total = subtotal + tax_amount

        return {"subtotal": subtotal, "tax": tax_amount, "total": total}

# Create some menu items
pizza = MenuItem("Pizza", 450)
pasta = MenuItem("Pasta", 350)
coke = MenuItem("Diet Coke", 60)

# create new order
my_order = Order()

# Adding those items to the order
my_order.add_item(pizza)
my_order.add_item(pasta)
my_order.add_item(coke)

# Calculate final bill with 5% tax
bill = my_order.calculate_total(5)

# print the final bill
print("\n ------- Your Bill ------- ")
print(f"\n Subtotal: {bill["subtotal"]:.2f}")
print(f"\n Tax (5%): {bill["tax"]:.2f}")
print(f"\n Total : {bill["total"]:.2f}")


