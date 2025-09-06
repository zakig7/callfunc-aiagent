# Calculator

A simple command-line calculator application that evaluates mathematical expressions for testing purposes.

## Features

- Supports addition, subtraction, multiplication, and division.
- Handles nested and complex expressions.
- Error handling for invalid operators and insufficient operands.
- Formats the output in a visually appealing box.

## Usage

```bash
python main.py "<expression>"
```

For example:

```bash
python main.py "3 + 5"
python main.py "2 * 3 - 8 / 2 + 5"
```

## Example Output

```
┌─────────┐
│  3 + 5  │
│         │
│  =      │
│         │
│  8      │
└─────────┘
```

## Dependencies

- Python 3.x

## Installation

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Run the `main.py` file with the expression as an argument.

## Testing

To run the tests, execute the following command:

```bash
python tests.py
```

## Project Structure

```
.
├── main.py         # Main application file
├── pkg/            # Package containing calculator logic
│   ├── calculator.py # Calculator class with evaluation logic
│   └── render.py     # Function to render the output
├── tests.py        # Unit tests for the calculator
└── readme.md       # This file
```
