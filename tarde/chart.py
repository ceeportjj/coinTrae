import pyupbit
tickers = pyupbit.get_tickers(fiat="KRW")


#일봉데이터 9시 기준
# print(pyupbit.get_ohlcv("KRW-BTC"))

#주봉차트
# print(pyupbit.get_ohlcv("KRW-BTC",interval="week"))

#최대200개 60분봉
df_min60=pyupbit.get_ohlcv(ticker="KRW-BTC", interval="minute60", count=20)

print(df_min60)
#1분봉차트
df_min1=pyupbit.get_ohlcv("KRW-BTC", interval="minute1")

how= {
    "open" :'first',
    "hight": max,
    "low"  : min,
    "close" :'last',
    "volume": sum
}

print(df_min1.resample("2T").apply(how))

# df.head(5)