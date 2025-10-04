# Demonstrate the usage of assert keyword.

def apply_discount(discount_percent, price):

    assert 0 <= discount_percent <= 100, "Discount percent must be between 0 and 100."

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount

final_price_1 = apply_discount(50, 650)

try:
    final_price_2 = apply_discount(150, 650)
    print(f"\n Price with 150% discount: ${final_price_2}")

except AssertionError as e:
    print(f"\n Assertion error occured: {e}")