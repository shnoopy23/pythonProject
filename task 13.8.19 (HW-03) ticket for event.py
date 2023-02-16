tickets = int(input("Введите количество билетов \n"))
age = [int(input("Введите возраст участника \n")) for i in range(tickets)]
cost = 0
for i in age:
    if i < 18:
       cost += 0
    if 18 <= i <25:
        cost += 990
    if i >= 25:
        cost += 1390

print(cost, " итого стоимость билетов")

if tickets > 3:
    cost = cost - cost * 0.1
print(cost, " итого стоимость билетов со скидкой")











