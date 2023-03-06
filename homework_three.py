s1 = input("Pleas, input  you string?:")  # Вводим необходимую строку
s1 = s1.lower()  # переводим в нижний регистр
# удаляем пунктуацию в тексте
s2 = s1.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "").replace(";", "")
s2 = s2.rstrip()  # удаляем пробелы с права
print(s1)
print(s2)

s3 = input("With what do you want to replace?""\n")  # Указываем что мы хотим найти в тексте
s3 = s3.lower()  # переводим в нижний регистр
s3 = s3.rstrip()  # удаляем пробелы с права
print(f"Was found at position: {s1.find(s3)}")  # Сообщает позицию необходимого слова в тексе

s4 = input("With what do you want to replace? \n")  # Указываем на что хотим изменить найденное ранее слово
s4 = s4.lower()  # переводим в нижний регистр
s4 = s4.rstrip()  # удаляем пробелы с права
print("Here is your result :""\n " + s2.replace(s3, s4))  # Выводим готовый текс и изменениями
