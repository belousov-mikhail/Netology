# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 08:49:12 2017

@author: Mikhail Belousov
"""

family_budget = 500

flight_costs = 50

trip_counts = 3

trip_length_1 = 10
trip_length_2 = 20
trip_length_3 = 10

expenses = [ [], []]

for n in range (2): #ввод расходов на двух человек, без защиты от дурака
    adding_expenses = ''
    while adding_expenses != 'no':
        adding_expenses = input ('Введите сумму расхода, чтобы завершить ввод, введите no,  -->')
        if adding_expenses == 'N':
            break
        else:
            expenses[n].append (float (adding_expenses))

print (sum (expenses[0]))      

day_cost = 20
flights_per_trip = 2 

trip_cost = (trip_length_1 + trip_length_2 + trip_length_3) * day_cost
trip_cost = trip_cost + flight_costs * trip_counts * flights_per_trip

print ('Стоимость поездки в евро:', trip_cost) 

rouble_rate = 62.68 
print ('Курс евро к рублю на сегодня составляет: ', rouble_rate) # вывели курс евро
print ('Стоимость поездки в рублях:', trip_cost*rouble_rate) # вывели стоимость поездки в рублях


months_before_trip = 3 
save_per_month = trip_cost / months_before_trip
print ('Нужно откладывать каждый месяц ', save_per_month, 'евро')

if family_budget < trip_cost:
  print ('Затраты на поездку превышают бюджет за один месяц на ', trip_cost - family_budget, 'евро') # вывели предупреждение о превышении бюджета за месяц

# if family_budget * months_before_trip < trip_cost :
# print ('Затраты на поездку превышают бюджет  на ', trip_cost - family_budget, 'евро') # вывели предупреждение о превышении бюджета за срок months_before_trip

if family_budget < trip_cost:
  deficit = trip_cost - family_budget
  print ('Дефицит бюджета:', deficit,'евро')
else:
  proficit = family_budget - trip_cost
  print ('У нас остаток:', proficit, 'евро')