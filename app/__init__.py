import os
import logging
import logging.config
from dotenv import load_dotenv

class App:
    def __init__(self):
        self.command_handler = None
        self.history = []

    def load_commands(self):
        from app.commands import GreetCommand, MenuCommand, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand, HistoryCommand, ExitCommand
        from app.commands.handler import CommandHandler
        self.command_handler = CommandHandler()

        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("add", AddCommand(self.history))
        self.command_handler.register_command("subtract", SubtractCommand(self.history))
        self.command_handler.register_command("multiply", MultiplyCommand(self.history))
        self.command_handler.register_command("divide", DivideCommand(self.history))
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("history", HistoryCommand(self.history))

    def start(self):
        self.load_commands()
        logging.info("Starting application...")
        print("Welcome to the advanced calculator!")
        print("Type 'menu' to see available commands, 'history' to see previous calculations or 'exit' to quit.")
        while True: # REPL: Read-Evaluate-Print Loop
            cmd_input = input(">>> ").strip()
            self.command_handler.execute_command(cmd_input)
