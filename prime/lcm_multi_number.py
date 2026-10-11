import sys
from factor_utils import prime_factors, turn_to_dict, multiply_factors
from lcm import lcm as lcm_two_number
def main():
    test_cases = [
            ([24, 36], 72),
            ([4, 9, 8], 72),
            ([1, 2, 5, 7], 70),
            ([9, 397, 675, 12, 85], 18222300),
            ([2, 3, 5, 7, 9, 11, 13, 756797], 68179841730)
        ]
    
    lcm_fun = get_lcm_fun(sys.argv)
    
    print(f"lcm is {lcm_fun}")
    
    for case in test_cases:
        result = lcm_fun(case[0])
        excepted = case[1]
        print(" O " if result == excepted else " X ", case)

def lcm(numbers):
    factor_dict_list = []
    for number in numbers:
        factor_dict_list.append(turn_to_dict(prime_factors(number)))
    
    sum_factors = {}
    for factor_dict in factor_dict_list:
        for key in factor_dict:
            if key in sum_factors:
                if factor_dict[key] > sum_factors[key]:
                    sum_factors[key] = factor_dict[key]
            else:
                sum_factors[key] = factor_dict[key]
                    
    return multiply_factors(sum_factors)

def lcm_1(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm_two_number(result, numbers[i])
        
    return result

def get_lcm_fun(argv):
    # print(argv)
    lcm_fun_name = argv[1] if len(argv) > 1 else "lcm"
    lcm_fun_map = {
        "lcm": lcm,
        "lcm_1": lcm_1,
    }

    if lcm_fun_name not in lcm_fun_map:
        raise ValueError(f"Unknown lcm function '{lcm_fun_name}'. Choose from: {', '.join(lcm_fun_map.keys())}")

    return lcm_fun_map[lcm_fun_name]
                  
if __name__ == "__main__":
    main()