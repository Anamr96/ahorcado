# -*- coding: utf-8 -*-
#idiota no me quiere ensenar

import random

modo_de_juego = input("¿Desea jugar contra la maquina?")
if modo_de_juego in ["si", "Si", "s", "S", "yes", "Y", "y"]:
    list = [sofa, calamar, delfin, sillon, cocina, salon, pulpo, caballo, cebra, cabra, oveja, balcon, armario, perro, gato, casa, amarillo, verde, azol, rosa, rojo, negro, blanco]
    palabra_misteriosa = input(random.list)

    for i in range(100):
        print (".")

    espacios = ""

    for letritas in palabra_misteriosa:
        espacios = espacios + "_"

    errores = 0
    ganar = False
    perder = False

    print espacios
    while not ganar and not perder:
        letra_magica = input("dame la letra magica: ")
        if letra_magica in palabra_misteriosa:
            for posicion, letra_palabra in enumerate(palabra_misteriosa):
                if letra_magica == letra_palabra:
                    espacios = list(espacios)
                    espacios[posicion] = letra_magica
                    espacios = "".join(espacios)

        else:
            errores = errores + 1
            print (espacios, "Numero de errores:", errores)

            if errores == 0:
                print(" _____________")
                print(" |            |")
                print(" |            |")
            	print(" |           ")
            	print(" |           ")
            	print(" |        ")
            	print(" |            ")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 1:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ")
            	print(" |           ")
            	print(" |           ")
            	print(" |        ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 2:
                print(" _____________")
                print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |            ||")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 3:
    	        print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 4:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 5:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |           /")
            	print(" |         _/")
            	print(" |")
            	print(" |")
            	print("----")


            if errores == 6:
                perder = True
                print ("Oh, vaya")

            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           X  X")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |           /  \ ")
            	print(" |         _/    \_")
            	print(" |")
            	print(" |")
            	print("----")


        if espacios == palabra_misteriosa:
            ganar = True
            print ("Wiiiiiii")
            print("           VVVVVVV")
            print("            O  O")
            print("              3")
            print("        ~~~~~||~~~~~")
            print("             ||")
            print("            /  \ ")
            print("          _/    \_")

else:
    palabra_misteriosa = input("dame la palabra misteriosa: ")

    for i in range(100):
        print (".")

    espacios = ""

    for letritas in palabra_misteriosa:
        espacios = espacios + "_"

    errores = 0
    ganar = False
    perder = False


    print espacios
    while not ganar and not perder:
        letra_magica = input("dame la letra magica: ")
        if letra_magica in palabra_misteriosa:
            for posicion, letra_palabra in enumerate(palabra_misteriosa):
                if letra_magica == letra_palabra:
                    espacios = list(espacios)
                    espacios[posicion] = letra_magica
                    espacios = "".join(espacios)

        else:
            errores = errores + 1
            print (espacios, "Numero de errores:", errores)

            if errores == 0:
                print(" _____________")
                print(" |            |")
                print(" |            |")
            	print(" |           ")
            	print(" |           ")
            	print(" |        ")
            	print(" |            ")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 1:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ")
            	print(" |           ")
            	print(" |           ")
            	print(" |        ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 2:
                print(" _____________")
                print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |            ||")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 3:
    	        print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 4:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |          ")
            	print(" |         ")
            	print(" |")
            	print(" |")
            	print("----")

            if errores == 5:
            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           O  O")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |           /")
            	print(" |         _/")
            	print(" |")
            	print(" |")
            	print("----")


            if errores == 6:
                perder = True
                print ("Oh, vaya")

            	print(" _____________")
            	print(" |            |")
            	print(" |            |")
            	print(" |           X  X")
            	print(" |            __")
            	print(" |        ----||----")
            	print(" |            ||")
            	print(" |           /  \ ")
            	print(" |         _/    \_")
            	print(" |")
            	print(" |")
            	print("----")


        if espacios == palabra_misteriosa:
            ganar = True
            print ("Wiiiiiii")
            print("           VVVVVVV")
            print("            O  O")
            print("              3")
            print("        ~~~~~||~~~~~")
            print("             ||")
            print("            /  \ ")
            print("          _/    \_")
