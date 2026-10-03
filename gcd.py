from prime_factor import prime_factors
from lcm import turn_to_dict, multiply_factors

def gcd(a, b):
    if a == 0 or b == 0:
        raise ValueError("no gcd for zero")
    a_factor_dict = turn_to_dict(prime_factors(a))
    b_factor_dict = turn_to_dict(prime_factors(b))
    merge_factor_dict = merge_dict(a_factor_dict, b_factor_dict)
    #print(merge_result)
    return multiply_factors(merge_factor_dict)

# intersection two factor list, keep smaller
def merge_dict(a_factor_dict, b_factor_dict):
    result_dict = {}
    for key, value in a_factor_dict.items():
        if key in b_factor_dict:
            result_dict[key] = min(value, b_factor_dict[key])
    return result_dict

def main():
    test_cases = [
        [24, 36, 12],
        [4, 9, 1],
        [1, 2, 1],
        [3, 5, 1]
    ]
    
    for case in test_cases:
        print(gcd(case[0], case[1]) == case[2])
        
if __name__ == "__main__":
    main()