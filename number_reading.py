import subprocess

def input_number():
    number_ok = False
    while number_ok == False:
        number = input("input number to read: ")
        try:
            number_int = int(number)
            number_ok = True
        except:
            print("the number is not valid. Try again.")
    return number_int

under_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
 "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
 "Eighteen", "Nineteen", "Twenty"]

tens_multiples = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

def convert_number(number, place_value, place_name):
    place = number // place_value
    remainder = number % place_value
    
    result = []
    result.append(show_number(place))
    result.append(place_name)
    if (remainder > 0):
        result.append(show_number(remainder))
    
    return " ".join(result)

def show_number(number):
    if number == 0:
        return "Zero"
    elif number <= 20:
        return under_20[number]
    elif number < 100:
        tens = number // 10
        remainder = number % 10
        remainder_str = "" if remainder == 0 else show_number(remainder)
        return f"{tens_multiples[tens]} {remainder_str}"
    elif number < 1_000:
        return convert_number(number, 100, "Hundred")
    elif number < 1_000_000:
        return convert_number(number, 1000, "Thousand")
    elif number < 1_000_000_000:
        return convert_number(number, 1_000_000, "Million")
    elif number < 1_000_000_000_000:
        return convert_number(number, 1_000_000_000, "Billion")
    else:
        print("too big")

def speak(text):
    try: 
        subprocess.run(["say", text])
    except:
        print("no voice on your device")

def main():
    numbers = [0, 12, 102, 4578, 654633, 27564509, 1054735577]
    for number in numbers:
        print(number, show_number(number))
    
    number = input_number()
    text = show_number(number)
    print(text)
    speak(text)

main()