'''test_commands.py'''
import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.greet import GreetCommand
from app.commands.history import HistoryCommand
from app.commands.menu import MenuCommand
from app.commands.exit import ExitCommand

@pytest.fixture
def history():
    '''history tracking'''
    return []

def test_add_command(history, monkeypatch, capsys):
    '''testing add command'''
    command = AddCommand(history)
    monkeypatch.setattr('builtins.input', lambda _: '5 10')
    command.execute()
    captured = capsys.readouterr()
    assert "Result: 15.0" in captured.out
    assert "Added 5, 10 = 15.0" in history

def test_add_command_invalid_input(monkeypatch, capsys):
    '''Test AddCommand for invalid inputs'''
    add_cmd = AddCommand([])
    monkeypatch.setattr('builtins.input', lambda _: 'invalid')
    add_cmd.execute()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter valid numbers." in captured.out

def test_subtract_command(history, monkeypatch, capsys):
    '''testing subtact command'''
    command = SubtractCommand(history)
    monkeypatch.setattr('builtins.input', lambda _: '10 5')
    command.execute()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_multiply_command(history, monkeypatch, capsys):
    '''testing multiply command'''
    command = MultiplyCommand(history)
    monkeypatch.setattr('builtins.input', lambda _: '4 5')
    command.execute()
    captured = capsys.readouterr()
    assert "Result: 20.0" in captured.out

def test_divide_command(history, monkeypatch, capsys):
    '''testing divide command'''
    command = DivideCommand(history)
    monkeypatch.setattr('builtins.input', lambda _: '10 2')
    command.execute()
    captured = capsys.readouterr()
    assert "Result: 5.0" in captured.out

def test_divide_by_zero(history, monkeypatch, capsys):
    '''testing divide by zero'''
    command = DivideCommand(history)
    monkeypatch.setattr('builtins.input', lambda _: '10 0')
    command.execute()
    captured = capsys.readouterr()
    assert "Error: Division by zero is not allowed." in captured.out

def test_greet_command(capsys):
    '''testing greet command'''
    greet_cmd = GreetCommand()
    greet_cmd.execute()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out

def test_history_command(capsys):
    '''testing history command'''
    history_cmd = HistoryCommand(["Added 1, 2 = 3", "Subtracted 5, 3 = 2"])
    history_cmd.execute()
    captured = capsys.readouterr()
    assert "Added 1, 2 = 3" in captured.out
    assert "Subtracted 5, 3 = 2" in captured.out

def test_menu_command(capsys):
    '''testing menu command'''
    menu_cmd = MenuCommand()
    menu_cmd.execute()
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add" in captured.out
    assert "subtract" in captured.out
    assert "multiply" in captured.out
    assert "divide" in captured.out
    assert "history" in captured.out
    assert "exit" in captured.out

def test_exit_command():
    '''testing ExitCommand functionality (SystemExit)'''
    exit_cmd = ExitCommand()
    with pytest.raises(SystemExit):
        exit_cmd.execute()
