file = open('file.txt', "w")
    
try:
    file.write("Exemplo de texto.")
except IOError:
    print("Não foi possível escrever no arquivo.")
finally:
    file.close
