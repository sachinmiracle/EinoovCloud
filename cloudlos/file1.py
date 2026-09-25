def main():
    name = input("Enter your name: ").strip()
    print(f"Hello, {name or 'World'}! Welcome to Python.")


if __name__ == "__main__":
    main()