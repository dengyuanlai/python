import math

def main():
    number = input_number()
    print(find_prime(number))

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

def find_prime(number):
    if number < 2:
        return "No, numbers less than 2 are not prime."

    sqrt_round = round(math.sqrt(number))
    for i in range(2, sqrt_round + 1):
        if number % i == 0:
            factor = str(i)
            text = "No, the number is not prime, divisible by " + factor
            return text

    return "Yes, the number is prime."

main()
