from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.history = []

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            command = self.commands[command_name]
            result = command.execute()
            if result:
                self.history.append(result) 
        except KeyError:
            print(f"Unknown command: {command_name}")
