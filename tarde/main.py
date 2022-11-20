import pyupbit
import time

# 원화로 거래가능한 코인 종류
tickers = pyupbit.get_tickers(fiat="KRW")
tickers = pyupbit.get_tickers()

# 현재가
btc_curr=pyupbit.get_current_price("KRW-BTC")
# 비트코인 이더리움 가격
btc_eth=pyupbit.get_current_price("BTC-ETH")
print("ticker:",tickers)
print("btc_curr:",btc_curr)
print("btc_curr:",btc_eth)
print("btc_eth*btc_curr:",btc_eth*btc_curr)


# 포문이용해서 받기
print("포문이용해서 받기")
for t in tickers[:10]:
    price=pyupbit.get_current_price(t)
    if t[:3]=="KRW":
        print(t,f"{price}")
    else:
        print(t,f"{price:.8f}")
    time.sleep(0.1)

print("리스트로 값을 갖고오기")
#리스트로 값을 갖고오기
data= pyupbit.get_current_price(["KRW-BTC","BTC-ETH"])
print(data)

print("keyvalue")

#딕셔너리
data=pyupbit.get_current_price(tickers[:10])
for key,value in data.items():
    print(f"[key:9]",value)
