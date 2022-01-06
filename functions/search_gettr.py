"""
gg is the client
"""

def searchGG(gg,searchTerm, maxLim=50,printOut=False):
    searched = list(gg.search(searchTerm,max=maxLim))
    if(printOut):
        for item in searched:
            for x in item:
                print(str(x) + ': ' + str(item[x]))
            print('---')
            print('')

    return(searched)