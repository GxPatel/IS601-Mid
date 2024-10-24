from app.commands.handler import Command
import sys

class ExitCommand(Command):
    def execute(self):
        print("Exiting the app...")
        sys.exit(0)
