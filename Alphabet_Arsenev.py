# Created by Arsenev
# Date 27.10.2020
# Task Description: вывести полный перебор строк от первой до второй в алфавитном порядке с сохранением длины строки

def Alphabet(FirstStr, LastStr):
    while FirstStr != LastStr:
        print(FirstStr)
        FirstStr = FirstStr[:-1] + chr(ord(FirstStr[-1]) + 1)
        if FirstStr[-1] > 'z':
            for i in range(len(FirstStr) - 1, 0, -1):
                if FirstStr[i] > 'z':
                    FirstStr = FirstStr[:i - 1] + chr(ord(FirstStr[i - 1]) + 1) + 'a' + FirstStr[i + 1:]
    print(FirstStr)