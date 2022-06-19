#Write a program to print all the prime numbers from 5 to 50.

for i in range(5,50):
    for j in range(2,int(i/2)+1):
        if(i&j)==0:
            break
    else:
        print(i, "is a prime number") 
            