def car_reward(car, *persons):
    #АААВТОМОБИИИЛЬ
    for person in persons:
        print(person.title() + " в нашей передаче выигрывает АААВТОМОБИИИЛЬ! И это новенькая " + car)

car1 = "LADA Granta с автоматом!"
car2 = "гнилая газелька 3310"

car_reward(car1, "fedor", "alexandr", "vasiliy")
car_reward(car2, "Ivan", "Anton")