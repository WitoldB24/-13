tickets = int(input("Введите кол-во мест."))
print("Введите возраст каждого посетителя")
s = 0
for i in range(tickets):
    age = int(input("Возраст: "))
    if 0 < age < 18:
        s += 0
    elif 18 <= age < 25:
        s += 990
    else:
        s += 1390
if tickets > 3:
    p = 0.9
else:
    p = 1
print("Сумма к оплате: ", s * p)
