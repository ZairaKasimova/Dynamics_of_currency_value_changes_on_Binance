import requests
import time
import datetime
import numpy as np
import matplotlib.pyplot as plt


def get_rate(currencies: str):
    '''Show the dynamics of changes in the value of the currency on the Binance website using a graph.'''
    URL = 'https://api.binance.com/api/v3/ticker/price'
    prices = np.array([])
    moments = np.array([])
    
    try:
        for i in range(20):
            response = requests.get(URL, params={'symbol':currencies})
            current_time = datetime.datetime.now()
            price = float(response.json()['price'])
            prices = np.append(prices, price)
            moments = np.append(moments, current_time)
            time.sleep(1)
        plt.plot(moments, prices)
        plt.title('Динамика изменения стоимости валюты на Binance')
        plt.show()
    except:
        print('Что-то пошло не так, возможно, Вами был неправильно передан аргумент функции get_rate().')


if __name__ == '__main__':
    get_rate('BTCUSDT')