name = ''


print('Кажется, я вас не знаю.')

while name != 'fedor':
    name = input('Ваше имя? ')
    if name != 'fedor':
        print('Мы с вами не знакомы. ' + name)
print('Рад встрече с вами, ' + name + '!')