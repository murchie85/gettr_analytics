"""
gg is the client
"""
searchTerm = 'Crypto'
resultList = list(gg.search(searchTerm,max=50)) 

def searchGG(gg,searchTerm, maxLim=50,printOut=False):
    searched = list(gg.search(searchTerm,max=maxLim))
    sArray = []
    if(printOut):
        for item in sArray:
            for x in item:
                print(str(x) + ': ' + str(item[x]))
            print('---')
            print('')

    return(sArray)