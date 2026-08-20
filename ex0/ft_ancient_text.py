import sys
from typing import IO


def read_file(path: str) -> None:
    print(f"Accessing file '{path}'")
    try:
        f: IO[str] = open(path, "r")
        content: str = f.read()
        print("---")
        print(content, end="")
        print("---")
        f.close()
        print(f"File '{path}' closed.")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    read_file(sys.argv[1])


if __name__ == "__main__":
    main()
