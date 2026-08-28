import csv

DATA_FILE = "users.csv"


def load_users(filepath: str) -> dict[str, str]:
    users = {}
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users[row["username"].lower()] = row["password"]
    print(f"Loaded {len(users)} users from '{filepath}'.\n")
    return users


def main():
    users = load_users(DATA_FILE)

    while True:
        input_username = input("Username (or 'quit' to exit): ").strip()
        username = input_username.lower()
       
        if username == "quit":
            print("Goodbye!")
            break
        
        if not (username in users):
            print(f"{input_username} not exist")
            continue
        
        password = input("Password: ").strip()
        if password.lower() == "quit":
            print("Goodbye!")
            break

        if users.get(username) == password:
            print(f"Welcome, {input_username}: {password} ! Login successful.\n")
        else:
            print("Invalid username or password. Please try again.\n")


if __name__ == "__main__":
    main()
