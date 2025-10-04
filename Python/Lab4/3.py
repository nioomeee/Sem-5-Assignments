# Write a python program to create a class Bank with following members:
#   Id- Private
#   Name -Protected
#   Balance – Public
# Member Functions:
#   • Constructor to initialize balance as 1000.

# Create another class named Customer and add following methods:
#   withdraw() - To withdraw money
#   deposit() - To deposit money
#   interest() - calculate interest

#  Call all the methods appropriately and print Id, Name and Balance.

class Bank:
    def __init__(self, id, name):
        self.__ID = id # id is private: only accessible within the bank
        self._name = name # name is protected: accessible by Bank aand it's children
        self.Balance = 1000.0 # balance is public: accessible from anywhere

class Customer(Bank): #Customer(subclass) inherits from Bank(superclass)
    def __init__(self, id, name):
        super().__init__(id, name) #super() calls constructor of parent class
        print(f" Welcome, {self._name}, Your account has been created with initial balance of {self.Balance:.2f}")
        
