import math
import time

def main():
    number = input_number()
    start_time = time.perf_counter()
    print(f"prime factors: {prime_factors(number)}")
    end_time = time.perf_counter()
    print(f"elapsed time: {end_time - start_time:.6f} seconds")

def input_number():
    number_ok = False
    while number_ok == False:
        number = input("input number to see prime factor: ")
        try:
            number_int = int(number)
            print(f"this number you input: {number_int}")
            number_ok = True
        except:
            print("the number is not valid. Try again.")
    return number_int

def is_prime(number):
    if number < 2:
        return False

    sqrt_round = round(math.sqrt(number))
    for i in range(2, sqrt_round + 1):
        if number % i == 0:
            return False

    return True

def prime_factors(number):
    if number < 2:
        return []
    
    if is_prime(number):
        return [number]

    result = []
    for i in range(2, number + 1):
        if number % i == 0:
            factor = number // i
            if is_prime(i):
                result.append(i)
            else:
                result.extend(prime_factors(i))

            if is_prime(factor):
                result.append(factor)
            else:
                result.extend(prime_factors(factor))
            return result

main()
