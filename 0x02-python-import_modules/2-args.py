#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]  # Exclude the script name
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

