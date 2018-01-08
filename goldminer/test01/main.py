# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

# 策略中必须有init方法
def init(context):
    subscribe(symbols='SHSE.600000', frequency='1d', count=5)

if __name__ == '__main__':
    run(strategy_id='ed367b56-f4bd-11e7-a989-408d5c29b4d4',
        filename='main.py',
        mode=MODE_BACKTEST,
        token='4fb4208498feaa5764af15a72cdc8cf179b60603',
        backtest_start_time='2017-05-17 13:00:00',
        backtest_end_time='2017-08-21 15:00:00')