from django.shortcuts import render
from pandas import pandas
from matplotlib import pyplot
import japanize_matplotlib
import pathlib
import os
from app.processing_data.lib.file import read


def index(request):
    df = read.csv_read('/data/sale/customer_master.csv')
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'processing_data/sale/index.html', context)


def get_customer_data():
    return read.csv_read('/data/sale/customer_master.csv')


def item_master(request):
    df = get_customer_data()
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'processing_data/sale/index.html', context)


def get_item_data():
    return read.csv_read('data/sale/item_master.csv');

def get_transaction_data():
    transaction_1 = read.csv_read('data/sale/transaction_1.csv')
    transaction_2 = read.csv_read('data/sale/transaction_2.csv')
    # データをユニオンする
    return pandas.concat([transaction_1, transaction_2], ignore_index=True)


def transaction(request):
    transaction = get_detail_data()
    data_num = len(transaction)
    context = {
        'df': transaction,
        'data_num': data_num,
    }
    return render(request, 'processing_data/sale/index.html', context)


def get_detail_data():
    transaction_detail_1 = read.csv_read('data/sale/transaction_detail_1.csv')
    transaction_detail_2 = read.csv_read('data/sale/transaction_detail_2.csv')
    # データをユニオンする
    df_details = pandas.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
    return df_details


def transaction_detail(request):
    #  トランザクションデータの詳細データを取得する
    df_detail = get_detail_data()
    data_num = len(df_detail)
    context = {
        'df': df_detail,
        'data_num': data_num,
    }
    return render(request, 'processing_data/sale/index.html', context)


def sale_data(request):
    # トランザクションデータを取得する
    df_detail = get_detail_data()
    dt_transaction = get_transaction_data()
    dt_customer = get_customer_data()
    dt_item = get_item_data()
    join_data = pandas.merge(df_detail,
                             dt_transaction[["transaction_id", "payment_date", "customer_id"]],
                             on='transaction_id',
                             how='left')

    join_data = pandas.merge(join_data,
                             dt_customer,
                             on='customer_id',
                             how='left')

    join_data = pandas.merge(join_data,
                             dt_item,
                             on='item_id',
                             how='left')

    join_data['price'] = join_data['quantity'] * join_data['item_price']
    join_data['payment_date'] = pandas.to_datetime(join_data['payment_date'])
    join_data['payment_month'] = join_data['payment_date'].dt.strftime('%Y年%m月')
    join_data['payment_day'] = join_data['payment_date'].dt.strftime('%Y年%m月%d日')
    data_num = len(join_data)

    # 月別集計データ
    monthly_sale = join_data.groupby('payment_month').sum()['price']

    annual_sale = pandas.pivot_table(join_data, index='item_name', columns='payment_month',
                                     values=['price', 'quantity'], aggfunc='sum')

    # 商品別の売上推移可視化
    graph_data = pandas.pivot_table(join_data, index='payment_month', columns='item_name', values='price',
                                    aggfunc='sum')

    fig = pyplot.figure(figsize=(10, 10), facecolor='lightblue')

    pyplot.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
    pyplot.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
    pyplot.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
    pyplot.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
    pyplot.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')

    pyplot.legend()

    pyplot.show()
    fig.savefig('processing_data/static/images/sale/graph.png')

    # 欠損値があるかをチェックします
    sum_data = join_data.isnull().values.sum()
    message = ''
    if sum_data > 0:
        message = '欠損値があります。'

    # トータルを出力
    total = join_data.describe()

    min_date = join_data['payment_day'].min()
    max_date = join_data['payment_day'].min()

    context = {
        'df': join_data,
        'data_num': data_num,
        'message': message,
        'total': total,
        'monthly_sale': monthly_sale,
        'annual_sale': annual_sale,
        'min_date': min_date,
        'max_date': max_date,
    }
    return render(request, 'processing_data/sale/sale_data.html', context)
