class SecurityError(Exception):
    """Raised when PIN is incorrect"""
    pass

class InsufficientFunds(Exception):
    """Raised when withdrawal amount exceeds balance"""
    pass

class SecureAccount:
    def __init__(self, balance, pin):
        self._balance = balance #protected

        self.__pin = pin #private

        print(f"\n Account opened with initial balance: {self._balance}")

    def verify_pin(self, input_pin):
        return self.__pin == input_pin
    
    def withdraw_amount(self, amount, input_pin):
        if not self.verify_pin(input_pin):
            raise SecurityError("\n ACCESS DENIED! Pin doesn't match")
        
        if amount > self._balance:
            raise InsufficientFunds(f"\n ERROR: Balance is only {self._balance}")
        
        self._balance -= amount

        print(f"\n Successfully withdrew {amount} \n Current balance: {self._balance}")

        return self._balance
    
    def __del__(self):
        print("\n Account connection closed")