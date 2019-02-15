def fizzbuzz(a, b):
    try:
        lenghtOfList1List2 = len(a + b)

        if (lenghtOfList1List2 % 3 == 0 and lenghtOfList1List2 % 5 == 0):
            return("fizzbuzz")
        elif (lenghtOfList1List2 % 5 == 0):
            return("buzz")
        elif (lenghtOfList1List2 % 3 == 0):
            return("fizz")
        else:
            return(lenghtOfList1List2)
    except TypeError:
        return("Invalid input")
