
def llegir_llista_enters():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nombre: ")
        if a!=".":
            l.append(a)
    print(l)
llegir_llista_enters()

def llegir_llista_enters():
    l=[]
    a="a"
    while a!=".":
        a=input("Introdueix un nombre: ")
        if a!=".":
               l.append(a)
        print(l)

def llegir_llista_enters():
    llista = []
    while True:
        entrada = input("Introdueix un nombre (o '.' per acabar): ")
        if entrada == ".":
            break
        else:
            llista.append(int(entrada))
    print("Llista d'enters: {}".format(llista))

def senars_llista(llista):
    senars = [num for num in llista if num % 2 != 0]
    print("Nombres senars: {}".format(senars))

def sumar_parells_llista(llista):
    suma_parells = sum(num for num in llista if num % 2 == 0)
    print("Suma de nombres parells: {}".format(suma_parells))

def cercar_numero_llista(llista, numero):
    if numero in llista:
        posicio = llista.index(numero)
        print("El número {} està a la posició {}".format(numero, posicio))
    else:
        print("El número {} no es troba a la llista".format(numero))

def llegir_llista_paraules():
    llista = []
    while True:
        entrada = input("Introdueix una paraula (o '.' per acabar): ")
        if entrada == ".":
            break
        else:
            llista.append(entrada)
    print("Llista de paraules: {}".format(llista))

def crear_paraula_llista(llista):
    paraula = ''.join([paraula[0] for paraula in llista])
    print("Paraula creada: {}".format(paraula))

def crear_llista_num_aleatoris():
    import random
    llista_aleatoria = [random.randint(1, 100) for _ in range(5)]
    print("Llista de números aleatoris: {}".format(llista_aleatoria))

def comparar_llistes(llista1, llista2):
    resultat = []
    for i in range(5):
        if llista2[i] not in llista1:
            resultat.append(0)
        elif llista2[i] == llista1[i]:
            resultat.append(2)
        else:
            resultat.append(1)
    print("Comparació de llistes: {}".format(resultat))

def majors_edat(edat1, edat2):
    majors = []
    if edat1 >= 18:
        majors.append(edat1)
    if edat2 >= 18:
        majors.append(edat2)
    print("Majors d'edat: {}".format(majors))
