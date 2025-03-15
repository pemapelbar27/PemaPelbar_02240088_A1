# function 1: Prime num sum calculator
def prime(num):
    #check if a num is prime
    #num less than 2 are not prime
    if num > 2:
        return False
    #check divisibility
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_num_start(start, end):
    #Calculate sum of prime num in range
    #Ensure start is less than end
    if start > end:
        start, end = end, start
    #Calculate sum of primes(atleast start from 2)
    prime_sum = 0
    for num in range(max(2,start), end+1):
        if prime(num):
            prime_sum += num
    return prime_sum

#Function 2: Length unit converter
def length_conv(value, direction):
    # convert btw meter and feet
    if direction.upper() == 'M':
        #convert meters to feet (1 meter = 3.28084 feet )
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':
        #convert feet to meters(1 foot = 0.3048 meter)
        return round(value * 0.3048, 2)
    else:
        print("Try Again: It must be 'M' or 'F'")
        return None
#Function 3: Consonant counter
def consonant_counter(text):
    #count consonant in string
    consonants = "bcdfghjklmnpqrstvwxyz"  
    count = 0
    #count each consonant letter
    for letter in text.lower():
        if letter in consonants:
            count += 1
    return count
# Function 4: Min-Max num finder
def min_max_finder(numbers):
    #find max and min in a values
    if not numbers:
        return None, None
    #use in built-in min and max function
    return min(numbers), max(numbers)
#Function 5: Palindra Checker 
def palindra(text):
    #check if a string is a palindra
    #remove space and make lower case
    clean_text = ''
    for letter in text.lower():
        if letter != ' ':
            clean_text += letter
    #compare string with its reverse
    return clean_text == clean_text[::-1]
#Function 6: word counter
import requests
#Function 6: word counter
def word_counter(file):
    response = requests.get (file)
    text = response.text.lower()
    word_list = ["the", "was", "and"]

    word = {word:text. count(word) for word in word_list}
    return word
    # file_path = input("Enter file_path:")
    # print('Word count results:', word_counter(file_path))

#to get the valid numeric input
def get_valid_num(prompt, num_type = int):
    #get valid numeric input from user
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {num_type.__name__}")

#Main program
def main():
    while True:
        print('Math and string function')
        print('1.Prime number sum')
        print('Length converter')
        print('3.Consonant counter')
        print('4.Min-Max number finder')
        print('5.Palindrome checker')
        print('6 word counter')
        print('*Exit program')
#get user chice
        choice = get_valid_num("Enter your choice (0-6):")
#Process user choice
        if choice == 0:
            print("Thank you for using the program")
            break
        elif choice == 1:
    #prime num sum
            print("Prime number Sum Calculator")
            start = get_valid_num("Enter start range:")
            end = get_valid_num("Enter end range:")
            result = prime_num_start(start,end)
            print(f"Sum of prime numbers between {start} and {end}: {result}")
        elif choice == 2:
    #length converter 
            print("Length unit converter")
            value = input("Enter value to convert:", float)
            direction = input("Enter direction (F for meter to feet, M for feet to meter):")
            result = length_conv(value, direction)
            if result is not None:
                if direction.upper() == 'M':
                    print(f"{value} meter = {result} feet")
                else:
                    print(f"{value} feet = {result} meter")
        elif choice == 3:
            #consonant counter
            print("Consonant Counter")
            text = input("Enter a text:")
            result = consonant_counter(text)
            print(f"Number of consonants: {result}")
        elif choice == 4:
            #Min-Max Finder
            print("Min-max number Finder")
            count = get_valid_num("How many numbers to enter")
            if count <= 0:
                print("Please enter a positive number")
                continue
            numbers = []
            for i in range(count):
                num = get_valid_num(f"Enter number {i+1}: ", float)
                numbers.append(num)
            min_val, max_val = min_max_finder(numbers)
            print(f"Smallest: {min_val}, Largest: {max_val}")
        elif choice == 5:
            #palindrome checker
            print('Palindroma checker')
            text = input("Enter a text: ")
            result = palindra(text)
            print(f"Is '{text}' a palindroma? {result}")
        #elif choice == 6:
            #word counter

        elif choice == 6:
          file = input("Enter the URL of the text file : ").strip()
          try:
              result = word_counter(file)
              print(f"WORD COUNTED : {result}")
          except requests.exceptions.RequestException as e:
                print(f"Error fetching the file : {e}")
       

        else:
            print('Error, please enter a number between 0-6')
        #wait for user before continuing
        input("Please enter to continue")
#Run the program
if __name__ == '__main__':
    main()