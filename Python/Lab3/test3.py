from finance.tax.income_tax import calculate_tax
from finance.tax.gst import calculate_gst

print(f" ----- Financial Calculator ----- ")

salary = 60000
payable_tax = calculate_tax(salary)
in_hand = salary - payable_tax
print(f" For a salary of {salary}")
print(f" The income tax is: {payable_tax}")
print(f" Your in-hand salary is: {in_hand}")


product_price = 1000
product_gst = calculate_gst(product_price)
final_price = product_price + product_gst
print(f" For a product of price {product_price:.2f}")
print(f" The gst is {product_gst:.2f}")
print(f" The final payable price = {final_price:.2f}")