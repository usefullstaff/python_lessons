
"""
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True) - Открывает файл и возвращает соответствующий поток.

'r'	открытие на чтение (является значением по умолчанию).
'w'	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
'x'	открытие на запись, если файла не существует, иначе исключение.
'a'	открытие на дозапись, информация добавляется в конец файла.
'b'	открытие в двоичном режиме.
't'	открытие в текстовом режиме (является значением по умолчанию).
'+'	открытие на чтение и запись
"""


#такая запись сработает. только если в данной директории есть файл test.txt
file = open('test.txt')

#работает, т.к метод 'а' указывает, что файл необходимо открыть и добавить к нему запись.
# и, если файла нет, то он будет автоматически создан.
file = open('tes.txt','a')

#файл необоходимо закрыто командой close
file = open('tes.txt','a')
file.close()



#полный процесс открытия, записи и закрытия

file = open('test.txt','a')
file.write('some text')
file.close()



"""
Здесь получим ошибку, так, как записывать нужно строковый тип данных, если используются другие,
то позаботьтесь об их преобразовании. 
Скажем [file.write(x) for x in range(10) if type(x) != str x = str(x)]
"""


file = open('test.txt','a')
write_lines = [file.write(x) for x in range(10)]
file.close()


file = open('test.txt','a')
write_lines = [file.write(str(x)) for x in range(10)]
file.close()



#запись идет в тупую,  одной строкой, посимвольно
#нужно построчно - добавьте символ перехода со строки на строку
file = open('test.txt','a')
write_lines = [file.write(str(x)+'\n') for x in range(10)]
file.close()




запись обычный циклом так же работает.

file = open('test.txt','a')
for x in range(10):
	file.write(str(x)+'\n')
file.close()



#теперь поговорим о чтении из файла
#так мы выгрузим в память весь документ
file = open('test.txt','a')
file.read()


#так мы получим первый символ
file = open('test.txt','a')
file.read()
print(file.read(1))

#а вот так можно читать файл построчно
read_lines = [file.read(x) for x in range(10)]
print(read_lines)

for line in file:
	print(line)
