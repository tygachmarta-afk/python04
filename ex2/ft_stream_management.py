import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO
    try:
        file = open(filename, "r")
    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{filename}': {error}\n"
        )
        return

    content: str = file.read()
    print("---")
    print(content, end="")
    print("---")
    file.close()
    print(f"File '{filename}' closed.")

    # Add the archive character '#' at the end of each line
    new_content: str = ""
    for char in content:
        if char == "\n":
            new_content += "#\n"
        else:
            new_content += char
    # Last line without a trailing newline
    if len(content) > 0 and content[len(content) - 1] != "\n":
        new_content += "#\n"

    print("Transform data:")
    print("---")
    print(new_content, end="")
    print("---")

    # Read user input from stdin without input()
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name: str = sys.stdin.readline()
    # readline() keeps the trailing newline: remove it
    if len(new_name) > 0 and new_name[len(new_name) - 1] == "\n":
        new_name = new_name[:len(new_name) - 1]

    if len(new_name) == 0:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    out: typing.IO
    try:
        out = open(new_name, "w")
        out.write(new_content)
        out.close()
    except OSError as error:
        sys.stderr.write(
            f"[STDERR] Error opening file '{new_name}': {error}\n"
        )
        return
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()