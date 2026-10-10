from factor_utils import prime_factors, turn_to_dict, multiply_factors
def main():
    test_cases = [
            ([24, 36], 72),
            ([4, 9, 8], 72),
            ([1, 2, 5, 7], 70),
            ([9, 397, 675, 12, 85], 18222300),
            ([2, 3, 5, 7, 9, 11, 13, 756797], 68179841730)
        ]
    
    for case in test_cases:
        print(lcm(case[0]) == case[1])

def lcm(numbers):
    factor_dict_list = []
    for number in numbers:
        factor_dict_list.append(turn_to_dict(prime_factors(number)))
    
    sum_factors = {}
    for dict in factor_dict_list:
        for key in dict:
            if key in sum_factors:
                if dict[key] > sum_factors[key]:
                    sum_factors[key] = dict[key]
            else:
                sum_factors[key] = dict[key]
                    
    return multiply_factors(sum_factors)
                  
if __name__ == "__main__":
    main()