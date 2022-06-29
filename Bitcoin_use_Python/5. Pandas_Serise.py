from pandas import Series 

date = ['2018-08-01', '2018-08-02', '2018-08-03', '2018-08-04', '2018-08-05'] 
xrp_close = [512, 508, 512, 507, 500] 

s = Series(xrp_close, index=date) 
print(s)

print(s[0])
print(s['2018-08-01'])

print(f's의 인덱스 : {s.index}')
print(f's의 값 : {s.values}')

print(s[['2018-08-02', '2018-08-04']])

print(s['2018-08-01' : '2018-08-03'])
print(s[0:2])

s['2018-08-06'] = 490 
print(s.drop('2018-08-01')) 
print(s)

######################################
# 연산 # 
my_list = [100, 200, 300, 400]
new_list = []
for val in my_list: 
    new_list.append(val/10)