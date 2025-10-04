def calculate_tax(income):
    if income > 50000:
        tax_amount = income * 0.10 # 10%
    else:
        tax_amount = income * 0.05 # 5%
    return tax_amount