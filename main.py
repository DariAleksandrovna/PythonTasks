money = int(input("Введите сумму\n"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = list(map(lambda x: int(x * money / 100), per_cent.values()))
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", deposit.max())
