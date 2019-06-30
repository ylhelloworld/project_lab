import tushare as ts
import pandas  as pd
df = ts.get_tick_data('000725',date='2019-02-25',src='tt')
print(df)