def factorial(a):
    answer = 1
    for i in range(1, a+1):
        answer = answer * i
    return answer

print("Factorials:")
for i in range(1,10):
    print(str(i) + " = " + str(factorial(i)))