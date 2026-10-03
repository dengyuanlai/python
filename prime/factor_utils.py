import math

def is_prime(number):
    if number < 2:
        return False

    sqrt_round = round(math.sqrt(number))
    for i in range(2, sqrt_round + 1):
        if number % i == 0:
            return False

    return True

def is_prime_faster(number):
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2

    return True

def prime_factors(number):
    if number < 2:
        return []
    
    if is_prime_faster(number):
        return [number]

    result = []
    for i in range(2, number + 1):
        if number % i == 0:
            factor = number // i
            if is_prime_faster(i):
                result.append(i)
            else:
                result.extend(prime_factors(i))

            if is_prime_faster(factor):
                result.append(factor)
            else:
                result.extend(prime_factors(factor))
            return result

def prime_factors_faster(number):
    if number < 2:
        return []

    result = []

    # Handle factor 2 separately
    while number % 2 == 0:
        result.append(2)
        number //= 2

    # Only need to test odd numbers up to sqrt(number)
    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            result.append(factor)
            number //= factor
        factor += 2

    # If what's left is greater than 1, it's prime
    if number > 1:
        result.append(number)

    return result

def turn_to_dict(factor_list):
    factor_dict = {}
    for factor in factor_list:
        if factor in factor_dict:
            factor_dict[factor] += 1
        else:
            factor_dict[factor] = 1

    return factor_dict

def multiply_factors(factor_dict):
    result = 1
    for key, value in factor_dict.items():
        result *= key ** value
    return result
