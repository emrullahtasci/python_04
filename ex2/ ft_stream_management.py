import sys
from typing import IO, Optional


def print_error(message: str) -> None:
    print(f"[STDERR] {message}", file=sys.stderr)


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
        print_error(f"Error opening file '{filename}': {error}")
        return None


def transform(content: str) -> str:
    lines: list[str] = content.splitlines()
    return "".join(f"{line}#\n" for line in lines)


def read_line_from_stdin(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    return line.rstrip("\n")


def save_file(new_content: str) -> None:
    new_filename: str = read_line_from_stdin(
        "Enter new file name (or empty): "
    )

    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        out: IO[str] = open(new_filename, "w")
        out.write(new_content)
        out.flush()
        out.close()
        print(f"Data saved in file '{new_filename}'.")
    except OSError as error:
        print_error(f"Error opening file '{new_filename}': {error}")
        print("Data not saved.")


def main() -> None:
    argv: list[str] = sys.argv
    if len(argv) != 2:
        print("Usage: ft_stream_management.py <file>")
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
