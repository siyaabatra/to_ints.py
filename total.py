# TODO Your solution(s)
import sys
from io_lib import to_ints as to_ints

def main():
    int_args = to_ints(sys.argv[1:])  # Use io_lib.to_ints on all command-line arguments
    total = sum(int_args)  # Calculate the sum of integers
    print(total)

if __name__ == "__main__":
    main()