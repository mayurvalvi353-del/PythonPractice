'''def countDown(number):
    print(number)
    if number == 0 :
        return
    else :
        print("Going to the Recursion :", number)
        countDown(number - 1)
        print("Out of recursion : ", number)

print("Starting Recursion")
countDown(5)
print("Finished Recursion")'''

def factorial(number):
    if number <= 0 :
        return 1
    else :
        return number * factorial(number - 1)
print(factorial(5))


