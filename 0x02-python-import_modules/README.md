# 0x02-python-import_modules

This repository contains Python code examples and exercises related to importing modules in Python.

## Files

- `0-add.py`: A Python script that imports a function from another module and uses it to perform addition.
- `1-calculation.py`: A Python script that imports functions from another module and uses them to perform various calculations.
- `2-args.py`: A Python script that prints the number of and the list of its arguments.
- `3-infinite_add.py`: A Python script that prints the result of the addition of all arguments.
- `4-hidden_discovery.py`: A Python script that prints all the names defined by a compiled module.
- `5-variable_load.py`: A Python script that imports a variable from another module and prints its value.

## Usage

To run any of the Python scripts, use the following command:

```
python <script_name>.py
```

Replace `<script_name>` with the name of the script you want to execute.

## Examples

```
$ python 0-add.py
Result: 10

$ python 1-calculation.py
Addition: 5 + 2 = 7
Subtraction: 10 - 3 = 7
Multiplication: 8 * 2 = 16
Division: 100 / 10 = 10

$ python 2-args.py
0 arguments.
$ python 2-args.py Hello
1 argument:
1: Hello

$ python 3-infinite_add.py
Result: 10

$ python 4-hidden_discovery.py
__builtins__
__doc__
__file__
__loader__
__name__
__package__
__spec__
my_variable

$ python 5-variable_load.py
Value of my_variable: 98
```

