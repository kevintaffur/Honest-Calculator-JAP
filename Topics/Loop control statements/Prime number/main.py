value = int(input())
prime = True
if value == 1:
    prime = False
else: 
    for number in range(2, value):
        if value % number == 0 and number != value:
            prime = False
            break

if prime:
    print("This number is prime")
else:
    print("This number is not prime")
