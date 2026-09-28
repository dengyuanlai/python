import math
from prime_factor import is_prime

def main():
    number = input_number()
    print(check_prime(number))

def input_number():
    number_ok = False
    while number_ok == False:
        number = input("input number to see if it's prime: ")
        try:
            number_int = int(number)
            print(f"this number you input: {number_int}")
            number_ok = True
        except:
            print("the number is not valid. Try again.")
    return number_int

def check_prime(number):
    if number < 2:
        return "No, numbers less than 2 are not prime."

    result = is_prime(number)

    return "Yes, the number is prime." if result else "No, it is not prime"

main()
