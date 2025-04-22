human1 = { # item
'location' : 'Russia', #location = key ; Russia = value
'race' : 'human',
'age' : 20,
'name' : 'Fedor'
}

print(human1)

human1['age'] = 21

print(human1)
print('Что-то ' + human1['name'] + ' постарел...') 