import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename: str = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file: typing.IO
    try:
        file = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
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

    new_name: str = input("Enter new file name (or empty): ")
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
        print(f"Error saving file '{new_name}': {error}")
        return
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
