#Повертає масив слів всього тексту у файлі. На вхід приймає шлях до файлу
def input_to_words(path):
    t = open(path)
    return t.read().split()

#Переводить всі букви у нижній регістр та видяляє всі вказані символи.
#На вхід приймає масив рядків(слів) та рядок символів, що потрібно видалити(за замовченням ".,/#:")
def clean_up(text_arr, toremove = ".,/#:"):
    t = text_arr
    for i in range(0, len(t)):
        for j in toremove:
            t[i] = t[i].replace(j,"").lower()
    return t


# Функція, яка змінює регістр букв (верхній на нижній і навпаки) для всього тексту
def swaplit(text_arr):
    for word in range(len(text_arr)):
        text_arr[word] = text_arr[word].swapcase()  # Інвертуємо регістр для кожного слова
    return text_arr

# Функція, яка замінює всі 'o' на 'і' в тексті
def replace_o_with_i(text_arr):
    for o in range(len(text_arr)):
        text_arr[o] = text_arr[o].replace('o', 'і').replace('O', 'І')  # Заміна 'o' на 'і' та 'O' на 'І'
    return text_arr

text = input_to_words("Text.txt")
print(text)
clean_text = clean_up(text)
print(clean_text)

# Застосовуємо swapcase для інвертування регістру
swapped_text = swaplit(clean_text)
print("Текст з інвертованим регістром:")
print(swapped_text)

# Застосовуємо заміну 'o' на 'і'
replaced_text = replace_o_with_i(swapped_text)
print("Текст з заміною 'o' на 'і':")
print(replaced_text)

# Вивід тексту у зворотньому порядку
def reverse_text(text_arr):
    return text_arr[::-1]
reversed_text = reverse_text(replaced_text)
print("Текст у зворотньому порядку:")
print(reversed_text)   

# Вивід кожне друге слово
def every_second_word(text_arr):
    return text_arr[1::2]
second_words = every_second_word(replaced_text)
print("Кожне друге слово:")
print(second_words) 