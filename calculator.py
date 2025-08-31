class Calculator():
    def add(self, a, b):
        return a + b
    
    def subtact(self, a, b):
        return a - b
    
calci = Calculator()

add_result = calci.add(2, 3)
print(f"Addition Result: {add_result}")

subtact_result = calci.subtact(5, 1)
print(f"Subtraction Result: {subtact_result}")
