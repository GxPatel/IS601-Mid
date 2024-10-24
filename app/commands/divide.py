import pandas as pd
from app.commands.handler import Command

class DivideCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        try:
            # Taking multiple numbers as input, separated by space
            numbers = input("Enter numbers to divide, separated by space: ").split()
            num_series = pd.Series([float(num) for num in numbers])
            # Check if there's a zero in the divisor positions
            if (num_series[1:] == 0).any():
                print("Error: Division by zero is not allowed.")
            else:
                result = num_series.iloc[0] / num_series.iloc[1:].prod()
                print(f"Result: {result}")
                self.history.append(f"Divided {', '.join(numbers)} = {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
