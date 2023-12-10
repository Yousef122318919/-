import re

def is_haiku(text):
    lines = re.split('/', text)
    if len(lines) != 3:
        return "Не хайку. Должно быть 3 строки."
    syllables = [len(re.findall('[aeiou]', line, re.IGNORECASE)) for line in lines]
    if syllables == [5, 7, 5]:
        return "Хайку!"
    else:
        return "Не хайку."
print(is_haiku("a e i o u / a e i o u a e / a e i o u"))  # Хайку!
print(is_haiku("a e i o / a e i o u a e / a e i o u"))  # Не хайку.
print(is_haiku("a e i o u / a e i o u a e / a e i o u / a e i"))  # Не хайку. Должно быть 3 строки.
print(is_haiku("a e i o u a / a e i o u a e / a e i o u"))  # Не хайку.
print(is_haiku("a e i o u / a e i o u a e i / a e i o u"))  # Хайку!