#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def checkAllDifferent(lista):

    doubled = False

    for number in range(0, len(lista)):
        #print("PRIMO FOR Number: ", number, " valore:", lista[number])
        for var in range(0, len(lista)):
            #print("--SECONDO FOR: var: ", var, " valore:", lista[var])
            if ( (lista[number] == lista[var]) and (number != var)):
                doubled = True

    if(doubled):
        print("You have a double!")
    else:
        print("Your numbers are all different from each other")



if __name__ == '__main__':
    numbers = [0,1,2,3,4,5,6,7,8,9]
    checkAllDifferent(numbers)













