list_a = [[1,4,3,2,1,2],['a','b','d','e','r','q']]

for index, sublist in enumerate(list_a):
    try:
        print(sublist.index('a'))
        print(f"It was in list {index}")
    except:
        'No A'


