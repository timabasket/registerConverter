import os

directory = "D:\ОСНОВНОЕ\АКАДЕМИЯ\\4 курс\Пайтон\ProjectForDiploma\\files"
lis_dir = os.listdir(directory)

for item in lis_dir:
    if item.endswith(".txt"):
        os.remove(os.path.join(directory, item))