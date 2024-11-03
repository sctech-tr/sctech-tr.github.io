import sys

def main():
    if len(sys.argv) > 1:
        print(' '.join(sys.argv[1:]))
    else:
        print("No input provided")

if __name__ == "__main__":
    main()