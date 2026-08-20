def secure_archive(
    file_name: str,
    action: int | str = "read",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action in ("read", 0):

            with open(file_name, "r") as f:
                data: str = f.read()
            return True, data

        elif action in ("write", 1):
            with open(file_name, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"

        else:
            return False, f"Unknown action: {action}"

    except OSError as e:

        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")

    success: bool
    data: str
    success, data = secure_archive("ancient_fragment.txt")
    print((success, data))

    print("Using 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_vault_file.txt", "write", data))


if __name__ == "__main__":
    main()
