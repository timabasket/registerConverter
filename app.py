import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x200")
root.title('Конвектор регистров')
root.resizable(width=False, height=False)


def delete_file():
    directory = "D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Пайтон\ProjectForDiploma\\files"
    lis_dir = os.listdir(directory)

    for item in lis_dir:
        if item.endswith(".txt"):
            os.remove(os.path.join(directory, item))
    messagebox.showinfo("Сообщение", 'Файл удалён!')


def convertor():
    my_filename = file_name.get()
    data = str.upper(message.get())
    s = ''
    if my_filename.__eq__(s) or data.__eq__(s):
        messagebox.showinfo("Сообщение", "Заполните поля информацией")
    else:

        fext2 = 'txt'  # расширение файла
        with open("D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Пайтон\ProjectForDiploma\\files\\" + my_filename + '.' + fext2, 'w',
                  encoding='utf-8') as fp:  # собираем то, что в файл попадет(data), +имя фйала(filename)+ расширение, открываем неа запись(w)
            print(data, file=fp, sep="\n")
        messagebox.showinfo("Сообщение", 'Файл готов!')

Label(text="Введите имя файла: ").grid(row=0, column=0,
                        sticky=W,
                        pady=10, padx=10)
Label(text="Введите ваш текст: ").grid(
    row=1, column=0, sticky=W,
    padx=10, pady=10)

file_name = StringVar() #переменная для получения пользовательского текста
filename_entry = Entry(textvariable=file_name, width=50)
filename_entry.grid(row=0, column=1,
                columnspan=3,
                sticky=W+E, padx=10)

message = StringVar() #переменная для получения пользовательского текста
message_entry = Entry(textvariable=message, width=50)
message_entry.grid(row=1, column=1,
                columnspan=3,
                sticky=W+E, padx=10)

Button(text="Конвертировать",
       command=convertor).grid(row=2, column=0)
Button(text="Удалить файл",
       command=delete_file).grid(row=2, column=1)

root.mainloop()

