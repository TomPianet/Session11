def m6() :
    """
    A function that returns a multiple of 6
    :return:
    """
    while True:
        try :
            #first we need to read a number
            number = input("Please give me a multiple of 6 number")
            number = int(number)

        except ValueError :
            #if the number is not valid print an error and retry
            print("This is not a number.Retry")
            continue
        #check if the number is a multiple of 6
        if number % 6 == 0:
            # return the value
            return number
        # print and error and try again
        print("That number is not a multiple of 6. Retry")

print("A multiple of 6 number is,", m6())