"""
gg is the client
"""
def getTrends(gg,maxLim=50,printOut=False,returnArray=False):
    trending = list(gg.trends(max=maxLim))
    trendArray = []
    for trend in trending:
        if('ttl' in trend.keys()):
            trendArray.append(trend['ttl'])
    trends = list(dict.fromkeys(trendArray))
    trendString = ""
    if(printOut):
        for t in trends:
            print(t + '\n')
            trendString += t + '\n'
    if(returnArray):
        return(trends)
    return(trendString)
