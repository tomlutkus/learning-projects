import sys

def format_full_name(f_name, l_name):
    full_name = f"{f_name.title()} {l_name.title()}"
    return full_name

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 task.py <first name> <last name>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])