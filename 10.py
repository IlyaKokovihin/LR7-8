text = input()
if len(text) % 2 == 0:
    srd = "В строке четное количество символов"
else:
    srd = 'Средний символ ' + text[len(text) // 2]

print("Первый символ", text[0])
print(srd)
print("Последний символ", text[-1])