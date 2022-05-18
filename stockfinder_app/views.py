# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . import sele_test 
# Create your views here.
def get_home(request):
    return render(request,'home.html')

def search_stock(request):
    searched_stock = request.GET['search']
    #searched_table, searched_price= sele_test.search_stock('https://www.macrotrends.net/',searched_stock)
    #return render(request,'search_result.html',{'searched_stock':searched_stock, 'searched_table':searched_table, 'searched_price':searched_price})
    searched_summary, searched_history = sele_test.search_finance('https://finance.yahoo.com/',searched_stock)
    return render(request,'search_result.html',{'searched_stock':searched_stock, 'searched_summary':searched_summary, 'searched_history':searched_history})
