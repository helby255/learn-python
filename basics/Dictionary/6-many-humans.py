human1 = { 
'location' : 'Russia', #location = key ; Russia = value
'race' : 'human',
'age' : 20,
'name' : 'Fedor'
}

all_humans = []

for x in range(0, 10):
    all_humans.append(human1.copy())

for xx in all_humans:
    print(xx)