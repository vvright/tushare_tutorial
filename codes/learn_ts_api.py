import tushare as ts

ts.set_token("1b75db5141c73a91e760400dea153620f6ce8d52d611b2abd61ebf9c")

pro = ts.pro_api()

# 获取交易日历信息
# df = pro.query('trade_cal', exchange='', start_date='20221101', end_date='20221201', fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

# print(df)

# 查询当前所有正常上市交易的股票列表
# df = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(df)

# df = pro.query('daily', ts_code='300274.SZ', start='20221201', end='20221202')
df = pro.daily(ts_code='300274.SZ', trade_date='20221202')
print(df)
