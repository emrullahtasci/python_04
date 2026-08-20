import sys
from typing import IO, Optional


def read_file(filename: str) -> Optional[str]:
    print(f"Accessing file '{filename}'")
    try:
        file: IO[str] = open(filename, "r")
        content: str = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")
        return content
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None


def transform(content: str) -> str:
    lines: list[str] = content.splitlines()
    return "".join(f"{line}#\n" for line in lines)


def save_file(new_content: str) -> None:
    new_filename: str = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        out: IO[str] = open(new_filename, "w")
        out.write(new_content)
        out.close()
        print(f"Data saved in file '{new_filename}'.")
    except OSError as error:
        print(f"Error opening file '{new_filename}': {error}")
        print("Data not saved.")


def main() -> None:
    argv: list[str] = sys.argv
    if len(argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    content: Optional[str] = read_file(argv[1])
    if content is None:
        return

    print("Transform data:")
    new_content: str = transform(content)
    print("---")
    print(new_content, end="")
    print("---")

    save_file(new_content)


if __name__ == "__main__":
    main()
