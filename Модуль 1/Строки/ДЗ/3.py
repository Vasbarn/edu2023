filename = input("Введите название файла: ")
starter = ('@', '№', '$', '%', '^', '&', '*', '()')
end = (".txt",'.docx')
if filename.startswith(starter)==False and filename.endswith(end)==True:
    print(filename)