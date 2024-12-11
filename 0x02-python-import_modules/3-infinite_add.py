#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = sum(int(arg) for arg in sys.argv[1:])
    print(total)
