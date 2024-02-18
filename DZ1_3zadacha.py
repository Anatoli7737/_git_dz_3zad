# Anatoli Gutovski
# Date: 18/02/2024
# Description: Homework 2_zadacha4
# Grodno IT Academy Python 3.11.7


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если введено "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"


def longest_word(sentence):
    vse_slova = sentence.split()  # Разбиваем предложение на слова
    max_dlin_slovo = max(vse_slova, key=len)  # Находим самое длинное слово
    return max_dlin_slovo


sentence = input("Введите предложение: ")
max_dlin_slovo = longest_word(sentence)
print(f"Самое длинное слово в предложении: {max_dlin_slovo}")

# return False
