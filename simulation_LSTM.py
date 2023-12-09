from db.mysql.mysql_handler import MySqlHandler

mySqlHandler = MySqlHandler(mode="local", db_name="flowbit")
actual_data = mySqlHandler.find_all_data_from_actual_data()
predicted_data = mySqlHandler.find_all_data_from_predicted_data()

"""
알고리즘 세우기
2014-01-10일 부터 시작
"""

import pandas as pd

# 예시 데이터 생성
data = {
    'predict_C': [100, 105, 95, 110, 90, 120, 115, 105, 100, 110],
}

df = pd.DataFrame(data)

# 이동 평균 계산 함수
def calculate_moving_average(series, window):
    return series.rolling(window=window).mean()

# 전략 함수
def trading_strategy(data, short_window, long_window):
    # 초기값 설정
    data['short_ma'] = 0
    data['long_ma'] = 0
    data['signal'] = 0

    # 이동 평균 계산
    data['short_ma'] = calculate_moving_average(data['predict_C'], short_window)
    data['long_ma'] = calculate_moving_average(data['predict_C'], long_window)

    # 매매 신호 생성
    data['signal'][short_window:] = 0  # 초기값 설정
    data['signal'][short_window:] = np.where(data['short_ma'][short_window:] > data['long_ma'][short_window:], 1, 0)
    data['positions'] = data['signal'].diff()

    return data

# 전략 적용
short_window = 5
long_window = 20

df_result = trading_strategy(df.copy(), short_window, long_window)

# 결과 출력
print(df_result)

print(actual_data)
print(predicted_data)
calculate_moving_average()


calculate_moving_average