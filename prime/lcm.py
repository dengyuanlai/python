from factor_utils import prime_factors, turn_to_dict, multiply_factors

def main():
    print(lcm(24, 36) == 72)
    print(lcm(11, 13) == 143)
    print(lcm(117, 5096) == 45864)
    print(lcm(1, 3) == 3)
    print(lcm(1, 1) == 1)
    print(lcm(0, 1) == 0)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    a_factor_dict = turn_to_dict(prime_factors(a))
    b_factor_dict = turn_to_dict(prime_factors(b))
    merge_factor_dict = merge_dict(a_factor_dict, b_factor_dict)
    #print(merge_result)
    return multiply_factors(merge_factor_dict)

# union two factors list, if in both group, keep greater one
def merge_dict(dict_a, dict_b):
    for key, value in dict_a.items():
        if key in dict_b:
            if value > dict_b[key]:
                dict_b[key] = value
        else:
            dict_b[key] = value
    return dict_b

if __name__ == "__main__":
    main()