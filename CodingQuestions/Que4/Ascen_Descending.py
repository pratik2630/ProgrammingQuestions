#Coding question 4:
#Program to accept three numbers from user and print them in ascending and decending order

#Taking input from user and stroing it in list
NumList = []
value = int(input("Enter total number to be inserted:"))
for i in range(0 , value):
    num =int(input("Enter number {} :".format(i+1)))
    NumList.append(num)

def ascending(NumList):
    for i in range (value):
        for j in range(i + 1, value):
            if(NumList[i] > NumList[j]):
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp
    print("Number in ascending order:" , NumList)

def descending(NumList):
    for i in range (value):
        for j in range(i + 1, value):
            if(NumList[i] < NumList[j]):
                temp = NumList[i]
                NumList[i] = NumList[j]
                NumList[j] = temp
    print("Number in descending order:" , NumList)
    
ascending(NumList)
descending(NumList)
