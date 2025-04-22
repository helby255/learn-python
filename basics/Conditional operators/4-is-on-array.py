cars = ['lada', 'bmw', 'fiat', 'gazele', 'uaz', 'kia']
russian_cars = ['lada', 'gazele', 'uaz']

print("Введите марку авто:")
for x in cars:
    print(x)
print("")
selected_car = input()

if selected_car in cars:
    print("Машина " + selected_car + " есть в списке.")
else:
    print("Такой машины нет в списке.")

if selected_car in russian_cars:
    print("Машина продается со скидкой 20%")