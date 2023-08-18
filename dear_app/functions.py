# funciones basicas
def separate(chart):
    '''Funcion que tiene como unico objetivo separar o dividir la cadena que se le pase como parametro (chart), 
    el cual se espera como un dato de tipo string, para poder manipularlo bien, el cual, como tal esperara 
    una cadena de tipo numerica, por ejemplo: "654654654654" 
    Con N cantidad de numeros, el punto esta en que al final, esta funcion lo que debe retornar será una 
    cadena_total, tambien de tipo string, donde, una vez ya procesado el parametro que se le paso al inicio, 
    (654654654654), debe retornar lo siguiente: "654 654 654 654"
    solo por decir un ejemplo, cabe aclarar! :) :> ;> ;):
    ejemplo mas claro:
    # llamamos a separate:
    separate(str(564745)) // y retornará un: "564 745"  
    '''
    cont = 0
    strings = []
    letters = []
    for letter in chart:
        cont += 1
        letters.append(letter)
        
        if cont == 3:
            cont = 0
            strings.append(letters)
            letters = []
    new_letters = []
    for i in range(cont):
        new_letters.append(chart[-1*(i+1)])
    strings.append(new_letters)
            
    cadena_total = ''
    for chart in strings:
        for l in chart:
            cadena_total += l
        cadena_total += ' '
            
    return cadena_total
