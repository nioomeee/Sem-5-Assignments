# Define a class Teacher with the following specification:
#  Private members:
#       Name : 20 char
#       Subject: 10 char
#       Basic, DA,HRA : float
#       Salary: float
# Calculate () - function computes the salary and returns it.
# Salary is sum of basic, DA and HRA
# Public member: Readdata() function accept the data values and invoke the calculate
# function

class Teacher:
    def __init__(self):
        self.__Name = ""
        self.__Subject = ""
        self.__Basic = 0.0
        self.__DA = 0.0
        self.__HRA = 0.0
        self.__Salary = 0.0

    def __Calculate(self): # it's a pvt method because it starts with __
        return self.__Basic + self.__DA + self.__HRA
    
    def ReadData(self): # it's a public function
        print(f"Please enter Teacher details: ")
        self.__Name = input("Enter Name: ")
        self.__Subject = input("Enter Subject: ")
        self.__Basic = float(input("Enter Basic Salary: "))
        self.__DA = float(input("Enter DA: "))
        self.__HRA = float(input("Enter HRA: "))

        self.__Salary = self.__Calculate() # setting the salary using the calculate function 
                                            #from within the class itself

    def DisplayData(self):
        print(f"----- Teacher Details -----")
        print(f" Name: {self.__Name}")
        print(f" Subject: {self.__Subject}")
        print(f" Total Salary: {self.__Salary}")


Teacher1 = Teacher()

Teacher1.ReadData()

Teacher1.DisplayData()

