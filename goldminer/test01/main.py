# coding=utf-8
from __future__ import print_function, absolute_import
from gm.api import *

# 策略中必须有init方法
def init(context):
    subscribe(symbols='SHSE.600000', frequency='1d', count=5)
    print(context.now)
    print(context.symbols)
    print(context.account())
    print(context.parameters )
    

def on_bar(context,bars):
    #print(context.data('SHSE.600000', '1d', count=5, fields=['open','close']))
    #print(bars)
    pass

if __name__ == '__main__':
    run(strategy_id='bb59ae09-f4d1-11e7-839f-4ccc6ab44bf8',
        filename='main.py',
        mode=1,
        token='4fb4208498feaa5764af15a72cdc8cf179b60603',
        backtest_start_time='2016-06-17 13:00:00',
        backtest_end_time='2017-08-21 15:00:00')