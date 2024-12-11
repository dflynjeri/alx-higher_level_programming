#!/usr/bin/python3
print("".join([chr(c) if c % 2 == 1 else chr(c).upper() for c in range(122, 96, -1)]), end="")

