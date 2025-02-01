print("Hello")


cats = ["Barsik", "Murzik","Matur"]

print(list(enumerate(cats)))

for idx, name in enumerate(cats):
    print(f"{idx} . {name}")

print( list(reversed(cats)))


eng_dic ={
    "cat": "кот",
    "car": "машина"
}
for key, value in eng_dic.items():
    print(f" Ключ: {key} - значение: {value} ")
symbol_number = ord("а")
while symbol_number <= ord("я"):
    print(f"number - {symbol_number} : letter - {chr(symbol_number)}")
    symbol_number += 1

print( "test git - second coomit")