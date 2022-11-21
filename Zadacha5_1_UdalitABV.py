# Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = input("Введите текст :\n")
print(f"Исходный текст: {text}")
del_text = "абв"
new_text = [i for i in text.split() if del_text not in i]
print(f'Результат: {" ".join(new_text)}')