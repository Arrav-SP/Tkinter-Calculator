# Tkinter Calculator

## Overview
This project is a basic calculator application built with Python's Tkinter library. The calculator features a graphical user interface (GUI) where users can perform simple arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- **User-friendly GUI** with buttons for digits (0-9) and operations (+, -, ×, ÷)
- **Entry widget** to display input and results
- **Clear** button to reset the input
- **Equals** button to compute the result

## How It Works
- The main window (`root`) is created using Tkinter.
- An Entry widget (`e`) displays numbers and results.
- Number and operation buttons are arranged in a grid layout.
- When a number button is pressed, it appends the digit to the entry.
- When an operation button is pressed, it stores the current number and the operation.
- Pressing "=" computes the result using the selected operation.
- "Clear" resets the entry box for new calculations.

## Usage
1. Run the Python script.
2. Enter numbers by clicking the digit buttons.
3. Choose an operation (+, -, ×, ÷).
4. Enter the next number.
5. Click "=" to see the result.
6. Use "Clear" to reset and start over.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)

## How to Run
Save the code in a `.py` file and execute:
