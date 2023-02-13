money = int(input(("Введите сумму вклада")))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit=[]
deposit.append(money*per_cent['ТКБ']/100)
deposit.append(money*per_cent['СКБ']/100)
deposit.append(money*per_cent['ВТБ']/100)
deposit.append(money*per_cent['СБЕР']/100)
print(deposit)
print('Максимальная сумма,которую вы можете заработать', max(deposit))





