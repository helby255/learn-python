def tel_book(name, phone, address):
    book_record = {
        'name': name,
        'phone': phone,
        'address': address
    }
    return book_record

user1 = tel_book("fedor", "88005553535", "Magnitogorsk. gorod")
user2 = tel_book("vasiliy", "03", "zazhopinsk")

print(user1)
print(user2)