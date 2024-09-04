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


text = input_to_words("Text.txt")
print(text)
clean_text = clean_up(text)
print(clean_text)