import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK , HTTP_404_NOT_FOUND
from yahoo_fin.stock_info import * 
from yahoo_fin.stock_info import get_quote_table
import yfinance as yf
import queue
from threading import Thread
import time


class ListStock(APIView):
    def get(self,request):
        stock_picker = tickers_nifty50()
        return Response(data=stock_picker , status=HTTP_200_OK)
    


class GetStocks(APIView):
    def post(self,request):
        stockPicker = request.data 
        stocks_dict = []
        available_stocks = tickers_nifty50()
        for stocks in stockPicker:
            if stocks  in available_stocks:
                pass
            else:
                message = "Stocks is Not in Nifty 50"
                return Response(status= HTTP_404_NOT_FOUND , data=message)
        n_threads = len(stockPicker)
        thread_list = []
        que = queue.Queue()
        for i in range(n_threads):
            thread = Thread(target = lambda q, arg1: q.put({stockPicker[i]: yf.Ticker(arg1).history(period="1d")}), args = (que, stockPicker[i]))
            thread_list.append(thread)
            thread_list[i].start()

        for thread in thread_list:
            thread.join()

        while not que.empty():
            result = que.get()
            print(result)
            stocks_dict.append(result)
        return Response(data=stocks_dict ,status=HTTP_200_OK)