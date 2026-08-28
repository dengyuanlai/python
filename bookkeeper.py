from datetime import datetime
from pathlib import Path

def main():
    date_ok = False
    while not date_ok:
        input_date = input("input date: (YYYY-MM-DD, Enter for today): ")
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

    record = f"{date}\t{input_type}\t{cash_float}\t{description}\n"

    with open("my_book.txt", "a") as f:
        f.write(record)

    print("Record saved.")
    
    print_book()


def balance():
    total = 0.0
    with open("my_book.txt", "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) < 4:
                continue
            sign = 1 if parts[1] == "+" else -1
            total += sign * float(parts[2])
    print(f"Balance: ${total:.2f}")

def print_book():
    print(f"{'date':^12}{'type':^10}{'amount':^10}{'description'}")
    print("-" * 50)
    with open("my_book.txt", "r") as f:
        for line in f:
            print(line, end="")
    print("-" * 50)
    balance()


if __name__ == "__main__":
    Path("my_book.txt").touch()
    print_book()
    while True:
        main()