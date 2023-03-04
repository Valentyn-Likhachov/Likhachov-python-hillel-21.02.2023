s1 = input("Pleas, input  you string?:")  # Вводим необходимую строку
s1 = s1.lower()  # переводим в нижний регистр
s2 = "".join(s1 for s1 in s1 if s1.strip(".,-:;?!"))  # удаляем все символы пунктуации и пробелы
print(s1)
print(s2)

s3 = input("With what do you want to replace?""\n")  # что мы хотим поменять в введённой ранее
s4 = "Hello!, My name is ?-vAlentyn . I am learning Java!"  # Пример строки (s1) для поиска и замены слова
print("was found at position", s4.find("Java"))  # Указываем слово которое хотим найти и заменить

s5 = input("With what do you want to replace?""\n")  # На что меняет указанное ранее слово
print("Here is your result :""\n " + s2.replace("java", "python"))  # Выводим готовый результат преобразованной строки
