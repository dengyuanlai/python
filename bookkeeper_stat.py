from datetime import datetime
from pathlib import Path

BOOK_FILE = "my_book.txt"


def handle_input():
    """Prompt the user and return (date, type, amount, description)."""
    year_ok = False
    while not year_ok:
        input_year = input("input year: (YYYY, Enter for this year, 'quit' to exit): ")
        # when enter quit or exit, exit loop and program
        if input_year.strip().lower() in ("quit", "exit"):
            print("bye~")
            raise SystemExit
        try:
            year = datetime.today().date().year if input_year.strip() == "" else int(input_year)
            year_ok = True
        except ValueError:
            print("invalid date, try again.")

    return year


def display_book():
    print(f"{'date':^12}{'type':^10}{'amount':^10}{'description'}")
    print("-" * 50)
    total = 0.0
    with open(BOOK_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            # invalid line, skip
            if len(parts) < 4:
                continue
            print(line, end="")
            sign = 1 if parts[1] == "+" else -1
            total += sign * float(parts[2])
    print("-" * 50)
    print(f"Balance: ${total:.2f}")

def load_book():
    book_records = []
    with open(BOOK_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            # invalid line, skip
            if len(parts) < 4:
                continue
            date = datetime.strptime(parts[0], "%Y-%m-%d").date()
            sign = parts[1]
            amount = float(parts[2])
            record = (date, sign, amount)
            book_records.append(record)
    
    return book_records

def init_report_data():
    report_data = []
    for i in range(12):
        report_data.append([0,0])
    return report_data

def build_report_data(year, book_records, report_data):
    for record in book_records:
        if record[0].year != year:
            continue
        month = record[0].month
        if record[1] == '+':
            report_data[month - 1][0] += record[2]
        else:
            report_data[month - 1][1] += record[2]
            
months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
          "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

def monthly_report(report_data):
    monthly_report_list = []
    for i in range(len(report_data)):
        report = report_data[i]
        month_report = report[0] - report[1]
        final_month_report = [months[i], month_report]
        monthly_report_list.append(final_month_report)
    return monthly_report_list

def show_report(report_data):
    for i in range(len(report_data)):
        month_data = report_data[i]
        month_name = months[i]
        print(month_name, '+' * round(month_data[0]))
        print(' ' * len(month_name), '-' * round(month_data[1]))
        
def main():
    # ensure file exists before start
    Path(BOOK_FILE).touch()
    while True:
        year = handle_input()
        print(year)
        book_records = load_book()
        report_data = init_report_data()
        build_report_data(year, book_records, report_data)
        monthly_report_list = monthly_report(report_data)
        show_report(report_data)
        print(monthly_report_list)

        #display_book()


if __name__ == "__main__":
    main()