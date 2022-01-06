# -----Imports and setup 

from gogettr import PublicClient

# API client
gg = PublicClient()

from functions.get_trends import *
from functions.wordCloud import *



print('Getting Trends: ')
trends = getTrends(gg,printOut=True)

print('Generating Word Cloud: ')
make_wordCloud(trends, 'report/wordCloud.png')

print('***Analytics Complete****')