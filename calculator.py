class Calculator():
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
calci = Calculator()

add_result = calci.add(2, 3)
print(f"Addition Result: {add_result}")

multiply_result = calci.multiply(4, 5)
print(f"Multiplication Result: {multiply_result}")
