'''test_app.py'''
import pytest
from app import App
from app.commands.add import AddCommand

def test_app_add_command(monkeypatch, capsys):
    """Test that the AddCommand correctly computes the sum of numbers."""
    app = App()
    app.load_commands()
    app.command_handler.register_command("add", AddCommand(app.history))
    # Mock input for '1 2 3'
    monkeypatch.setattr('builtins.input', lambda _: '1 2 3')
    app.command_handler.execute_command('add')
    captured = capsys.readouterr()

    assert "Result: 6.0" in captured.out
    assert "Added 1, 2, 3 = 6.0" in app.history

def test_app_exit_command(monkeypatch):
    """Test that the app exits correctly on 'exit' command."""
    app = App()
    app.load_commands()
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit):
        app.start()
