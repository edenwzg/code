# -*- coding: utf-8 -*-

from gmsdk.api import StrategyBase

class Mystrategy(StrategyBase):
    def __init__(self, *args, **kwargs):
        super(Mystrategy, self).__init__(*args, **kwargs)


    def on_login(self):
        pass

    def on_error(self, code, msg):
        pass

    def on_bar(self, bar):
        pass

    def on_execrpt(self, res):
        pass

    def on_order_status(self, order):
        pass

    def on_order_new(self, res):
        pass

    def on_order_filled(self, res):
        pass

    def on_order_partiall_filled(self, res):
        pass

    def on_order_stop_executed(self, res):
        pass

    def on_order_canceled(self, res):
        pass

    def on_order_cancel_rejected(self, res):
        pass


if __name__ == '__main__':
    myStrategy = Mystrategy(
        username='-',
        password='-',
        strategy_id='43c1cbc0-f42d-11e7-af61-4ccc6ab44bf8',
        subscribe_symbols='SZSE.000001.bar.60',
        mode=2,
        td_addr='127.0.0.1:8001'
    )
    ret = myStrategy.run()
    print('exit code: ', ret)