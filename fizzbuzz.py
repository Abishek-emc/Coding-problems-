"""Given an integer n, return a string array answer (1-indexed) where:
● answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
● answer[i] == "Fizz" if i is divisible by 3.
● answer[i] == "Buzz" if i is divisible by 5.
● answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]"""
n = 3
l = [i for i in range(1,n+1)]

for i in range(len(l)):
    if l[i]%3==0 and l[i]%5==0:
        l[i]= "FizzBuzz"
    elif l[i]%3==0:
        l[i] = "Fizz"
    elif l[i]%5==0:
        l[i] = "Buzz"
print(l)