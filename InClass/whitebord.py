# Given a random number as an input to a function, return "FIZZ" if the number is even and "BUZZ" if the number is odd


def fizz_buzz():
    user = int(input("Please enter a number: "))
    if user %3 == 0 and user %5 == 1:
        return "FizzBuzz"
        return "Fizz"
    else:
        user %5 == 0
        return "Buzz"

print(fizz_buzz())


# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number