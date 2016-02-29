import timeit

def search_fast(findThis, myList):
    for item in myList:
        if item == findThis:
            return True
    return False

def search_slow(findThis, myList):
    return_value = False
    for item in myList:
        if item == findThis:
            return_value = True    
    return return_value
    
terje = []
for i in range(1000):
    terje.append(i)

print('search_slow')   
print(min(timeit.repeat("search_slow(70, terje)", setup="from __main__ import search_slow, terje", number=100000)))
print('search_fast')
print(min(timeit.repeat("search_fast(70, terje)", setup="from __main__ import search_fast, terje", number=100000)))



    

    

        
        