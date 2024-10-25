# Advanced Python-Based Calculator: [Demonstrating video](https://drive.google.com/file/d/1A_GttAriyoDxoVJSkmnYzSfua3x5ohlp/view?usp=sharing)

This project is an advanced Python-based calculator designed with professional software development practices. The calculator supports basic operations like addition, subtraction, multiplication, and division. It uses **design patterns**, **logging**, **environment variables**, and features **real-time user interaction via a command-line interface (REPL)**. This project also incorporates **error handling** with "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) approaches. Additionally, **Pandas** is used to demonstrate efficient data handling.

## Features
- **Design Patterns**: Command Pattern for flexible operation handling.
- **Dynamic Configuration**: Managed with environment variables.
- **Comprehensive Logging**: Capturing and logging key events in the system.
- **Error Handling**: Structured exception handling with LBYL and EAFP principles.
- **Real-time User Interaction**: Interactive calculator with REPL functionality.
- **Data Handling**: Pandas used for efficient and scalable numerical operations.

---

## Design Patterns
This project utilizes the **Command Pattern** to decouple the actions (calculator operations) from the invoker (REPL). This pattern allows the application to easily add, remove, or extend new commands with minimal changes.

### [Command Pattern Implementation](app/commands/__init__.py)
The `Command` class is used to define operations like addition, subtraction, multiplication, and division. The `CommandHandler` class manages the registration and execution of these commands.

- `commands/add.py` [AddCommand](app/commands/add.py)
- `commands/subtract.py` [SubtractCommand](app/commands/subtract.py)
- `commands/multiply.py` [MultiplyCommand](app/commands/multiply.py)
- `commands/divide.py` [DivideCommand](app/commands/divide.py)

---

## Environment Variables
This project uses environment variables to load application configurations, allowing dynamic behavior changes without modifying the source code. The environment variables are managed using the `dotenv` library.

### [Environment Variables Implementation](app/__init__.py#L18)
The environment variables are loaded and accessed using `os.environ` to configure settings such as logging behavior and environment mode (e.g., production, development).

---

## Logging
Comprehensive logging is used to capture important events in the application, including command execution, plugin loading, and error handling. The `logging` module is used for this purpose, and configuration is dynamically managed via environment variables.

### [Logging Implementation](app/__init__.py#L22)
Logs are written to a file and console, with different logging levels (INFO, ERROR). Logging is configured based on the existence of a `logging.conf` file or defaults to basic configuration.

---

## Exception Handling (LBYL & EAFP)
The project uses both **Look Before You Leap (LBYL)** and **Easier to Ask for Forgiveness than Permission (EAFP)** approaches for exception handling to ensure robustness.

### [LBYL Approach - Divide Command](app/commands/divide.py#L10)
The **LBYL** approach is used in the division command to check for zero divisors before performing the division.


### [EAFP Approach - Command Execution](app/commands/__init__.py#L20)
The **EAFP** approach is used in command execution to handle unknown commands by catching the `KeyError` exception.

---

## Data Handling with Pandas
Pandas is used to handle user input as a **Series** and perform numerical operations efficiently, especially for the division command, which supports multiple inputs.

### [Pandas Integration](app/commands/divide.py#L12)
The numbers are converted into a Pandas Series, and the division operation is performed across the series. This allows handling more complex input scenarios efficiently.

---

This project demonstrates the application of professional practices in software development, ensuring maintainable, robust, and scalable code.

--- 

### Contributors
- Goral Patel
