
try: 
    import mathmatics

    print(math.sqrt(25))

except ModuleNotFoundError as error:
    print('Importação inválida!', error)

#Resposta:
# A exceção foi de ModuleNotFound Error, pois não foi encontrada a biblioteca mathmatics