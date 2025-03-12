
def is_prime(n):
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
        elif userchoice == 2: