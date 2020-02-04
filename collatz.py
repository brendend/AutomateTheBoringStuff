def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

while True:
    try:
        user_number = int(input("Give me a number: "))
    except ValueError:
        print("please enter a whole numeric value")
        continue
    else:
        break
while user_number != 1:
    n = collatz(int(user_number))
    




            
