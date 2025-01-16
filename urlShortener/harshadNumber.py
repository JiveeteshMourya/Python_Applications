num = int(input("Enter a number to check for Harshad Number: "))
def chechHarshadNumber(num):
    n = 0
    temp = num
    while(temp != 0):
        n += temp%10
        temp /= 10
    
    if(num%n == 0):
        print("Its Harshad Number")
    else:
        print("Its not")
chechHarshadNumber(num)