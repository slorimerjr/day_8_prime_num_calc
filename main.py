#Write your code below this line 👇
#prime = only divisible by 1 and itself

# my solution:
def prime_checker(number):
    f = 2
    s = []
    while f < number:
        if number % f == 0:
            s.append(f)
        f += 1
    if len(s) > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")
            

# teacher solution:
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



