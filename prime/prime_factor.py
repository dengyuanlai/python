import time
from factor_utils import prime_factors
    
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

if __name__ == "__main__":
    main()
