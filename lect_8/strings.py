
string = 'some string'

len(string)
#print(len(string))


string[0]
#print(string[0])


string[-1]
#print(string[-1])

string[3:6]
#print(string[3:6])

for x in string:
	print(x)


string[2]='2'
#ошибка, так, как это неизменяемый тип, а мы не создаем новую строку. а пытаемся заменить элемент


another_str = 'some another text'

new = string+another_str
#print(new)



"""
ФУНКЦИИ СТРОКИ
Так, как str это объект, то он имеет и свои методы (функции)
"""

#S.find(str, [start],[end])	Поиск подстроки в строке. 
#Возвращает номер первого вхождения или -1

new.find('so')

#print(new.find('so'))




#S.rfind(str, [start],[end])	Поиск подстроки в строке. 
#Возвращает номер последнего вхождения или -1
new.rfind('so')

#print(new.rfind('so'))




#S.index(str, [start],[end])	Поиск подстроки в строке. 
#Возвращает номер первого вхождения или вызывает ValueError

new.index('so')
#print(new.index('so'))


#S.rindex(str, [start],[end])	Поиск подстроки в строке. 
#Возвращает номер последнего вхождения или вызывает ValueError

new.rindex('so')
#print(new.rindex('so'))


#S.replace(шаблон, замена) Заменяет заданный символ во всей строке на указанный	
new.replace('so',  'new templ')

new_str = 'change-some-symbols'
new_str.replace('-','')
#print(new_str.replace('-',''))


new_str = 'change,some,symbols'
new_str.replace(',', " ")
#print(new_str.replace(',', " "))


new_str = 'change,some,symbols-and:another;tt'
new_str.replace(';','_______')
#print(new_str.replace(';','_______'))



#S.split(символ) разбиение строки на список по символу

new_str = 'change-some-symbols'
new_str.split('-',)
#print(new_str.split('-',))

new_str = 'change,some,symbols'
new_str.split(',',)
#print(new_str.split(',',))

new_str = 'change,some,symbols-and:another;tt'
new_str.split(';')
#print(new_str.split(';'))


long_str = """
Вот так можно писать довольно объемный текст
на несколько строчек. Скажем, запросы к БД или еще что
"""
#print(long_str)

select_obj_in_squad = """ 
SELECT * FROM obj_locations
WHERE obj_lat BETWEEN {:f} AND {:f}
AND obj_lon BETWEEN {:f} AND {:f};
"""

#ФОРМАТИРОВАНИЕ СТРОК