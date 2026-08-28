from datetime import datetime
from pathlib import Path

BOOK_FILE = "my_book.txt"


def handle_input():
    """Prompt the user and return (date, type, amount, description)."""
    date_ok = False
    while not date_ok:
        input_date = input("input date: (YYYY-MM-DD, Enter for today, 'quit' to exit): ")
        if input_date.strip().lower() in ("quit", "exit"):
            raise SystemExit
        try:
            date = datetime.today().date() if input_date.strip() == "" else datetime.strptime(input_date, "%Y-%m-%d").date()
            date_ok = True
        except ValueError:
            print("invalid date, try again.")

    type_ok = False
    while not type_ok:
        input_type = input("+ for in, - for out: ")
        if input_type in ["+", "-"]:
            type_ok = True
        else:
            print("invalid type, try again")

    amount_ok = False
    while not amount_ok:
        amount_of_cash = input("input amount of cash: ")
        try:
            cash_float = float(amount_of_cash)
            if cash_float > 0:
                amount_ok = True
            else:
                print("amount must be greater than 0.")
        except ValueError:
            print("invalid amount of cash, try again.")

    description = input("description: ")
    return date, input_type, cash_float, description


def handle_save(date, input_type, cash_float, description):
    record = f"{date}\t{input_type}\t{cash_float}\t{description}\n"
    with open(BOOK_FILE, "a") as f:
        f.write(record)
    print("Record saved.")


def display_book():
    print(f"{'date':^12}{'type':^10}{'amount':^10}{'description'}")
    print("-" * 50)
    total = 0.0
    with open(BOOK_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) < 4:
                continue
            print(line, end="")
            sign = 1 if parts[1] == "+" else -1
            total += sign * float(parts[2])
    print("-" * 50)
    print(f"Balance: ${total:.2f}")


def main():
    Path(BOOK_FILE).touch()
    display_book()
    while True:
        date, input_type, cash_float, description = handle_input()
        handle_save(date, input_type, cash_float, description)
        display_book()


if __name__ == "__main__":
    main()