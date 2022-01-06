from gogettr import PublicClient

gg = PublicClient()


from functions.get_trends import *

trends = getTrends(gg,printOut=True)