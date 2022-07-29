my_filename=str(input("имя файла: ")) #ФАЙЛ
data=str.upper(input("что в файле: ")) #данные в него отправляемые
fext2='txt' # расширение файла
with open("D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Пайтон\ProjectForDiploma\\files\\" + my_filename + '.' + fext2, 'w', encoding='utf-8') as fp:# собираем то, что в файл попадет(data), +имя фйала(filename)+ расширение, открываем неа запись(w)
     print(data, file=fp, sep="\n")
\