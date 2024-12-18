def llegir_llista_enters():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix un nombre: ")
        if a != ".":
            l.append(int(a))
    print("Llista d'enters: {}".format(l))
    return l

def llegir_llista_paraules():
    l = []
    a = "a"
    while a != ".":
        a = input("Introdueix una paraula: ")
        if a != ".":
            l.append(a)
    print("Llista de paraules: {}".format(l))
    return l

def senars_llista(llista):
    senars = [num for num in llista if num % 2 != 0]
    print("Nombres senars: {}".format(senars))
    return senars

def sumar_parells_llista(llista):
    suma_parells = sum(num for num in llista if num % 2 == 0)
    print("Suma de nombres parells: {}".format(suma_parells))
    return suma_parells

def cercar_numero_llista(llista, numero):
    if numero in llista:
        posicio = llista.index(numero)
        print("El número {} està a la posició {}".format(numero, posicio))
    else:
        print("El número {} no es troba a la llista".format(numero))

def crear_paraula_llista(llista):
    paraula = ''.join([paraula[0] for paraula in llista])
    print("Paraula creada: {}".format(paraula))
    return paraula

def crear_llista_num_aleatoris():
    import random
    llista_aleatoria = [random.randint(1, 100) for _ in range(5)]
    print("Llista de números aleatoris: {}".format(llista_aleatoria))
    return llista_aleatoria

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
    return resultat

def majors_edat(edat1, edat2):
    majors = []
    if edat1 >= 18:
        majors.append(edat1)
    if edat2 >= 18:
        majors.append(edat2)
    print("Majors d'edat: {}".format(majors))
    return majors

def menu():
    print("Opcions:")
    print("1. Llegir llista d'enters")
    print("2. Nombres senars de la llista")
    print("3. Sumar nombres parells de la llista")
    print("4. Cercar un número a la llista")
    print("5. Llegir llista de paraules")
    print("6. Crear paraula amb inicials de la llista")
    print("7. Crear llista de números aleatoris")
    print("8. Comparar llistes")
    print("9. Determinar majors d'edat")
    print("10. Sortir")

    opcio = int(input("Escull una opció (1-10): "))
    return opcio

def principal():
    while True:
        opcio = menu()
        if opcio == 1:
            llista_enters = llegir_llista_enters()
        elif opcio == 2:
            llista_enters = llegir_llista_enters()
            senars_llista(llista_enters)
        elif opcio == 3:
            llista_enters = llegir_llista_enters()
            sumar_parells_llista(llista_enters)
        elif opcio == 4:
            llista_enters = llegir_llista_enters()
            numero = int(input("Introdueix un número per cercar: "))
            cercar_numero_llista(llista_enters, numero)
        elif opcio == 5:
            llegir_llista_paraules()
        elif opcio == 6:
            llista_paraules = llegir_llista_paraules()
            crear_paraula_llista(llista_paraules)
        elif opcio == 7:
            crear_llista_num_aleatoris()
        elif opcio == 8:
            llista1 = crear_llista_num_aleatoris()
            llista2 = crear_llista_num_aleatoris()
            comparar_llistes(llista1, llista2)
        elif opcio == 9:
            edat1 = int(input("Introdueix la primera edat: "))
            edat2 = int(input("Introdueix la segona edat: "))
            majors_edat(edat1, edat2)
        elif opcio == 10:
            print("Sortint del programa. Adéu!")
            break
        else:
            print("Opció no vàlida. Si us plau, tria una opció del 1 al 10.")

if __name__ == "__main__":
    principal()
