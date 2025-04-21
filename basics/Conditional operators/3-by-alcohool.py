print ("Сколько вам лет?")
age = int(input())

if age < 18:
    print ("Уроки сделал?")
elif age >= 18:
    print ("Какой алкоголь вы хотите купить?")
    aclo_buy = input()
    print("Вы покупаете " + aclo_buy)
else:
    print("ERROR")