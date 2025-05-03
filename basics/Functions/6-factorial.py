def factorial(a):
    answer = 1
    for i in range(1, a+1):
        answer = answer * i
    return answer

print(factorial(1))
print(factorial(3))
print(factorial(10))