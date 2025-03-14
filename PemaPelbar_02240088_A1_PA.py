
'''def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

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

        userchoice = input('Enter choice (0-5):')
        if userchoice == 1:
            try:
                start = int(input('Enter start number:'))
                end = int(input('Enter end number:'))
                if start > end:
                    start, end = end, start
                
                total = 0
                for num in range(max(2, start), end + 1):
                    if is_prime(num):
                        total += num
                
                print(f"Sum of primes from {start} to {end}: {total}")
            except ValueError:
                print("Please enter valid integers")
        elif userchoice == 2:'''


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
    # convert btw centimeter and meter
    if direction.upper() == 'CM':
        #convert centimeter to meter (1 mter = 10 cm)
        return round(value * 10, 2)
    elif direction.upper() == 'M':
        #convert metr to centimeter(1 centimeter = 0.1 meter)
        return round(value * 0.1, 2)
    else:
        print("Try Again: It must be 'CM' or 'M'")
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