#▓▓▓▓▓▓
#▒▒▒▒▒▓▓
#▒▒▒▒▒▒▒▓
#▒▒▒▒▒▒▒▒▓
#▒▒▒▒▒▒▒▒▓
#▒▒▒▒▒▒▒▒▒▓
#▒▒▒▒▒▒▒▒▒▓▓▓
#▒▒▒▓▓▓▓▓▓░░░▓
#▒▒▒▓░░░░▓░░░░▓
#▒▒▓░░░░░░▓░▓░▓
#▒▒▓░░░░░░▓░░░▓
#▒▒▓░░▓░░░▓▓▓▓
#▒▒▒▓░░░░▓▒▒▒▒▓
#▒▒▒▒▓▓▓▓▒▒▒▒▒▓
#▒▒▒▒▒▒▒▒▒▒▓▓▓▓
#▒▒▒▒▒▒▒▓▓▓▒▒▒▒▓
#▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▓
#▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▓
#▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▓
#▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒▓
#▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓
#▒▒▒▓▒▒▒▒▒▒▒▓
#▒▒▒▒▓▒▒▒▒▒▓

import random

print("Bienvenido al mundo del blackjack digital")
print("Es como el blackjack pero digital")
print("ingresa cuando dinero quieres depositar")
DA = int(input("Ingresa la cantidad de dinero en numeros: "))
print(f"Ingresaste {DA} pesos, estas seguro?")
input()
print("No importa ya esta depositado")
DU = 0
while DA >= 0:
    AV = False
    while AV != True:
        print(f"Te quedan {DA} Pesos y tienes una deuda de {DU} pesos")
        print("Cuanto quieres apostar?")
        AC = int(input())
        if AC > DA:
            print("No tienes el dinero suficiente para apostar esa cantidad, intentalo de nuevo")
        else:
            AV = True
        print(f"Tu apuesta es de {AC} pesos, ¿estas seguro?")
        input()
        print("Muy tarde para arrepentirse")
        C1 = random.randint(0, 13)
        if C1 == 0:
            C1 = "joker"
        elif C1 == 1:
            C1 = "A"
        elif C1 == 11:
            C1 = "J"
        elif C1 == 12:
            C1 = "Q"
        elif C1 == 13:
            C1 = "K"
        C2 = random.randint(0, 13)
        if C2 == 0:
            C2 = "joker"
        elif C2 == 1:
            C2 = "A"
        elif C2 == 11:
            C2 = "J"
        elif C2 == 12:
            C2 = "Q"
        elif C2 == 13:
            C2 = "K"
        print(f"tus cartas son {C1} y {C2}")
        if C1 == "A" and C2 == "K":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "A" and C2 == "Q":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "A" and C2 == "J":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "A" and C2 == "joker":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "K" and C2 == "A":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "Q" and C2 == "A":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "J" and C2 == "A":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "joker" and C2 == "A":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "joker" and C2 == "joker":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "joker" and C2 == "J":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "joker" and C2 == "Q":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "joker" and C2 == "K":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "J" and C2 == "joker":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "Q" and C2 == "joker":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        elif C1 == "K" and C2 == "joker":
            AC = AC * 2
            DA += AC
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        else:
            if C1 == "joker":
                V1 = 10
            elif C1 == "A":
                V1 = 1
            elif C1 == "J":
                V1 = 10
            elif C1 == "Q":
                V1 = 10
            elif C1 == "K":
                V1 = 10
            else:
                V1 = C1
            if C2 == "joker":
                V2 = 10
            elif C2 == "A":
                V2 = 1
            elif C2 == "J":
                V2 = 10
            elif C2 == "Q":
                V2 = 10
            elif C2 == "K":
                V2 = 10
            else:
                V2 = C2
            VM = []
            VM = VM + [V1]
            VM = VM + [V2]
            VA = 0
            C1D = random.randint(1,13)
            if C1D == 0:
                C1D = "joker"
                V1D = 1
            elif C1D == 1:
                C1D = "A"
                V1D = 1
            elif C1D == 11:
                C1D = "J"
                V1D = 10
            elif C1D == 12:
                C1D = "Q"
                V1D = 10
            elif C1D == 13:
                C1D = "K"
                V1D = 10
            else:
                V1D = C1D
            print(f"La primera carta de la casa es {C1D}, su segunda carta se mantiene oculta")
            while VA <= 21:
                VA = 0
                CC = len(VM)
                for i in range(0,CC):
                    VA += VM[i]
                print(f"El valor de tus cartas es de {VA}, ¿Quieres quedarte o robar?")
                print("Escribe textualmente: me quedo o robo")
                Is = input("me quedo / robo: ")
                if Is == "robo":
                    C = random.randint(1, 13)
                    if C == 0:
                        print("Te salio un Joker")
                        VM = VM + [1]
                        VA += 1
                    elif C == 1:
                        print("Te salio una A")
                        VM += VM + [1]
                        VA += C
                    elif C == 11:
                        print("Te salio una J")
                        VM = VM + [10]
                        VA += 10
                    elif C == 12:
                        print("Te salio una Q")
                        VM = VM + [10]
                        VA += 10
                    elif C1 == 13:
                        print("Te salio una K")
                        VM = VM + [10]
                        VA += 10
                    else:
                        print(f"Te salio un {C}")
                        VM = VM + [C]
                        VA += C
                elif Is == "me quedo":
                    print(f"Te quedas con {VA}")
                    break
            print(f"El valor de tus cartas es de {VA}")
            if VA > 21:
                print(f"Perdiste, tus puntos son de {VA}, pasandote por {VA-21} puntos!!!")
                DA -= AC
                print(F"pierdes {AC} pesos, quedando con {DA}")
                print("⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜")
                print("⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜")
                print("⬜⬜⬜⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬜⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬜⬛⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬜⬜⬜⬜")
                print("⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜")
                print("⬜⬜⬛🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦⬛⬜⬜")
                print("⬜⬛⬛🟦⬛🏻🏻⬛⬜⬜⬜⬛⬜⬜⬜⬛🏻🏻⬛🟦⬛⬛⬜")
                print("⬜⬛🟦🟦🟦⬛🏻🏻⬛⬛⬛⬜⬛⬛⬛🏻🏻⬛🟦🟦🟦⬛⬜")
                print("⬛🟦🟦⬛⬛🟦⬛⬛⬛⬜⬜⬛⬜⬜⬛⬛⬛🟦⬛⬛🟦🟦⬛")
                print("⬛🟦🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜⬛🟦🟦⬛🟦🟦🟦🟦⬛")
                print("⬛🟦🟦🟦🟦🟦⬛🟦⬛⬛⬜⬜⬜⬛⬛🟦⬛🟦🟦🟦🟦🟦⬛")
                print("⬜⬛🟦🟦🟦⬛🟦🟦⬛⬜⬜⬜⬜⬜⬛🟦🟦⬛🟦🟦🟦⬛⬜")
                print("⬜⬜⬛⬛🟦⬛🟦🟦⬛⬛⬛⬛⬛⬛⬛🟦🟦⬛🟦⬛⬛⬜⬜")
                print("⬜⬜⬜⬛⬛⬛🟦🟦⬛⬛⬛⬛⬛⬛⬛🟦🟦⬛⬛⬛⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜")
                print("⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜")
                print("⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜")
                print("⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜")
                print("⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜")
                print("⬜⬜⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜")
                print("⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜")
                if DA == 0:
                    print(F"Te quedaste sin dinero eeeeeeeee, ¿Quieres que te preste?")
                    RE = input("si / no  :")
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input())
                        if DP > 0:
                            DA += DP
                            DU += DP
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU} pesos conmigo")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("Pobreeeeeeee")
                        else:
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                elif DA < 0:
                    DU += DA
                    print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                    print("¿Quieres que te presteeeeee?")
                    RE = input("si / no  :")
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input())
                        if DP > 0:
                            DA += DP
                            DU += DP
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU} pesos conmigo")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("Pobreeeeeeeeeee")
                            break
                        else:
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print(f"Te quedaste sin dinero y con una deuda de {DU}")
                        break
            else:
                print(F"TURNO DE LA CASA")
                print(F"La primera carta de la casa es {C1D}")
                C2D = random.randint(0, 13)
                if C2D == 1:
                    C2D = "A"
                    V2D = 1
                elif C2D == 11:
                    C2D = "J"
                    V2D = 10
                elif C2D == 12:
                    C2D = "Q" 
                    V2D = 10
                elif C2D == 13:
                    C2D = "K"
                    V2D = 10
                elif C2D == 0:
                    C2D = "Joker"
                    V2D = 1
                else:
                    V2D = C2D
                print(f"La segunda carta de la casa es {C2D}")
                VMD = []
                VMD = VMD + [V1D]
                VMD = VMD + [V2D]
                VMA = V1D + V2D
                if C1D == "A" and C2D == "K":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "A" and C2D == "Q":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "A" and C2D == "J":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "A" and C2D == "joker":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "K" and C2D == "A":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "Q" and C2D == "A":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "J" and C2D == "A":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "joker" and C2D == "A":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "joker" and C2D == "joker":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "joker" and C2D == "J":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "joker" and C2D == "Q":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "joker" and C2D == "K":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "J" and C2D == "joker":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "Q" and C2D == "joker":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                elif C1D == "K" and C2D == "joker":
                    DA -= AC
                    print("Blackjack de la casa, DERROTA APLASTANTE!!!")
                    print(f"Pierdes {AC}, Tu dinero actual es de {DA}")
                else:
                    print(F"El valor del maso de la casa es de {VMA}")
                    while VMA > 21 and VMA >= VA:
                        VMA = 0
                        R = len(VMD)
                        for e in range(0,R):
                            VMA += VMD[e]
                        CND = random.randint(0,13)
                        if CND == 0:
                            VMD = VMD + [1]
                            VMA += 1
                            print(f"La nueva carta de la casa es un JOKER, valor actual de las cartas {VMA}")
                        elif CND == 1:
                            VMD = VMD + [1]
                            VMA += 1
                            print(f"La nueva carta de la casa es una A, valor actual de las cartas {VMA}")
                        elif CND == 11:
                            VMD = VMD + [10]
                            VMA += 10
                            print(f"La nueva carta de la casa es una J, valor actual de las cartas {VMA}")
                        elif CND == 12:
                            VMD = VMD + [10]
                            VMA += 10
                            print(f"La nueva carta de la casa es una Q, valor actual de las cartas {VMA}")
                        elif CND == 13:
                            VMD = VMD + [10]
                            VMA += 10
                            print(f"La nueva carta de la casa es una K, valor actual de las cartas {VMA}")
                    if VMA > 21:
                        print(f"La casa pierde con {VMA} puntos, pasandose por {VMA-21} puntos")
                        AC = AC * 2
                        DA += AC
                        print(F"Ganaste con {VA} puntos")
                        print(F"Ganas {AC}!!! Quedando con {DA} pesos")
                    elif VMA > VA:
                        print(f"La casa gana con {VMA} puntos, pasandote por {VMA-VA} puntos")
                        print(F"Perdiste con {VA} puntos")
                        DA -= AC
                        print(F"Pierdes {AC}!!! Quedando con {DA} pesos")
                    elif VMA < VA:
                        print(f"La casa pierde con {VMA} puntos, la pasaste por {VA-VMA} puntos")
                        print(F"Ganaste con {VA} puntos")
                        AC = AC * 2
                        DA += AC
                        print(F"Ganas {AC}!!! Quedando con {DA} pesos")
                    elif VA == VMA:
                        print(f"La casa empata con {VA} puntos, se devuelve el dinero")
                        print(F"Empataron con {VA} puntos")
                        print(F"No ganas nada, Quedando con {DA} pesos")
                if DA == 0:
                    print(F"Te quedaste sin dinero, ¿Quieres pedir un prestamo?")
                    RE = input("si / no  :")
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input())
                        if DP > 0:
                            DA += DP
                            DU += DP
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU}")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("Pobre")
                        else:
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print(f"Te quedaste sin dinero y con una deuda de {DU}")
                elif DA < 0:
                    DU += DA
                    print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                    print("¿Quieres un prestamo?")
                    RE = input("si / no  :")
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input())
                        if DP > 0:
                            DA += DP
                            DU += DP
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU}")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("Pobre")
                            break
                        else:
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print(f"Te quedaste sin dinero y con una deuda de {DU}")
                        break