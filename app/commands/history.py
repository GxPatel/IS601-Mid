from app.commands.handler import Command

class HistoryCommand(Command):
    def __init__(self, history):
        self.history = history

    def execute(self):
        if not self.history:
            print("No calculations yet.")
        else:
            print("Calculation History:")
            for record in self.history:
                print(record)
