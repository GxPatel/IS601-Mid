from app.commands.handler import Command

class GreetCommand(Command):
    def execute(self):
        print("Hello, World!")
