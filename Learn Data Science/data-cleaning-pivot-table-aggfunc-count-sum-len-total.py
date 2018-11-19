import pandas as pd

users = pd.read_csv('users.csv')
print(users)

by_city_day = users.pivot_table(index='weekday', columns='city')
print(by_city_day)

count_by_weekday1 = users.pivot_table(index='weekday', aggfunc='count')
print(count_by_weekday1)

count_by_weekday2 = users.pivot_table(index='weekday', aggfunc=len)

print('---------------------------------------------------------------')

print(count_by_weekday1.equals(count_by_weekday2)) #aggfunc='count' == aggfunc=len

signup_and_visitors = users.pivot_table(index='weekday', aggfunc=sum)
print(signup_and_visitors)

signup_and_visitors_total = users.pivot_table(index='weekday', aggfunc=sum, margins=True)
print(signup_and_visitors_total)