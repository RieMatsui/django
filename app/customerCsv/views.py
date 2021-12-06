from django.shortcuts import render
from pandas import pandas as pd
import csv
import os

from django.http import HttpResponse

def index(request):
    global line
    filePath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/customerCsv/file/customer_master.csv'
    df = pd.read_csv(filePath, index_col=0)
    context = {
            'df': df,
    }
    return render(request, 'customerCsv/index.html', context)
