# Divisable by 3 -> "Fizz"
# Divisable by 5 -> "Buzz"
# Divisable by both -> "Fizz Buzz"

# 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'Fizz Buzz', 16, 17, 'Fizz', 19, ...

def fizzBuzz(n):
    list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("Fizz Buzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
    return list

def fizzBuzz2(n):
    return ["Fizz Buzz" if (i%3 == 0 and i%5 == 0) else "Fizz" if i%3 == 0 else "Buzz" if i%5 == 0 else i for i in range(1, n+1)]

print(fizzBuzz(40))

print(fizzBuzz2(40))