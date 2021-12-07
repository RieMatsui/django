from django.shortcuts import render
from pandas import pandas as pd
import csv
import os

from django.http import HttpResponse


def index(request):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/customer_master.csv'
    df = pd.read_csv(filePath)
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'customerCsv/index.html', context)


def getCustomerData():
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/customer_master.csv'
    df = pd.read_csv(filePath)
    return df


def itemMaster(request):
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'customerCsv/index.html', context)


def getItemData():
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/item_master.csv'
    df = pd.read_csv(filePath)
    return df


def getTransactionData():
    transaction_1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/transaction_1.csv'
    transaction_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/transaction_2.csv'
    df_transaction_1 = pd.read_csv(transaction_1)
    df_transaction_2 = pd.read_csv(transaction_2)
    # データをユニオンする
    transaction = pd.concat([df_transaction_1, df_transaction_2], ignore_index=True)
    return transaction


def transaction(request):
    transaction = getDetailData()
    data_num = len(transaction)
    context = {
        'df': transaction,
        'data_num': data_num,
    }
    return render(request, 'customerCsv/index.html', context)


def getDetailData():
    transaction_detail_1 = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/transaction_detail_1.csv'
    transaction_detail_2 = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/transaction_detail_2.csv'
    df_detail_1 = pd.read_csv(transaction_detail_1)
    df_detail_2 = pd.read_csv(transaction_detail_2)
    # データをユニオンする
    df_details = pd.concat([df_detail_1, df_detail_2], ignore_index=True)
    return df_details


def transactionDetail(request):
    #  トランザクションデータの詳細データを取得する
    df_detail = getDetailData()
    data_num = len(df_detail)
    context = {
        'df': df_detail,
        'data_num': data_num,
    }
    return render(request, 'customerCsv/index.html', context)


def saleData(request):
    # トランザクションデータを取得する
    df_detail = getDetailData()
    dt_transaction = getTransactionData()
    dt_customer = getCustomerData()
    dt_item = getItemData()
    join_data = pd.merge(df_detail,
                         dt_transaction[["transaction_id", "payment_date", "customer_id"]],
                         on='transaction_id',
                         how='left')

    join_data = pd.merge(join_data,
                         dt_customer,
                         on='customer_id',
                         how='left')

    join_data = pd.merge(join_data,
                         dt_item,
                         on='item_id',
                         how='left')

    join_data['price'] = join_data['quantity'] * join_data['item_price']
    data_num = len(join_data)

    # 欠損値があるかをチェックします
    sum_data = join_data.isnull().values.sum()
    message = ''
    if (sum_data > 0):
        message = '欠損値があります。'

    # トータルを出力
    total = join_data.describe()

    context = {
        'df': join_data,
        'data_num': data_num,
        'message': message,
        'total': total,
    }
    return render(request, 'customerCsv/sale_data.html', context)
