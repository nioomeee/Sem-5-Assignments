from BankingSystem.accounts import SecureAccount, SecurityError, InsufficientFunds

balance = float(input("\n Enter the amount for initial balance: "))
pin = input("\n Enter your 4 digit pin: ")

my_account = SecureAccount(balance, pin)

withdraw = float(input("\n Enter the amount you want to withdraw: "))

re_pin = input("\n Enter the pin for your account: ")

try:
    
    my_account.withdraw_amount(withdraw, re_pin)

except SecurityError as e:
    print(f"\n Security Error: {e}")

except InsufficientFunds as e:
    print(f"\n TRANSACTION FAILED: {e}")

except Exception as e:
    print(f"\n Error occured: {e}")

print("\n Delting account now...")
del my_account

