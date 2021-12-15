def countdown(number):
    print(number)

    # Base Case
    if number <=0 :
        return
    else :
        # Recursive Case
        countdown(number - 1)

number = int(input("Enter a number: "))
countdown(number)