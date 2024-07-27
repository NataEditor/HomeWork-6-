myDict = {'En' : 12 , 'Max' : 11 , 'Helga' : 10 , 'Ven' : 12}
print(myDict)
print(myDict['Max'], 'лет')
print(myDict.get('olga' , 'Такого чловека нет'))
myDict['En'] = 8
print(myDict)
myDict.update({'Nata' : 8 , 'Alen' : 12})
B = myDict.pop('Helga')
print(B)
B = myDict.pop('Ven')
print(myDict)

my_set = {1, 3, 2, 22, 2, 33, 3, 'Name', False }
my_set.add(77)
print(my_set)
my_set.add(9)
print(my_set)
my_set.discard(False)
print(my_set)