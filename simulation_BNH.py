from db.mysql.mysql_handler import MySqlHandler
from matplotlib import pyplot as plt
import numpy as np

def get_predicted_value(timestamp, predicted_data):
    for i in predicted_data:
        if i["timestamp"] == timestamp:
            return i
    return False

def get_rate(buy_value, current_value):
    return (current_value / buy_value) * 100 - 100

mySqlHandler = MySqlHandler(mode="local", db_name="flowbit")
actual_data = mySqlHandler.find_all_data_from_actual_data()
predicted_data = mySqlHandler.find_all_data_from_predicted_data()

"""
알고리즘 세우기
2014-01-10일 부터 시작
사고있지 않은 상태에서,
다음날에 비트코인 가격이 오른다면? -> 구매
내린다면? -> 팔기
"""

actual_data_index = 14
predicted_data_index = 0

rate_list = []

isSell = False
money = 1000000 #잔고
buyMoney = 0 #구매량
buyState = 0 #구매했을 때의 비트코인 가격

while len(actual_data) > actual_data_index:
    #print(actual_data[actual_data_index])
    #print(predicted_data[predicted_data_index])
    actual_close_price = actual_data[actual_data_index]["close_price"]
    predicted_close_price = predicted_data[predicted_data_index]["predicted_price"]

    if isSell == False:
        #매도하지 않은 상태
        if actual_close_price < predicted_close_price:
            #상승할 전망
            
            buyMoney = money
            money = 0
            buyState = actual_close_price
            isSell = True
    else:
        if actual_close_price > predicted_close_price:
            rate = get_rate(buyState, actual_close_price)
            money = buyMoney + (buyMoney / 100 * rate)
            isSell = False
            rate_list.append(rate)
    actual_data_index += 1
    predicted_data_index += 1

print(money)

x = range(0, len(rate_list))
y = rate_list

plt.plot(x,y)
plt.show()