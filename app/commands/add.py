import pandas as pd
from app.commands.handler import Command

class AddCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        try:
            # Taking multiple numbers as input, separated by space
            numbers = input("Enter numbers to add, separated by space: ").split()
            # Using Pandas Series to handle the numbers
            num_series = pd.Series([float(num) for num in numbers])
            result = num_series.sum() 
            print(f"Result: {result}")  
            calculation = f"Added {', '.join(numbers)} = {result}"
            self.history.append(calculation)
            return calculation
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return None
