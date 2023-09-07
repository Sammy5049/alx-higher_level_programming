import argparse

def main():
    parser = argparse.ArgumentParser(description="A program to print a list of numbers.")
    
    # Use nargs="*" to accept zero or more numbers
    parser.add_argument("numbers", type=float, nargs="*", help="Numbers to be listed")
    
    args = parser.parse_args()
    
    # Check if any arguments were provided
    if args.numbers:
        print("List of numbers:", args.numbers)
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()