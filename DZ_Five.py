Revenue = float(input("Введите выручку: "))
Costs = float(input("Введите издержки: "))
if Revenue < Costs:
    print("У вас убыточная компания: ")
elif Revenue == Costs:
    print("Ваша рентабильность 0 рублей: ")
else:
    print("Ваша прибыль составила:" f" {Revenue - Costs:.3f}")
    a = float(Revenue - Costs)
    b = float(input("Введите колличество сотрудников: "))
    print("Прибыль на сотрудника составила: "f"{b / a:.3f}")
