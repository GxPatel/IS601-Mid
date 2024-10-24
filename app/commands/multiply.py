import pandas as pd
from app.commands.handler import Command

class MultiplyCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        try:
            # Taking multiple numbers as input, separated by space
            numbers = input("Enter numbers to multiply, separated by space: ").split()
            num_series = pd.Series([float(num) for num in numbers])
            # Multiplying all the numbers in the Series
            result = num_series.prod()
            print(f"Result: {result}") 
            self.history.append(f"Multiplied {', '.join(numbers)} = {result}")      
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
