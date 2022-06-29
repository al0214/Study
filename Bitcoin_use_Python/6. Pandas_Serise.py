from pandas import Series

my_list = [100, 200, 300, 400]

new_list = []

for val in my_list: 
    new_list.append(val/10)
    
s = Series([100, 200, 300, 400])

print(f's / 10 =\n {s / 10}')