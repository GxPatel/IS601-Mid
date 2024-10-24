import pandas as pd
from app.commands.handler import Command

class SubtractCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        try:
            # Taking multiple numbers as input, separated by space
            numbers = input("Enter numbers to subtract, separated by space: ").split()
            num_series = pd.Series([float(num) for num in numbers])
            # Subtracting all subsequent numbers from the first number
            result = num_series.iloc[0] - num_series.iloc[1:].sum()
            print(f"Result: {result}")
            self.history.append(f"Subtracted {', '.join(numbers)} = {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
