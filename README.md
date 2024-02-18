## Это 3 задача ДЗ

Anatoli Gutovski
Date: 19/02/2024

Условие:  найти самое длинное слово в введенном предложении.
Учтите что в предложении могут быть знаки препинания.
Пример: если введено "This is a sample sentence where the longest word is in the middle!",
то надо вернуть "sentence".



Пояснение:  этот код просто разбивает введенное предложение на слова с помощью метода split(),
а затем находит самое длинное слово с помощью функции max() с параметром key=len.
Знаки препинания в этом случае не учитываются, так как они не влияют на длину слова.