#1) работа со словарём

my_dict={'Camry':4800000, 'Rav4':4500000, 'Prado':6500000, 'Land Cruiser':12000000}
print(my_dict)
print(my_dict.get('Camry')) #получим значение сущетвую-го ключа
print(my_dict.get('Highlander')) #получим значение не сущетвую-го ключа
my_dict.update({'Corolla':2500000,
                'Hilux':5000000}) #добавим сразу 2 ключа со своими значениями
del my_dict['Camry'] #удалим ключ
#print(my_dict['Camry']) при выводе удалённого ключа мы получим ошибку(KeyError)
print(my_dict) #выведем изменённый словарь

#2) работа с множествами

my_set={12, True, 'Three', 5, 5}
print(my_set)
my_set.add(6) #добавим элемент множества
my_set.add(233) #добавим элемент множества
print(my_set) #выведем получившееся множество
my_set.discard(5) #удалим один элемент множества
print(my_set) #выведем изменённое множество