# Create class A, class B, and class C(A, B). Both A and B have a method speak(). 
# Call C().speak() and tell me which one runs.

class A:
    def speak(self):
        print("\n A speaks.")

class B:
    def speak(self):
        print("\n B speaks.")

class C(A, B):
    pass

obj = C()

# calling the method
obj.speak()

# checking the MRO(Method Resolution Order)
print(f"\n MRO for class C: ")
for cls in C.__mro__:
    print(f" -> {cls.__name__}")