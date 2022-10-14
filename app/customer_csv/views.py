from django.shortcuts import render
from pandas import pandas as pd
from matplotlib import pyplot as plt
import japanize_matplotlib
import pathlib
import os


def index(request):
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/customer_master.csv'
    df = pd.read_csv(filePath)
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'customer_csv/index.html', context)


def get_customer_data():
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/customer_master.csv'
    df = pd.read_csv(filePath)
    return df


def item_master(request):
    df = get_customer_data()
    data_num = len(df)
    context = {
        'df': df,
        'data_num': data_num,
    }
    return render(request, 'customer_csv/index.html', context)


def get_item_data():
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/item_master.csv'
    df = pd.read_csv(filePath)
    return df


def get_transaction_data():
    transaction_1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/transaction_1.csv'
    transaction_2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/transaction_2.csv'
    df_transaction_1 = pd.read_csv(transaction_1)
    df_transaction_2 = pd.read_csv(transaction_2)
    # データをユニオンする
    return pd.concat([df_transaction_1, df_transaction_2], ignore_index=True)


def transaction(request):
    transaction = get_detail_data()
    data_num = len(transaction)
    context = {
        'df': transaction,
        'data_num': data_num,
    }
    return render(request, 'customer_csv/index.html', context)


def get_detail_data():
    transaction_detail_1 = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/transaction_detail_1.csv'
    transaction_detail_2 = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + '/customer_csv/file/transaction_detail_2.csv'
    df_detail_1 = pd.read_csv(transaction_detail_1)
    df_detail_2 = pd.read_csv(transaction_detail_2)
    # データをユニオンする
    df_details = pd.concat([df_detail_1, df_detail_2], ignore_index=True)
    return df_details


def transaction_detail(request):
    #  トランザクションデータの詳細データを取得する
    df_detail = get_detail_data()
    data_num = len(df_detail)
    context = {
        'df': df_detail,
        'data_num': data_num,
    }
    return render(request, 'customer_csv/index.html', context)


def sale_data(request):
    # トランザクションデータを取得する
    df_detail = get_detail_data()
    dt_transaction = get_transaction_data()
    dt_customer = get_customer_data()
    dt_item = get_item_data()
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
    join_data['payment_date'] = pd.to_datetime(join_data['payment_date'])
    join_data['payment_month'] = join_data['payment_date'].dt.strftime('%Y年%m月')
    join_data['payment_day'] = join_data['payment_date'].dt.strftime('%Y年%m月%d日')
    data_num = len(join_data)

    # 月別集計データ
    monthly_sale = join_data.groupby('payment_month').sum()['price']

    annual_sale = pd.pivot_table(join_data, index='item_name', columns='payment_month',
                                 values=['price', 'quantity'], aggfunc='sum')

    # 商品別の売上推移可視化
    graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')

    fig = plt.figure(figsize=(10, 10), facecolor='lightblue')

    plt.plot(list(graph_data.index), graph_data["PC-A"], label='PC-A')
    plt.plot(list(graph_data.index), graph_data["PC-B"], label='PC-B')
    plt.plot(list(graph_data.index), graph_data["PC-C"], label='PC-C')
    plt.plot(list(graph_data.index), graph_data["PC-D"], label='PC-D')
    plt.plot(list(graph_data.index), graph_data["PC-E"], label='PC-E')

    plt.legend()

    plt.show()
    fig.savefig('customer_csv/static/images/graph.png')

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
    return render(request, 'customer_csv/sale_data.html', context)
