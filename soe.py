# Sieve of Eratosthenes
numbers = []
max_number = 200

def init():
    numbers[:] = ["E"] * (max_number + 1)

def mark():
    min_number = 2
    while min_number <= max_number:
        numbers[min_number] = 'O'
        cross_out(min_number)
        min_number = next_min(min_number)
        if (min_number == -1):
            return
        
def cross_out(current_number):
    index = current_number + 1  
    while index <= max_number:
        if index % current_number == 0:
            numbers[index] = 'X'
        index += 1

def next_min(current_number):
    index = current_number + 1  
    while index <= max_number:
        if numbers[index] == 'E':
            return index
        index += 1
    
    return -1

def print_result():
    result = []
    for index, char in enumerate(numbers):
        if char == 'O':
            result.append(str(index))
    print(", ".join(result))

def main():
    init()
    mark()
    print_result()

if __name__ == "__main__":
    main()