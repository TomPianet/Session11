def m6() :
    """
    A function that returns a multiple of 6
    :return:
    """
    while True:
        try :
            number = input("Please give me a multiple of 6 number")
            number = int(number)

        except ValueError :
            print("This is not a number.Retry")
            continue
        if number % 6 == 0:
            return number
        print("That number is not a multiple of 6. Retry")
