#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if operator not in operations:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {operations[operator](a, b)}")

