msg = ''
list = []
while msg != 'stop':
    msg = input('Введите новый элемент массива. Если закончили, то отправьте stop и я покажу вам массив.')
    list.append(msg)

list.remove('stop')
print(list)
