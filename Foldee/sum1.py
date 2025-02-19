def sum_of_digit(n):
    sum = 0
    if(n==0):
        return 0
    return n % 10 +sum_of_digit(n//10)
n= int(input("Enter the number: "))
print(sum_of_digit(n))

      