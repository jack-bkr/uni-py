
def main():
    ex = input("Pick exercise 1-6: ")

    if(ex == "1"):
        ex1()
    elif(ex == "2"):
        ex2()
    elif(ex == "3"):
        ex3()
    elif(ex == "4"):
        ex4()
    elif(ex == "5"):
        ex5()
    elif(ex == "6"):
        ex6()
    elif(ex == "7"):
        ex7()
    else:
        main()

def ex1():
    word = input("Enter a word: ")
    for i in word:
        print(i)
        
def ex2():
    num = 0
    for i in range(5):
        num += int(input("Enter a number: "))
    print("Total:", num)    
        
def ex3():
    count = 0
    digits = input("Input a string of numbers:")
    for i in digits:
        count += 1
    print("Total number of digits:", count)

def ex4():
    num = int(input("Input a number: "))
    for i in range(20):
        print(num * (i + 1))
        
def ex5():
    count = 0
    start = float(input("Enter starting amount: "))
    intrest = float(input("Enter interest: "))
    years = int(input("Enter years: "))
    
    while(count < years):
        count += 1
        start += start * intrest
    
    print(start)
    
def ex6():
    num = 1
    while(num <= 7):
        print(num, " to the power of 3 is ", (num ** 3))
        num += 1
        
def ex7():
    string = ""
    for i in range(5):
        for j in range(5):
            string += str(i+j) + " "
        string += "\n"
    print(string)
    
    
main()