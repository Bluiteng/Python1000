Number = int(input("Please Enter Number: "))
print("Result is: ",end=" ")
for i in range(4,-1,-1):
    temp = Number//10**i
    Number = Number % 10**i
    print(temp,end=" ")
