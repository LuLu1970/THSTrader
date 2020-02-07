# -*- coding: utf-8 -*-


from THS.THSTrader import THSTrader


if __name__ == "__main__":
    trader = THSTrader(r"C:\同花顺软件\同花顺\xiadan.exe")    # 连接客户端

    print(trader.get_balance())                            # 获取当前可用资金

    print(trader.get_position())                           # 获取当前持有的股票
    print(trader.get_balance())
    # print(trader.sell(stock_no="000622", price=4.42, amount=100))  # 卖出股票

    # result = trader.buy(stock_no="000622", price=0.49, amount=100) # 买入股票
    # print(result)

    # if result["success"] == True:						   # 如果买入下单成功，尝试撤单
    #     print("撤单测试--->", end="")
    #     print(trader.cancel_entrust(entrust_no=result["entrust_no"]))
