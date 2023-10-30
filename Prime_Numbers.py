start = input("What is the first number of the range1 that you want to know the prime numbers of: ")
end = input("What is the second number of the range that you want to know the prime numbers of: ")
end = int(end) + 1
start = int(start) - 1
for num in range(int(start),int(end)):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)

file = open('test.txt', 'a')
file.write(str(num))
file.close()
