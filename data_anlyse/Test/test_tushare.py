import tushare as ts
print("start")
df = ts.get_tick_data('600848',date='2014-01-09')
result=df.head(10)
print(result)
print("end")