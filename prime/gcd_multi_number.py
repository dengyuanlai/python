from factor_utils import prime_factors, turn_to_dict, multiply_factors
def main():
    test_cases = [
    # Basic cases
    ([24, 36], 12),
    ([4, 12, 8], 4),
    ([16, 6, 28, 14], 2),
    ([9, 27, 81, 900, 333], 9),

    # Two numbers
    ([10, 15], 5),
    ([17, 19], 1),
    ([100, 250], 50),
    ([144, 60], 12),
    ([81, 153], 9),

    # Multiple numbers
    ([12, 18, 24], 6),
    ([15, 25, 35], 5),
    ([42, 56, 70], 14),
    ([48, 64, 80, 96], 16),
    ([100, 200, 300, 400], 100),
    ([7, 14, 21, 28, 35], 7),
    ([36, 60, 84, 108], 12),
    ([121, 242, 363], 121),

    # GCD is 1
    ([8, 15], 1),
    ([14, 25, 33], 1),
    ([17, 23, 29], 1),
    ([12, 25, 49], 1),

    # Prime numbers
    ([2, 3], 1),
    ([13, 13], 13),
    ([17, 17, 17], 17),
    ([2, 2, 2, 2], 2),

    # Identical numbers
    ([5, 5], 5),
    ([12, 12, 12], 12),
    ([100, 100, 100, 100], 100),

    # One element
    ([7], 7),
    ([1], 1),
    ([12345], 12345),

    # Include 1
    ([1, 5, 10], 1),
    ([1, 100, 1000], 1),

    # Zero values (if supported by your implementation)
    ([0, 12], 12),
    ([0, 0, 15], 15),
    ([0, 0, 0], 0),

    # Negative numbers (if supported by your implementation)
    ([-12, 18], 6),
    ([-24, -36], 12),
    ([12, -18, 30], 6),

    # Larger numbers
    ([123456, 789012], 12),
    ([1000000, 2500000], 500000),
    ([999999, 333333], 333333),
    ([123456789, 987654321], 9),
    ([360, 840, 1260, 1680], 60),

    # Different orderings
    ([24, 36, 60], 12),
    ([60, 24, 36], 12),
    ([36, 60, 24], 12),
]
    
    for case in test_cases:
        result = gcd(case[0])
        print(case, result, result == case[1])
        
def gcd(numbers):
    factor_dict_list = []
    for number in numbers:
        factor_dict_list.append(turn_to_dict(prime_factors(number)))
        
    all_factors = {}
    for dict in factor_dict_list:
        for key in dict:
            if not key in all_factors:
                all_factors[key] = 0
    
    least_common_factors = {}
    for factor in all_factors:
        is_common = True
        min_factor_value = None
        for dict in factor_dict_list:
            if not factor in dict:
                is_common = False
                break
            else:
                min_factor_value = dict[factor] if min_factor_value == None else min(min_factor_value, dict[factor])
        
        if is_common:
            least_common_factors[factor] = min_factor_value
    
    return multiply_factors(least_common_factors)

if __name__ == "__main__":
    main()