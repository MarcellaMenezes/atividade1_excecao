
try:
    file = open('file.txt', "r")
    file_line = file.readline()
    file.close()
except FileNotFoundError:
    print("Diretório não encontrado. Entre em contato com o desenvolvedor!")
