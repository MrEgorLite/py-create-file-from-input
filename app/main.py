def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    with open(file_name, "w") as f:
        while True:
            text = input("Enter new line of content: ")
            if text == "stop":
                break
            f.write(text + "\n")


if __name__ == "__main__":
    main()
