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
print("")
print("¿Conoces las Reglas?")
P1 = str(input(": "))
P1 = P1.lower()
if P1 == "si":
    print("QUE INICIEN LAS APUESTAS")
else:
    print("El blackjack es un juego para apostar en el cual el objetivo es tener mas puntos que la casa sin pasarse del limite (21)0.")
    print("Estos puntos se obtienen con las cartas, las cuales inicialmente te dan 2")
    print("El valor de las cartas es igual al numero a escepcion de las que tienen letras los cuales son los siguientes:")
    print("El valor de A = 1")
    print("El valor de J = 10")
    print("El valor de Q = 10")
    print("El valor de K = 10")
    print("El valor de JOKER = 1 o 10")
    print("")
    print("Los puntos tienen un limite siendo 21, si te pasas de este limite pierdes automaticamente")
    print("Tu inicias pudiendo realizar 3 acciones:")
    print("Puedes robar para obtener una nueva carta, aumentando tu puntaje")
    print("Puedes quedarte con tu puntaje actual finalizando tu turno")
    print("Finalmente puedes aumentar tu apuesta")
    print("Puedes ganar automaticamente mediante un blackjack")
    print("El blackjack se obtiene al juntar una A con J, Q o K (el JOKER puede remplazar la A o la Letra)")
    print("")
    print("Suerte")
    print("______________________________ฅ^•ﻌ•^ฅ________________________________________________________________________")
print("")
print("Para empezar: Ingresa cuando dinero quieres depositar")
DA = int(input("Dinero Ingresado: "))
print
print(f"Ingresaste {DA} pesos, estas seguro?")
input()
print("No importa ya esta depositado")
print("")
DU = 0
while DA >= 0:
    AV = False
    while AV != True:
        if DA > 0 and DU != 0:
            if DU == 1:
                DU -= 1
                DUS = 1
                DA -= 1
            else:
                DUS = DU // 2
                DA -= DUS
            print(f"Se te retira {DUS} pesos para saldar tu deuda")
        if DU > 0:
            print(f"Te quedan {DA} Pesos y tienes una deuda de {DU} pesos")
        print("__________________________________________________________________________")
        print("")
        print("Cuanto quieres apostar?")
        AC = int(input())
        if AC > DA:
            print("No tienes el dinero suficiente para apostar esa cantidad, intentalo de nuevo")
        elif AC == 0:
            print("¿Quieres dejar de apostar?")
            RES = input("si / no: ")
            if RES == "si":
                if DU > 0:
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⣀⣤⠖⠛⠉⠉⠛⠀⠀⠀⠸⠉⠛⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⣠⠔⠋⡀⠀⠀⠐⠟⠂⠀⠀⠚⠃⠀⠀⢦⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⢠⠞⠃⠀⠚⠃⢀⣠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣰⠏⢀⡄⠀⡠⠊⠁⣀⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⠀⠉⠀⠈⢁⠔⠋⠁⢀⣀⣤⠤⠴⠶⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⡏⣠⡀⠀⠰⠃⢀⣴⣚⣉⡴⠋⠙⠓⢦⡀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⡤⠤⢦")
                    print("⣇⠉⠀⠀⠀⡴⡿⠋⠉⠹⡇⠀⠀⠀⠀⣿⣤⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⡼")
                    print("⠹⡄⠀⠀⠘⢱⡇⠀⠀⣀⣿⡷⢺⣯⠉⠉⢹⡀⠐⣾⣅⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⢀⣀⡀⣠⠞⠁")
                    print("⠀⠙⢦⣀⠀⠀⣷⠿⣾⡅⠀⢧⠈⢿⣧⡀⠈⡇⠐⠊⣉⣁⣈⣙⣦⠀⠀⠀⠀⠀⢀⣀⡠⠴⠚⢩⠀⠀⠀⠀⠀⢀⣤⣤⣿⠿⠛⠁⠀⠀")
                    print("⠀⠀⠀⠈⠉⠙⠻⡄⠹⣿⣄⡼⠱⢄⣙⣁⣜⣡⠔⠋⠉⠀⠀⠈⠉⠙⠓⠲⢶⠚⠉⠁⠀⢀⣀⡬⠴⠒⠋⠙⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠛⣦⣌⣻⡇⠀⠀⣹⠾⠻⣀⣤⣀⡀⠀⣤⣄⡀⢀⣀⣠⡾⠶⠒⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⣸⣀⡤⠊⠁⠀⡴⣟⢿⡟⠛⠶⠿⠿⠖⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⣿⠀⠔⣩⠜⠁⠀⠀⡠⠊⠀⠘⣎⣧⠀⣀⣀⡤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠘⢲⠞⠁⠀⠀⡠⠊⠀⠀⠀⠀⡿⠉⠈⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⢰⢃⠀⠀⢀⠜⠓⠤⣄⣀⣤⠞⠁⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠘⠷⣶⣾⣥⠤⠶⠚⠉⠀⢿⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⣀⣠⣤⣤⣀⣀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠁⠀⠀⠀⠀⠉⠙⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print(f"Sales de Casino Virtual con {DA} pesos y una deuda de {DU}")
                    exit()
                else:
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠤⠤⠤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⡀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠰⡜⢠⠂⠀⠀⠀⣧⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⡀⠀⡇⣎⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠹⡄⠀⢠⡤⠴⠚⢧⡀⠁⣮⣴⣦⣀⡀⢠⠟⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠈⠶⢸⡋⠹⠿⢋⡇⠀⢿⡛⢿⣿⣷⡇⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⡞⠀⠀⠀⠀⠈⢉⠩⠟⠀⠀⠀⡿⠮⠉⠀⠙⡆⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⠀⢧⡀⠀⠀⠀⠀⠀⢀⡤⠀⠀⠀⡇⠀⠀⢀⡼⠁⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠉⢹⠒⠢⢤⠀⢀⣾⢶⣆⠀⠀⣿⠀⡴⠋⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⠀⠀⢸⠀⡜⠀⠀⣠⣍⣭⡈⡆⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡤⢤⠏⠀⠀⣸⠀⠀⠀⠀⠃⠰⣯⠴⠧⢾⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⣀⣤⠴⠒⠋⠉⠁⢰⠋⠀⠋⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⢲⠒⠚⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀⠢⠤⡀⠀⠙⣆⠀⠀⠀⠀⠀⠀")
                    print("⣞⣁⣤⣄⣀⣀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⣀⠀⠀⠀⠀⠀⠀⣁⢀⣀⡼⣦⡀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠸⡄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⡶⠀⠐⠚⢹⠍⠀⠀⠈⠋⠳⣄⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠄⠀⠙⢆⢓⡇⡠⡀⠀⠀⠀⠀⠀⠀⢚⡁⠀⠀⣠⣎⠀⠀⠀⠀⠀⠀⠹⢷⡀")
                    print(f"Sales de Casino Virtual con {DA} pesos")
                    exit()
            else:
                print("De vuelta al juego")
        else:
            AV = True
        print(f"Tu apuesta es de {AC} pesos, ¿estas seguro?")
        input()
        print("Muy tarde para arrepentirse")
        print("____________________________________________________________________")
        C1 = random.randint(0, 13)
        if C1 == 0:
            C1 = "JOKER"
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
            C2 = "JOKER"
        elif C2 == 1:
            C2 = "A"
        elif C2 == 11:
            C2 = "J"
        elif C2 == 12:
            C2 = "Q"
        elif C2 == 13:
            C2 = "K"
        print("")
        print(f"tus cartas son {C1} y {C2}")
        CBJ1 = ["JOKER", "A"]
        CBJ2 = ["JOKER", "J", "Q", "K"]
        JBJ = False
        for i in range(0,2):
            C1BJ = CBJ1[i]
            for e in range(0,4):
                C2BJ = CBJ2[e]
                if C1 == C1BJ and C2 == C2BJ:
                    JBJ = True
                elif C1 == C2BJ and C2 == C1BJ:
                    JBJ = True
        if JBJ == True:
            AC = AC * 2
            DA += AC
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣾⣿⣿⣿⣿⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣌⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⢀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠋⠉⠻⠋⡉⠉⠅⠹⠉⠙⠩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠠⠤⠄⠙⠹⡶⣦⠀⢰⠀⣯⠈⣿⣿⢿⣿⣿⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠙⠛⠿⣿⣿⣄⡀⠀⢀⣤⣴⣶⣤⣤⣤⣴⣿⢹⣶⣾⣶⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⡙⡟⠻⢿⣿⣿⡷⣿⣿⣿⠟⣿⠛⣿⣿⣿⡟⣿⣿⣿⡿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣴⣷⣧⠀⠘⡈⡿⠀⠙⠛⠉⣸⠏⠀⢿⣿⣿⣧⡨⡿⠋⢠⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣇⢸⡄⠀⠙⠳⠤⣤⣤⠶⡋⠀⠀⠘⣿⣿⣟⠳⣶⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣮⣿⣷⠂⠀⠀⠀⠀⣰⠟⣤⣤⣤⣰⣿⣿⣿⣷⣸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⠀⠈⠃⢀⣰⣷⣶⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡀⡏⠸⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⢻⣷⠀⢻⣿⣿⡉⢀⣠⣤⣤⣼⣿⣿⣿⣿⡏⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀")
            print("⠀⠀⠀⠀⠀⠀⠀⠐⢂⣴⣿⣿⣿⣿⠀⠙⢧⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠿⠿⠿⠟⢻⠛⠛⠛⠛⠋⠈⠀⠀")
            print("⣈⣅⣀⣤⣬⣤⣬⣽⣿⣿⣿⣿⣿⣿⣆⠀⠀⠹⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⡆⣾⣥⣴⣆⡹⣷⠂⣠⡍⠀⠀⠀⠀⢠")
            print("⠾⠿⣼⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿⢿⣿⡀⢀⣴⣿⣿⣿⣿⣄⠀⠄⢠⣈")
            print("⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⣸⣿⣿⣿⣿⣿⠟⢰⣿⣿⣿⣸⣿⣿⣿⣿⣿⠻⣿⣿⣿⣴⣶⡀⠀")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣴⣿⣿⣇⣽⣿⡏⢀⣾⣿⣿⣿⡽⣿⣿⣿⣿⣿⣿⣧⣽⣿⣿⣿⣿⠆")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣄")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
            print("Blackjack!!!, tu ganas")
            print(f"Ganaste {AC}, Tu dinero actual es de {DA}")
        else:
            if C1 == "JOKER":
                print("Que valor quieres que tome el JOKER")
                J = input("1 o 10: ")
                if J == "10":
                    V1 = 10
                else:
                    V1 = 1
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
            if C2 == "JOKER":
                print("Que valor quieres que tome el JOKER")
                J = input("1 o 10: ")
                if J == "10":
                    V2 = 10
                else:
                    V2 = 1
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
                C1D = "JOKER"
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
            if DA > (AC * 2):
                print("")
                print("¿Quieres Duplicar tu apuesta?")
                AP = input("si / no : ")
                AP = AP.lower()
                if AP == "no":
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⢟⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣠⣾⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣼⣿⢁⣿⣿⣿⣿⣿⢀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢘⣿⣿⣿⣿⣿⣿⣿⣿⠀⢡⠀⠀⠀")
                    print("⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢈⣿⣿⣿⣿⣿⣿⣿⣿⠀⣎⠆⠀⠀")
                    print("⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣷⢸⡰⠇⠀⠀")
                    print("⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡳⠁⠀⠀")
                    print("⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣸⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣯⢳⠁⠀⠀")
                    print("⡐⠁⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⣸⣿⣿⣿⣿⣿⣿⣧⡙⣿⣿⣿⣇⠃⠀⠀")
                    print("⠙⠲⢦⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠻⠟⠫⠩⠍⠀⣰⠾⢹⣿⣿⣛⣛⣻⣿⣿⣌⠻⣷⣏⠆⠀⠀")
                    print("⠀⠐⡈⣯⢴⠾⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠁⡀⢀⣠⣤⣦⣴⣤⡀⣠⣼⣦⠟⣠⡾⠟⠋⢉⠉⠉⠉⠉⠁⣘⢻⡇⠀⠀")
                    print("⠀⠀⢡⣷⢸⣿⣿⣂⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⡿⣋⡅⠂⢸⣷⠀⡀⠀⠀⠀⠐⢻⣿⣿⣌⠆")
                    print("⠀⠀⢀⣿⢸⣿⣿⣿⣷⣦⡻⣿⣿⣿⣿⡿⠻⣿⣿⣿⠿⠋⢠⣴⣾⣿⣿⣿⣿⣿⣿⡿⢿⣫⣶⣟⣿⣿⠢⠋⠀⠀⣿⡏⢠⣀⠒⢶⠀⣄⢂⠉⠙⠉⠀")
                    print("⠀⠀⢸⣽⡇⢿⣿⣿⣿⣿⣷⣄⠉⢁⢠⣷⣤⣄⡈⣁⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣶⡾⣿⡿⠟⣋⠉⠀⠀⠀⠀⢰⣾⡏⢰⢈⣿⣿⠀⢹⣾⢀⠀⠀⠀")
                    print("⠀⣴⣿⣿⣷⣶⣮⣭⣟⣛⣛⡂⡼⠦⣾⣿⣻⣿⣿⣿⣳⣜⣛⣻⣭⣷⣾⣿⡿⣿⠽⠟⠁⣠⣶⣷⣆⠀⠀⠀⠀⢸⣿⡇⢸⣿⣿⣿⠀⠈⠣⠘⠀⠀⠀")
                    print("⠚⢿⣿⣟⣿⣿⡈⠻⠍⢿⣿⡇⠄⠀⠈⢻⣿⣿⣻⣿⣿⣭⣿⡭⠉⠁⠄⠈⠁⠀⢀⢠⣇⠛⠉⠋⠀⠀⠀⠀⠀⢸⣿⠇⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠈⠋⠁⠀⠈⠁⠀⢨⣿⡿⠀⡴⢰⢡⣿⣿⣿⣿⣿⣿⣿⢃⠖⡀⠔⢠⢊⢠⣼⠾⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⠀⠀⣤⣽⡿⠃⣄⠶⠁⣰⣿⣿⣿⣿⢻⣿⡏⣰⠠⣽⣆⢹⣿⠘⣿⡇⡿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠀⢀⡾⣿⣿⠀⣴⣿⣦⢰⣿⣿⣿⣿⣿⢸⣿⡇⣿⠀⣾⣿⡈⢿⣷⠹⡛⠁⠀⠀⠀⠀⠀⠀⠀⢠⣿⡏⢸⣿⣧⣿⡆⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⢀⡿⢧⡟⣷⡾⣿⣿⣆⣿⣿⣿⢹⣿⣧⢸⣿⢀⣿⠇⠛⣭⡄⢤⣤⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⡇⢸⣿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⠸⢧⡿⣾⣿⢱⣿⣇⠿⢿⡻⠟⠻⣛⠁⣈⣥⢠⣾⣶⡹⣿⣿⡜⣿⣧⠻⠃⠀⠀⠀⠀⠀⢀⣰⣿⣿⠁⣾⣿⢡⣿⡇⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⢀⡶⣶⣰⣦⢆⣴⡐⣴⣶⢶⣾⡇⢹⣿⢃⣻⣿⡘⣿⣧⡇⠻⠟⠃⢉⡄⠀⠂⣀⣀⣀⡤⠔⣫⣿⣿⠃⣸⡿⣿⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⣾⣼⣿⣿⢇⡞⣧⣽⣿⢟⣼⣿⢣⣿⣿⠄⢿⠟⢃⡍⣩⡴⠀⣘⡋⣀⠄⣀⣴⣭⣿⣿⣿⣿⡿⠟⢁⣼⡟⢠⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠟⡋⠿⠟⠸⠿⣉⣙⡛⡸⣿⠋⢀⣭⣬⡔⢠⣿⡏⢀⡿⠀⢠⣽⡀⣶⣾⠘⣿⣏⣠⣶⣛⣷⣶⣶⣿⣿⣷⣿⣿⣿⣿⣿⣟⣷⡀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠀⡇⣿⣿⣸⣿⡿⣿⣇⡁⣿⣷⠎⢿⡿⠁⡈⠏⣀⢸⣶⣶⢸⣿⠇⣿⣷⣾⣉⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⡿⠁⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⢀⣁⢛⣁⣈⣛⣂⣌⣉⣤⣤⣥⠶⣶⣶⡔⢿⣿⡿⠸⣿⣏⠸⣿⣶⢹⣿⣿⣿⣿⣿⣟⡻⠾⠿⠿⠿⠿⣭⣜⣛⣻⣿⡾⠛⠁⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⠹⡇⣾⡟⢿⣿⡿⢿⣿⣿⢿⣿⡧⣟⣽⠃⡘⣿⣧⠂⣿⣿⣜⣿⣷⣬⣿⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠉⠐⠒⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠀⢠⣤⢨⣀⡈⡏⣁⡀⣿⢹⣟⣿⠇⣬⣹⣆⢷⣿⣿⣆⠻⣿⣿⣿⡿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⢠⣶⣟⣼⣿⣸⣷⣿⣇⣿⣾⣿⣿⣧⣸⣿⣿⣮⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⠀⠀⠀⠙⠾⠷⠿⠿⠿⢿⣿⣿⣿⣿⣿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("El barco esta mas seguro en el puerto pero no fue construido para eso")
                elif AP == "si":
                    print(f"Tu apuesta original de {AC} pesos subio a {AC * 2} pesos")
                    AC = AC * 2
            else:
                print("No tienes el dinero suficiente para duplicar tu apuesta")
            while VA <= 21:
                VA = 0
                CC = len(VM)
                for i in range(0,CC):
                    VA += VM[i]
                if VA > 21:
                    break
                print("")
                print(f"El valor de tus cartas es de {VA}, ¿Quieres quedarte o robar?")
                Is = input("me quedo / robo : ")
                Is = Is.lower()
                if Is == "robo":
                    C = random.randint(1, 13)
                    if C == 0:
                        print("Te salio un JOKER")
                        print("¿Que valor quieres que tome el JOKER?")
                        J = input("1 o 10: ")
                        if J == "10":
                            VM = VM + [10]
                            VA += 10
                        else:
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
                            print("░░░░░░░░░░░░░░░░██████████████████")
                            print("░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░████")
                            print("░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
                            print("░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██")
                            print("░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██")
                            print("░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
                            print("░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██████░░░░██")
                            print("░░░░░░░░██░░░░██████░░░░██░░░░██████░░░░██")
                            print("░░░░░░░░░░██░░░░░░░░░░██████░░░░░░░░░░██")
                            print("░░░░░░░░████░░██░░░░░░░░░░░░░░░░░░██░░████")
                            print("░░░░░░░░██░░░░██████████████████████░░░░██")
                            print("░░░░░░░░██░░░░░░██░░██░░██░░██░░██░░░░░░██")
                            print("░░░░░░░░░░████░░░░██████████████░░░░████")
                            print("░░░░░░░░██████████░░░░░░░░░░░░░░██████████")
                            print("░░░░░░██░░██████████████████████████████░░██")
                            print("░░░░████░░██░░░░██░░░░░░██░░░░░░██░░░░██░░████")
                            print("░░░░██░░░░░░██░░░░██████░░██████░░░░██░░░░░░██")
                            print("░░██░░░░████░░██████░░░░██░░░░██████░░████░░░░██")
                            print("░░██░░░░░░░░██░░░░██░░░░░░░░░░██░░░░██░░░░░░░░██")
                            print("░░██░░░░░░░░░░██░░██░░░░░░░░░░██░░██░░░░░░░░░░██")
                            print("░░░░██░░░░░░██░░░░████░░░░░░████░░░░██░░░░░░██")
                            print("░░░░░░████░░██░░░░██░░░░░░░░░░██░░░░██░░████")
                            print("░░░░░░░░██████░░░░██████████████░░░░██████")
                            print("░░░░░░░░░░████░░░░██████████████░░░░████")
                            print("░░░░░░░░██████████████████████████████████")
                            print("░░░░░░░░████████████████░░████████████████")
                            print("░░░░░░░░░░████████████░░░░░░████████████")
                            print("░░░░░░██████░░░░░░░░██░░░░░░██░░░░░░░░██████")
                            print("░░░░░░██░░░░░░░░░░████░░░░░░████░░░░░░░░░░██")
                            print("░░░░░░░░██████████░░░░░░░░░░░░░░██████████")
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU} pesos conmigo")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("█████████████▀▀▀▀▀▀▀▀▀▀▀▀▀█████████████")
                            print("████████▀▀░░░░░░░░░░░░░░░░░░░▀▀████████")
                            print("██████▀░░░░░░░░░░░░░░░░░░░░░░░░░▀██████")
                            print("█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█████")
                            print("████░░░░░▄▄▄▄▄▄▄░░░░░░░░▄▄▄▄▄▄░░░░░████")
                            print("████░░▄██████████░░░░░░██▀░░░▀██▄░░████")
                            print("████░░███████████░░░░░░█▄░░▀░░▄██░░████")
                            print("█████░░▀▀███████░░░██░░░██▄▄▄█▀▀░░█████")
                            print("██████░░░░░░▄▄▀░░░████░░░▀▄▄░░░░░██████")
                            print("█████░░░░░█▄░░░░░░▀▀▀▀░░░░░░░█▄░░░█████")
                            print("█████░░░▀▀█░█▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀██▀▀░░█████")
                            print("██████░░░░░▀█▄░░█░░█░░░█░░█▄▀░░░░██▀▀▀▀")
                            print("▀░░░▀██▄░░░░░░▀▀█▄▄█▄▄▄█▄▀▀░░░░▄█▀░░░▄▄")
                            print("▄▄▄░░░▀▀██▄▄▄▄░░░░░░░░░░░░▄▄▄███░░░▄██▄")
                            print("██████▄▄░░▀█████▀█████▀██████▀▀░░▄█████")
                            print("██████████▄░░▀▀█▄░░░░░▄██▀▀▀░▄▄▄███▀▄██")
                            print("███████████░██░▄██▄▄▄▄█▄░▄░████████░███")
                            print("Pobreeeeeeee")
                        else:
                            print("         ▄▄█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█▄▄▄")
                            print("     ▄▄█▀▀                    ▀█▄▄")
                            print("   ▄█▀                           ▀█▄")
                            print(" ▄█▀                               ▀█")
                            print(" █                                  █▄")
                            print("█▀      ▄▄▄▄▄▄                       █")
                            print("█    ▄█████████▄       ▄             █")
                            print("█   █████▀▀█████       █          █  █")
                            print("█▄  ▀████▄▄████▀   ▄   █▄       ▄█▀ █▀")
                            print(" █▄   ▀▀▀▀▀▀▀▀█   ███   ██▀▀▀▀▀▀▀ ▄█▀")
                            print("  ▀█       ▄▄▀   █████   ▀▄▄      ▀█")
                            print("  █▀    █        ▀▀▀▀▀       ▄     ▀█")
                            print("  █  ▄▄▀█▀▄▄                ▄█▄▄    █")
                            print("  █      ▀█ █▀▀█▀▀▀█▀▀▀█▀▀█▀▄▀      █")
                            print("  █▄       ▀█  █   █   █  █▀       █▀")
                            print("   ▀█▄       ▀▀▀▀▀▀▀▀▀▀▀▀▀      ▄▄█▀")
                            print("     ▀▀█▄▄▄                 ▄▄█▀▀")
                            print("          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print("""                             ...----.... """)
                        print("""                         ..-:"''         ''"-..""")
                        print("""                      .-'                      '-.""")
                        print("""                    .'              .     .       '.""")
                        print("""                  .'   .          .    .      .    .''.""")
                        print("""                .'  .    .       .   .   .     .   . ..:.""")
                        print("""              .' .   . .  .       .   .   ..  .   . ....::.""")
                        print("""             ..   .   .      .  .    .     .  ..  . ....:IA.""")
                        print("""            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.""")
                        print("""           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.""")
                        print("""           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.""")
                        print("""          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.""")
                        print("""         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA""")
                        print("""         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM""")
                        print("""        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM""")
                        print("""       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.""")
                        print("""       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI""")
                        print("""       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM""")
                        print("""       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM""")
                        print("""       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW""")
                        print("""       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV""")
                        print("""        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI""")
                        print("""       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'""")
                        print("""       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM""")
                        print("""     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.""")
                        print("""     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA""")
                        print("""     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH""")
                        print("""       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV" """)
                        print("""        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM" """)
                        print("""        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM""")
                        print("""        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI""")
                        print("""        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI""")
                        print("""        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'""")
                        print("""        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV""")
                        print("""          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM""")
                        print("""            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'""")
                        print("""             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI""")
                        print("""            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'""")
                        print("""            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM""")
                        print("""            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM""")
                        print("""            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.""")
                        print("""            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI""")
                        print("""            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI""")
                        print("""            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV" """)
                        print("""              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'""")
                        print("""               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM" """)
                        print("""                 "::....::.:::..:..::IIIIIHHHHMMMHHMV" """)
                        print("""                   "::.::.. .. .  ...:::IIHHMMMMHMV" """)
                        print("""                     "V::... . .I::IHHMMV"'""")
                        print("""                       '"VHVHHHAHHHHMMV:"'""")
                        print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                elif DA < 0:
                    DU += DA
                    print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                    print("¿Quieres que te presteeeeee?")
                    RE = input("si / no  : ")
                    RE = RE.lower()
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
                    C2D = "JOKER"
                    V2D = 1
                else:
                    V2D = C2D
                print(f"La segunda carta de la casa es {C2D}")
                VMD = []
                VMD = VMD + [V1D]
                VMD = VMD + [V2D]
                VMA = V1D + V2D
                CaBJ = False
                for i in range(0,2):
                    C1BJ = CBJ1[i]
                    for e in range(0,4):
                        C2BJ = CBJ2[e]
                        if C1D == C1BJ and C2D == C2BJ:
                            CaBJ = True
                        elif C1D == C2BJ and C2D == C1BJ:
                            CaBJ = True
                if CaBJ == True:
                    DA -= AC
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠒⠀⠀⠀⣀⡀⠀⣀⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠲⢤⡀⠀⠀⢀⠀⡇⠀⠁⠀⠀⢰⡏⢻⣿⣿")
                    print("⣿⣿⣿⣿⣿⣿⠻⣿⣿⣿⣿⣿⣿⣿⣿⠹⠶⠊⠉⠀⠀⠀⠀⢸⢶⡢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢁⣼⡴⢀⠇⠀⠀⠀⠀⠀⠀⠉⠿⢿")
                    print("⣿⣿⣿⣿⣿⣿⣷⡙⢻⣿⣿⣿⣿⣿⣿⣶⣶⣬⣤⣄⣨⣄⣀⠈⠈⡍⠉⠁⡏⠀⠀⠀⠀⠀⡀⣅⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠄⣤⠇⠧⣿⣄⣠⠚⢻⠀⠀⠀⠀⠀⠈")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣄⡀⠀⠄⠀⠋⠈⣙⣤⣤⣤⣤⣶⣦⣤⣶⣶⣦⣶⣭⣴⠾⠀⢨⢲⡟⠋⠀⣴⣿⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣁⣁⣈⣉⣙⣟⣻⣿⢻⣿⣿⣧⣤⣤⣬⣹⣾⣿⣿⣿⣾⣿⣟⡛⢛⠛⠉⢁⠁⢟⡿⢿⣶⣡⣿⠆⢀⡾⡟⣿⠀⠀⠀⠀⠀⢰")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⢛⠿⢿⠿⠋⠽⣿⣿⢿⣿⣿⠀⠀⠀⠙⣿⡿⢿⣿⣿⣋⣿⣿⣿⡟⠻⢿⣿⡥⠲⣋⢸⡄⢛⢀⡞⠀⡇⣼⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⢻⠀⠈⠻⢿⠏⠓⠤⣭⣩⣿⣦⣴⣿⣎⣿⣿⡏⠀⠀⠀⠀⢻⣿⡆⠁⢁⢴⡮⠯⢭⡤⢀⡽⠈⠽⡋⠉⢹⠃⣻⣿⠁⠀⢹⠋⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⣧⠀⠀⠈⢆⠀⠀⠀⠀⠨⠟⣻⢿⣿⢿⣿⣇⠀⠀⠀⠀⠈⢿⣆⠀⡀⢀⡈⢑⡖⠒⠏⠀⠀⠀⠀⠀⣼⠀⣼⠈⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣆⠙⠷⣄⣀⠀⠀⠀⠈⠀⠀⢐⣡⢾⠧⣸⣿⣧⠀⠀⠀⠀⠀⠈⢯⢧⡀⠀⠉⢖⡌⠁⠀⠀⠀⠀⢀⡼⠃⠀⣿⢀⠇⢠⠏⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⢉⢉⢉⣒⠒⠊⠉⠉⠁⡀⣧⣶⣿⠇⠀⠀⠀⠀⠀⠀⠈⠳⣭⣓⠦⠤⠤⠤⠤⠴⠶⠚⠉⠀⠀⣰⣿⠋⢀⡏⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣧⣋⠐⡾⢷⠇⠀⠀⠀⠀⣹⡟⣿⣟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⠇⠰⢻⠀⠀⠀⠀⣰⣴⣤⣠⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠐⠀⠀⠀⠀⣸⣿⣤⣿⣍⠀⠀⠀⠀⠀⠀⣀⣤⢀⢬⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⢀⠞⠀⠀⠀⠀⠘⠿⠿⠇⠁")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣮⡈⠈⠀⠁⢠⡜⢹⣿⣿⣿⣿⣿⣦⣤⣤⣴⣿⣿⣿⠃⠈⢖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠴⠀⠀⢢⣎⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣯⣿⣅⠠⢙⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⣿⣿⠖⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣥⠈⢅⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣧⡀⠀⠀⠀⠐⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣏⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠐⠁⣰⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⣉⣩⣍⣙⣙⣉⢁⠉⠁⠋⠙⢻⣿⣿⣿⣿⠀⠄⠀⡤⣶⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⡰⠆⢠⣮")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡋⠙⡙⠟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢈⢠⠀⣿⣿⣿⣿⡽⠀⣾⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⢜⣿")
                    print("⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡜⢵⣿⣿⣿⣿⣿⠣⣾⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘")
                    print("⣿⣿⣿⠉⣙⣥⣿⡟⣉⣭⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣟⣽⣽⣎⢿⣿⣿⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢾⣿⣏⡄⢻⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡀⠀⠀⠀")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⣾⢿⢷⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⣶⢿⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠯⡦⢫⣽⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⠋⡠⣞⢓⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
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
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠉⠉⠉⠉⠉⠉⠉⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣤⣤⡄⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡇⣶⢛⣶⡆⠘⣶⠀⢰⡛⠀⣶⡞⢳⡆⠀⢨⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡇⠿⣌⠉⠁⣠⠿⠀⠸⣥⠀⠉⢁⡼⣇⠀⠰⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣧⡀⣈⠛⠛⠃⣀⣤⠀⠀⠛⠛⠃⠀⣿⠛⢘⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣧⠿⣭⠀⠀⠀⣿⢿⡖⠀⠀⠀⠀⢰⡏⣾⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⡀⠀⠀⠁⠀⠀⠀⠀⢀⣸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠶⣶⠶⢶⡶⠶⣶⠮⢹⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⡟⠛⠻⣟⢻⣿⣿⣿⣧⡄⣸⠀⢸⣗⠀⣿⢠⣼⣿⡇⣿⣿⡟⠛⣭⠈⠁⢩")
                        print("⣿⡏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⣿⣶⡿⠛⣰⣾⣿⣛")
                        print("⣿⣿⡆⠀⠀⠘⠿⣿⣿⣿⣿⣯⣽⣩⣿⣹⣍⣿⡽⠏⢁⣾⡿⠟⢁⣾⣿⠏⠉⠉")
                        print("⣿⣿⣷⡆⠀⠀⠀⠉⠿⣿⣇⣀⣈⣉⣉⣉⣉⣉⣀⣰⣾⡿⠀⢠⣿⠏⠀⠀⠀⠀")
                        print("⣿⠙⢻⣿⣦⠀⠀⠀⠀⠙⠛⢻⣿⣿⣿⣿⣿⣿⡟⠛⠋⠁⠀⣿⡏⠀⠀⠀⠀⠀")
                        print(F"Ganaste con {VA} puntos")
                        print(F"Ganas {AC}!!! Quedando con {DA} pesos")
                    elif VMA > VA:
                        print("⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠏⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠢⡓⡄⠀⠀⠀⠀⠀⠀⣸⡀⡀⠀⠀⠀⠸⣿⣿⡷⣶⡄⣀⠀⠀⠀⠀")
                        print("⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠄⠁⠀⠀⠀⠀⠌⠂⡀⠀⡀⢀⡰⠛⠻⠃⠀⠀⠀⢀⣿⡟⡃⠀⣴⣿⣷⣄⠀⠀")
                        print("⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⢿⠛⠛⢿⡌⣯⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⠔⠈⡀⢞⠀⠀⠀⠀⠘⠀⠀⢁⣀⣁⡀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠛⣿⣿⠟⢧⠀")
                        print("⣸⣿⣿⣿⣿⣿⣿⠿⡈⠁⠀⣄⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠐⠈⢀⣤⢞⢽⢣⡆⢂⠀⠄⠀⠀⠀⠠⠠⠑⢫⣉⢛⣤⣀⠀⢸⣿⣿⠀⠀⠀⠘⠃⠰⣿⣇")
                        print("⣿⠛⠻⣿⣿⠿⠛⡁⠠⢶⠌⠈⠚⠄⡀⠀⠀⠀⠀⠀⠀⠠⠄⠊⡁⠀⠠⠒⢉⢠⢕⠅⣡⡊⠀⠈⢀⠀⢠⠐⠠⡀⠲⠮⠿⠦⣤⠬⠶⠼⢿⡶⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠈⠁⠀⠀⠁⣒⠁⢀⣶⣄⠀⠀⠀⢬⠑⠱⠄⠀⠀⠀⠀⢀⠇⠈⠀⠀⠀⠘⣉⣡⣄⣠⡌⠙⠀⠤⠁⠁⠀⠶⠴⠄⠹⠀⠐⠀⠈⠷⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                        print("⠀⠀⠀⠀⠀⠉⡀⠘⣯⣬⣠⠂⠀⠀⠈⠐⠐⢤⡀⠂⢀⢜⠯⠂⡀⣀⣴⣾⣿⣿⣿⢿⣿⣿⣦⣭⣈⣉⣁⠀⠀⠀⠀⡀⠒⠛⣂⣹⣷⣤⣄⡀⠀⠀⢀⡀⠀⠀⠀⠀")
                        print("⠀⠈⠂⠂⡆⣡⣟⠛⠉⢧⣛⠀⠀⠀⠀⠂⠈⠀⠀⠀⠀⢣⠀⢳⡿⣿⣿⠟⠉⠁⠀⠀⠀⠈⠙⢻⣷⣾⡭⠀⠂⠀⠐⠾⠿⠿⢿⠿⠿⢿⠓⠀⠀⠀⡀⠀⠀⢀⡀⠴")
                        print("⠀⠀⠀⠀⣹⣗⠙⢧⣳⠟⢿⡄⠀⠀⠀⣰⣾⣿⣷⡄⠀⢡⢆⣔⣠⠙⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣯⣴⣄⠀⠀⠈⠉⠩⡇⠀⠀⠴⣶⣿⣿⣿⣟⡛⠠⠗⠢")
                        print("⠀⢠⣶⡾⠉⣿⣷⡾⢿⠀⠐⠻⣦⠀⠀⡟⠛⠛⠛⠁⠀⡌⠿⢿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⡒⠀⡄⠐⡏⠈⡀⠀⠈⠻⡟⠟⠙⠁⠀⠀⠀")
                        print("⠀⠘⣿⡄⠀⠁⠻⣯⢿⣯⠀⣤⣽⢆⠀⠀⠀⠀⠀⠀⣴⣿⣷⠻⢰⣷⣄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⡀⠁⡸⠏⠀⠉⢴⠀⠀⠥⠐⠃⠀⠠⠀⠀")
                        print("⠀⠀⠹⣿⣀⠀⠀⠐⢀⣬⣦⡤⡊⠈⠁⠂⠠⢤⣴⣧⣿⣿⠗⠻⣾⣿⣿⣷⣄⢆⠡⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣎⡪⠈⢀⣀⡀⠁⢀⠄⠀⠀⠀⠀⠈⠉")
                        print("⠀⠀⢀⡟⠛⠷⣄⣠⣿⣿⡟⠀⠀⢄⣠⣀⣠⡾⠙⠻⣸⣯⡆⢀⠹⠻⢿⣿⣿⣷⢿⡜⡼⣒⣨⣄⡀⣠⣴⣴⣿⣷⣿⣿⣿⡟⠀⢰⣿⣿⣿⣆⠀⠂⢀⠠⢲⣶⠤⠈")
                        print("⠆⠀⠀⠀⠀⣰⣿⣿⣿⠟⠉⠀⠀⣺⣿⣿⣿⣶⣶⣦⢹⣿⣧⣧⢀⠀⣀⣄⡀⠄⣠⣾⣧⠘⠿⣿⣿⣿⣿⣿⣿⠁⣾⣿⣿⣷⠀⠩⠈⠙⠻⡿⠀⠈⢁⣤⡞⣧⠀⢀")
                        print("⢀⠀⠀⠤⠈⢋⠟⠉⠀⠀⠀⠀⠀⣏⠉⠉⠉⠉⠉⠉⠹⣿⣿⣿⣷⡠⣟⢛⣷⣼⣿⢿⣿⡆⣀⣀⠉⠛⠉⠋⠈⠀⢱⣿⣿⣿⣦⡀⠀⠀⠈⠊⢀⣼⠟⠉⠀⢚⡄⢉")
                        print("⠀⢈⠿⢶⣦⣌⣲⣤⣀⣀⣄⣤⣾⣿⣢⣄⠀⠀⣠⠀⡀⠹⣿⣿⣿⣶⡆⠨⢻⣿⣛⣸⣿⡇⠘⠉⠰⣂⣰⣡⡄⢀⣽⣿⣿⣿⣿⣷⣦⣤⢤⣴⡏⢡⡌⢢⣔⡏⣷⡿")
                        print("⢤⣅⣀⣤⣬⣉⣽⣿⣿⣿⣿⣿⣿⣿⣿⣭⣷⣿⣿⠾⣡⣢⣿⣿⣿⣿⠛⡇⡾⢠⡿⠉⡍⠁⠌⢃⣾⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⠟⣫⣍⣽⣿⣦⣤⡘⠋⡤⠛⠀")
                        print("⡀⠘⠀⠈⠙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⡿⢿⣥⣴⣿⣿⣿⣿⣿⣿⣶⣄⡟⠸⡗⢧⢶⡾⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠅⠰⢏⠙⠟⡟⠁⢙⣿⡄⠀⠀⠀")
                        print("⠡⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗⣐⣤⣭⣽⣿⣿⡁⠉⣿⢿⣿⣿⣿⣶⣶⣾⣾⣿⣿⣿⣿⡿⢸⣿⣿⣿⣿⣿⣿⡿⠿⠐⠀⣠⡴⠊⠀⠀⠂⣼⣷⡤⠒⠋")
                        print("⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢵⢷⠦⢙⡻⣿⣿⣿⣿⡁⢹⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠋⣠⣾⣿⣿⣿⣿⣿⣿⡳⠊⣠⡾⡟⡇⠀⠒⠀⠤⣿⣿⣿⠀⠀")
                        print("⡄⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⠇⠁⢨⢠⣶⣶⣿⣮⡙⢻⣿⣷⠀⢀⢻⣿⣿⣿⣿⣿⣿⢣⠇⣠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀⠠⠿⠾⢛⣧⡅⠀⠀⢁⣽⡿⠃⢂⠀")
                        print("⢃⡁⠀⠀⢆⠀⠀⢹⣿⡿⠋⠁⠀⠆⡸⡻⣿⣿⡿⡟⢿⣟⣷⣿⣇⠀⢾⣙⣙⣿⣿⣹⠿⢋⣼⣿⣿⣿⣿⣻⣿⣿⡿⢓⠐⠃⢀⣤⡶⣟⠯⣿⣄⠀⠈⢻⣷⣶⣶⣦")
                        print("⠈⢿⡆⢀⠐⡀⠀⠀⣟⠒⠀⣾⣿⣿⣥⣡⣘⡻⣛⣟⣳⢏⣿⣷⠛⣦⡀⠉⠏⠇⠃⣁⣴⣿⡿⣿⣵⣿⣿⣿⣻⣿⡞⠁⣠⣬⣿⣤⡄⠀⠀⣿⣿⣷⣄⢹⣿⣿⠿⠋")
                        print("⠀⠉⡇⠀⢀⠘⣔⣄⡄⠈⠁⣿⣿⣿⣿⢻⡞⡿⠟⠟⢋⡎⣼⣿⠷⡊⠻⣶⣶⣶⣾⣿⣿⢿⣿⣿⣤⣾⣿⣿⣿⡏⢳⠾⣿⣿⡝⢡⠛⣗⡀⢿⣿⣿⣿⠟⠋⠀⠀⠀")
                        print("⠀⠀⢁⡀⣼⣦⠰⢫⡇⠀⠀⢹⣿⣿⠙⠆⡿⢛⢛⣛⣻⣹⣷⢿⡃⠇⠀⠀⠈⠛⠛⠛⢯⣾⣿⣿⣿⣿⢿⢛⣿⡏⠁⢾⣿⢻⣇⠈⠆⠉⠀⢼⣿⡿⣦⠤⠤⢀⣀⣠")
                        print("⠀⠀⠈⡃⢈⣿⡇⠀⡿⣦⠀⠈⢹⠿⣷⡔⠘⠛⠛⣛⢉⡾⣟⣜⣡⣤⠀⠀⠀⢀⠀⣠⣑⠋⠛⠻⢛⠛⢩⣻⣿⣿⡁⢀⡈⠨⣻⡀⠀⢹⣀⣀⠤⣒⣒⣀⣼⡿⠟⠛")
                        print("⠀⡀⢰⢀⣾⣿⠃⠀⢃⣾⣧⡀⠘⡀⡘⣷⡀⠖⣟⣛⣏⣹⢻⠸⣟⡯⠀⠀⠀⠀⣀⡗⣙⣠⣤⢪⣼⣂⣿⣛⣿⣿⡹⠿⣿⣿⣻⡧⠡⠈⢿⣶⠛⠿⣿⣿⣧⣄⣀⠀")
                        print("⠀⢻⡆⣸⣿⣾⡇⠀⢸⠸⢿⣿⡜⠀⠀⠢⣅⠰⠞⣹⣵⣠⡏⣟⣿⣿⣷⣄⣢⠶⢏⠳⠾⡟⠾⢷⣾⢯⣼⣷⣎⣿⣯⠚⢣⣾⣾⣿⣿⣷⢈⢋⣰⣮⡄⠝⠻⣿⠟⠀")
                        print("⠀⠀⠙⢻⣿⣟⠆⠀⡈⢀⠈⣿⣿⣆⠈⠠⠈⢳⣞⣋⣽⣧⠾⢻⣿⣿⡉⡋⣂⠀⠀⠟⠿⢽⣄⣨⣿⢾⣿⢿⣿⣿⢿⡦⡈⡿⡿⠿⣿⣿⣿⣽⡿⣿⣷⠈⠼⠋⠀⠀")
                        print("⠀⠀⠀⠀⠙⠁⠀⠀⠡⠚⠈⠃⢹⡿⠟⠁⠀⠲⣿⠝⠫⢰⣯⠿⢿⣿⣷⡈⠙⡆⠤⠶⣤⣼⡭⣮⠛⡻⣛⠳⣿⣿⡵⠏⣞⣦⠀⠁⠜⠛⢿⣿⡿⠌⠛⠁⠀⠀⠀⠀")
                        print(f"La casa gana con {VMA} puntos, pasandote por {VMA-VA} puntos")
                        print(F"Perdiste con {VA} puntos")
                        DA -= AC
                        print(F"Pierdes {AC}!!! Quedando con {DA} pesos")
                    elif VMA < VA:
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠉⠉⠉⠉⠉⠉⠉⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡏⠀⢀⣤⣤⡄⠀⠀⠀⠀⣤⣤⡄⠀⠀⠀⢙⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡇⣶⢛⣶⡆⠘⣶⠀⢰⡛⠀⣶⡞⢳⡆⠀⢨⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⡇⠿⣌⠉⠁⣠⠿⠀⠸⣥⠀⠉⢁⡼⣇⠀⠰⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣧⡀⣈⠛⠛⠃⣀⣤⠀⠀⠛⠛⠃⠀⣿⠛⢘⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣧⠿⣭⠀⠀⠀⣿⢿⡖⠀⠀⠀⠀⢰⡏⣾⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⡀⠀⠀⠁⠀⠀⠀⠀⢀⣸⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠶⣶⠶⢶⡶⠶⣶⠮⢹⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⡟⠛⠻⣟⢻⣿⣿⣿⣧⡄⣸⠀⢸⣗⠀⣿⢠⣼⣿⡇⣿⣿⡟⠛⣭⠈⠁⢩")
                        print("⣿⡏⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⣿⣶⡿⠛⣰⣾⣿⣛")
                        print("⣿⣿⡆⠀⠀⠘⠿⣿⣿⣿⣿⣯⣽⣩⣿⣹⣍⣿⡽⠏⢁⣾⡿⠟⢁⣾⣿⠏⠉⠉")
                        print("⣿⣿⣷⡆⠀⠀⠀⠉⠿⣿⣇⣀⣈⣉⣉⣉⣉⣉⣀⣰⣾⡿⠀⢠⣿⠏⠀⠀⠀⠀")
                        print("⣿⠙⢻⣿⣦⠀⠀⠀⠀⠙⠛⢻⣿⣿⣿⣿⣿⣿⡟⠛⠋⠁⠀⣿⡏⠀⠀⠀⠀⠀")
                        print(f"La casa pierde con {VMA} puntos, la pasaste por {VA-VMA} puntos")
                        print(F"Ganaste con {VA} puntos")
                        AC = AC * 2
                        DA += AC
                        print(F"Ganas {AC}!!! Quedando con {DA} pesos")
                    elif VA == VMA:
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠫⠙⠩⠉⠫⠙⡝⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠑⢊⠲⣍⠻⣝⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠣⢌⠳⣜⠻⣼⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⢎⡱⢬⠳⡭⣞⣳⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠐⣊⠕⡳⢼⡹⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡈⢜⠱⣫⢵⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡘⠤⠫⡔⢯⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⢓⡘⡳⣮⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⡜⢠⢣⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⢁⠸⢄⢣⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠄⣘⡜⢢⢇⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣷⣌⡃⢎⠵⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠊⠀⢀⣀⣠⣶⣴⣶⣶⣶⣾⣿⣆⡁⢀⣄⣀⠀⠀⠀⠀⢤⣰⣿⣿⣿⣿⣿⣿⣷⣾⣿⣽⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠄⠨⠷⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠀⠀⠻⣿⣿⣿⡻⢿⠻⡟⠋⠁⠀⠀⠀⠀⠀⠀⣠⣤⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠐⠀⠀⠈⢹⠿⠿⠷⠷⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⢿⣿⣿⣿⣿⡿⠃⢠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⣀⣀⣤⣀⣀⣀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣼⣽⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣰⠀⠀⠙⠋⢉⠛⣋⠛⠀⠀⠀⠀⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣴⣤⣄⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣾⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⡇⡀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣶⡑⢦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⢻⣿⣿⣃⠀⠀⠀⠀⠀⠀⠀⠐⠾⡿⢏⡳⣉⠶⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠙⣿⣿⣿⠀⢹⣶⡄⠀⠀⠀⠀⣴⣶⣿⣵⡎⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠻⣿⣿⣦⣄⡉⠛⠒⠂⠀⢹⣿⠿⢿⡃⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠈⠁⠉⢻⣷⢶⣤⣤⣄⣼⣯⣀⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠀⠀⠀⠀⠀⠻⠁⣀⣿⠇⠀⢻⡗⠉⢻⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠈⠀⠀⡀⠀⠀⠉⠻⠟⣶⣶⣿⢿⣦⣶⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠠⠀⠀⠀⠀⠀⠈⠙⠎⠙⡻⢟⡿⣻⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠂⠀⠀⠀⠀⠀⠀⢀⠹⢎⢶⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⢀⢀⣄⣚⢤⣫⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
                        print(f"La casa empata con {VA} puntos, se devuelve el dinero")
                        print(F"Empataron con {VA} puntos")
                        print(F"No ganas nada, Quedando con {DA} pesos")
                if DA == 0:
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜")
                    print("⬜⬜⬜⬛🟥🟥🟥⬛⬛⬛⬜⬛⬜⬛⬜⬛⬛⬛🟥🟥🟥⬛⬜⬜⬜")
                    print("⬜⬛⬛⬜⬛⬛🟥🟥⬛⬜⬛⬛⬛⬛⬛⬜⬛🟥🟥⬛⬛⬜⬛⬛⬜")
                    print("⬛⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬛")
                    print("⬛⬜⬜⬜⬜⬜⬛⬛🟥🟥⬛⬛⬛⬛⬛🟥🟥⬛⬛⬜⬜⬜⬜⬜⬛")
                    print("⬛⬛⬛⬛⬛⬛⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜⬛⬛⬛⬛⬛⬛")
                    print("⬜⬛🟨🟨🟨⬛⬛⬜⬜⬛🟥🟥⬛🟥🟥⬛⬜⬜⬛⬛🟨🟨🟨⬛⬜")
                    print("⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬛🟥⬛🟥⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜")
                    print("⬜⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜⬛⬜🟧🟧⬜⬛⬜⬜⬛⬜⬜⬜")
                    print("⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜")
                    print("⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜")
                    print("⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜")
                    print("⬜⬜⬛⬛⬛⬛⬜⬜⬜⬛🟨⬛🟨⬛🟨⬛⬜⬜⬜⬛⬛⬛⬛⬜⬜")
                    print("⬜⬜⬛🟨🟨⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛🟨🟨⬛⬜⬜")
                    print("⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜")
                    print("⬜⬜⬛🟥🟥⬛⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬛⬛🟥🟥⬛⬜⬜")
                    print("⬜⬜⬛🟥🟥🟥⬛⬜⬜⬛🟨⬛⬛⬛🟨⬛⬜⬜⬛🟥🟥🟥⬛⬜⬜")
                    print("⬜⬜⬛🟥🟥⬛🟥⬛⬛🟦⬛🟨🟨🟨⬛🟦⬛⬛🟥⬛🟥🟥⬛⬜⬜")
                    print("⬜⬜⬜⬛🟥⬛⬛⬜⬛⬛🟦⬛⬛⬛🟦⬛⬛⬜⬛⬛🟥⬛⬜⬜⬜")
                    print("⬜⬜⬜⬛🟥⬛⬜⬜⬜⬛⬛🟦🟦🟦⬛⬛⬜⬜⬜⬛🟥⬛⬜⬜⬜")
                    print("⬜⬜⬜⬜⬛🟥⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛🟥⬛⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥🟥⬛⬜⬛🟥🟥⬛⬛⬛⬜⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥⬛⬜⬛🟥⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬛🟥🟥🟥🟥🟥⬛⬜⬛🟥🟥🟥🟥🟥⬛⬜⬜⬜⬜⬜")
                    print("⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜")
                    print(F"Te quedaste sin dinero, ¿Quieres pedir un prestamo?")
                    RE = input("si / no  :")
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input())
                        if DP > 0:
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠞⠉⠀⠀⠀⠀⠀⠉⠓⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠑⢲⡄⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⢸⡟⠲⠄⠀⣀⣀⣀⣀⡀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⢸⣧⠀⠀⠀⠀⣿⣏⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠉⠉⢠⣿⡀⠈⠉⠉⣧⣤⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⠸⠛⠇⠀⠀⢠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠬⢷⠶⡶⠶⠶⢶⡖⣿⣿⣧⠤⠤⢤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠁⢀⣠⣶⣾⣤⣧⣀⣆⣸⣇⣿⣿⣿⣿⣿⣿⠟⣣⣚⣛⠓⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢩⠟⠋⠉⠉⠉⠒⣄⠈⢣⡀⠀⠀⣀⡤⢖⣶⡄")
                            print("⠀⠀⠀⠀⢀⡠⠴⠶⣿⡀⠀⠀⠻⣿⡿⢧⣽⣸⣸⣀⣧⣿⣳⣿⠟⢀⠇⠀⠀⠀⠀⠀⠀⠈⣆⠀⠈⠉⢉⡥⠚⠉⠈⡾")
                            print("⠀⠀⢀⡞⠁⠀⠀⢀⡇⠑⢤⡀⠀⠈⠛⠶⣦⣥⣶⣶⣶⠿⠛⠁⢠⢾⠀⠀⠀⠀⠀⠀⠀⠀⢱⡉⠉⠉⠁⠀⠀⠀⠀⠀")
                            print("⠀⠀⡾⠀⠀⠀⠀⣾⠀⠀⠀⠙⢦⠀⣄⠀⠀⠈⠉⠉⠀⣀⡠⠖⠁⠸⡄⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⢳⠀⠀⠀⠀⣿⠀⠀⠀⠀⠘⡆⢸⠳⣄⣀⢀⡴⠊⠁⠀⠀⠀⠀⠳⣄⡀⠀⠀⠀⣀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠈⣧⡀⠀⠀⠘⣇⠀⠀⠀⠀⠙⢾⣆⠀⠈⠛⠘⢯⠟⠁⠀⠀⠀⡼⠈⣿⠙⠚⢉⣹⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⢠⡯⣉⡶⠒⠒⠛⠢⣀⠀⠀⠀⠀⠈⠁⠀⠀⠼⠶⠖⠂⠀⣠⠞⠁⠀⠈⡏⠉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⢀⠏⢀⡎⠀⠀⠀⠀⠀⠈⠙⠲⠦⣄⣀⣀⣀⣀⣀⣀⡠⠴⠋⠁⠀⠀⠀⠀⢿⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⡞⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⡀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⣇⣼⣀⣠⠤⠤⣤⣀⠤⡄⠀⠀⠀⠀⢸⡉⠉⡏⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠘⠿⣿⠯⣭⣍⠭⣷⠏⠀⣸⠦⣄⡀⠀⢸⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠓⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠈⠉⠉⠉⠉⣿⣤⣼⠁⠀⠀⣹⣆⢸⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⣿⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⢠⠒⣏⡉⠉⠁⠀⠀⠀⣇⠉⠛⠢⠤⣇⣀⣀⣀⡀⠀⠀⠀⠀⠀⢸⣿⠉⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠘⠷⣄⣉⠉⠉⠐⢀⣴⡇⠙⠲⢤⣀⣀⠀⢈⣉⡇⠀⠀⠀⠀⠀⠸⣿⣄⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⡞⢹⢄⡀⠀⠀⠀⢉⣭⡟⠁⠀⠀⠀⠀⠀⢠⣷⣻⣼⣧⠀⠀⠀⠀⣀⠤⠒⠲⢦⡀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⢸⠀⠉⠑⠒⠒⢻⡀⢧⠀⠀⠀⠀⠀⠀⠙⣇⠀⣀⣼⣀⣠⠴⠊⠁⠀⠀⠀⢀⡇⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⡎⠀⠀⠀⠀⠀⠈⢧⠘⡆⠀⠀⠀⠀⠀⠀⠘⢿⠁⠀⠀⠰⡄⠀⠀⠀⣀⡴⠋⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⣇⠀⠀⠀⠀⠀⠀⠘⡆⢹⣀⣠⢤⡀⠀⠀⠀⠈⠑⠦⣄⡀⠈⠛⠯⣍⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⠀⣿⣿⢦⠀⠀⠀⠀⢀⣵⠀⣿⠟⠁⢣⠀⠀⠀⠀⠀⠀⠈⠉⠓⠒⠒⠛⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⠹⢿⢿⠤⠟⠁⡞⠀⠀⠀⠰⡟⠛⠉⣀⠴⠋⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⡗⠤⠤⠄⠀⠀⡇⠀⠀⠀⠀⠙⢦⠈⢀⡠⠔⠋⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠒⠤⠄⠀⠀⢧⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⣀⠔⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⣒⡶⢦⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠹⡄⠈⠀⠀⡠⠞⠓⠲⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⢀⡴⠊⠉⠁⠀⠀⠈⠉⠀⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠉⢢⡀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⣠⠤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠳⣀⣀⣀⣀⣠⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠦⢄⣀⣀⣀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀")
                            DA += DP
                            DU += DP
                            print(F"FELICIDADES!!! ahora tienes una deuda de {DU}")
                            print("DEVUELTA AL JUEGO!!!")
                        elif DP == 0:
                            print("Pobre")
                        else:
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡘⠛⠛⠛⠛⠛⠛⠛⠛⠛⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⢸⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣼⣿⠀⠀⢀⣀⠘⠛⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⣤⡄⠀⠘⠛⠛⠛⠛⠛⠀⠀⠘⠛⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠃⣀⡀⠀⠀⠛⢃⣀⣀⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⣀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠘⠛⠛⠛⠛⠛⠀⠀⢠⣤⠘⠛⢻⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣤⣤⣿⡇⠀⠀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⢸⣿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⠛⠛⠛⠛⠛⠃⣤⡄⠛⢣⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⢠⣤⡀⠀⠀⠀⣤⣤⠘⠛⠛⠛⣿⣿⣤⣤⣤⣤⣤⣴⣿⡇⠀⢸⣿⣿⣿⠛⠛⢻⣿⠛⠛⢻⣿⣿⣿⣤⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⢸⣿⣧⣤⣤⣤⠙⠛⠀⠀⣤⣤⠛⠛⠛⠛⠛⠛⣿⡟⠛⠃⣤⡌⠛⢻⣿⠀⠀⢸⣿⠀⠀⢸⣿⣿⣿⠛⠛⠛⠃⣤⣄⠀⠀⠀⠀⠀⠀")
                            print("⢸⣿⡏⠉⠉⠉⠀⠀⢠⣤⠉⠉⠀⠀⠀⠀⠀⠀⠉⠁⣤⡄⠉⢡⣤⡌⠉⢠⣤⣼⣿⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠉⠉⣤⡄⠀⠀⠀⠀")
                            print("⢸⣿⡇⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠘⠛⢣⣤⠈⠉⠉⠉⢠⣤⠘⠉⢿⣿⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀")
                            print("⠈⠉⢠⣤⠀⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⡄⠀⠀⠀⠀⠉⠁⣤⡄⠀⠈⠉⢠⣤⣤⣤⣼⣿⣤⣤⣿⣿⣤⡄⠀⠀⣤⣤⠙⠃⣤⡄⠀⠀")
                            print("⠀⠀⠈⠛⢠⣤⠀⠀⢸⣿⠛⠛⠛⠛⠛⠃⣤⣤⣤⡄⠀⠀⠛⢡⣤⣤⣤⣼⣿⠛⠛⠛⠛⠛⠛⣿⣿⠛⠃⣤⡄⠛⠋⣤⡄⠛⠁⠀⠀")
                            print("⠀⠀⠀⠀⠈⠉⣤⣤⣾⣿⣤⣤⣤⣤⣤⣤⠉⠙⣿⡇⠀⠀⠀⠈⠉⢹⣿⠋⠉⠀⠀⠀⠀⢠⣤⠉⠉⣤⣤⣿⣷⣤⣤⣿⡇⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⢻⣿⣿⣿⣿⣿⣤⡄⠉⠁⠀⠀⠀⢠⣤⡌⠉⢠⣤⣤⣤⣤⣤⣾⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡟⠉⠉⣿⡇⠀⠀⠀⠀⠀⢸⣿⣧⣤⣼⣿⠋⠉⠉⠉⢹⣿⣤⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡄")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣾⣿⠉⠁⠀⠀⣿⣷⣤⡄⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠉⣿⡟⠉⠉⣿⣿⣿⣿⣿⡏⠉⠁")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣶⣶⣶⣦⠉⠉⣿⣷⣶⣶⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠉⠁⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⣿⣿⣿⠉⠉⠀⠀⣿⡏⠉⠙⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣿⣿⠀⠀⣶⡆⠉⠁⠀⠀⠉⠉⠉⠉⠉⢹⣿⠉⠉⢹⣿⠉⠉⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⣶⣶⣿⣷⣶⡆⠀⠀⠀⠀⠀⢰⣶⣾⣿⣶⣶⣾⣿⣶⣦⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⣿⣷⣶⡆⠀⠀⠀⢸⣿⣿⣿⣿⣿⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⠁⠀⢰⣶⣾⣿⣿⣿⣿⣿⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⣶⣶⣶⡎⠉⢹⣿⣿⣿⣿⣿⠉⠉⣴⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠉⢱⣶⡎⠉⠉⠉⠉⠉⢰⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠈⠉⢱⣶⣶⣶⣶⣶⡊⠉⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣶⡆⠀⠀⠀⠀⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⣿⣿⣿⡇⠀⠀⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢰⣶⣾⣿⣿⣿⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣾⣿⣿⣿⡇⠀⠀⠀⢸⣿⠁⠉⠉⠁⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⠈⣿⡇⠀⠀⠀⢸⣿⣷⣶⣶⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⠁⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⢈⣿⡇⠀⠀⠀⢸⣿⣷⣶⣶⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢸⣿⠁⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⢸⣿⠀⠀⢰⣶⠀⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀")
                            print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀")
                            print(F"No comprendo la cantidad asi que te prestare 100000 pesos")
                            DA += 100000
                            DU += 100000
                    else:
                        print("""                             ...----.... """)
                        print("""                         ..-:"''         ''"-..""")
                        print("""                      .-'                      '-.""")
                        print("""                    .'              .     .       '.""")
                        print("""                  .'   .          .    .      .    .''.""")
                        print("""                .'  .    .       .   .   .     .   . ..:.""")
                        print("""              .' .   . .  .       .   .   ..  .   . ....::.""")
                        print("""             ..   .   .      .  .    .     .  ..  . ....:IA.""")
                        print("""            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.""")
                        print("""           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.""")
                        print("""           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.""")
                        print("""          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.""")
                        print("""         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA""")
                        print("""         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM""")
                        print("""        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM""")
                        print("""       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.""")
                        print("""       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI""")
                        print("""       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM""")
                        print("""       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM""")
                        print("""       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW""")
                        print("""       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV""")
                        print("""        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI""")
                        print("""       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'""")
                        print("""       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM""")
                        print("""     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.""")
                        print("""     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA""")
                        print("""     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH""")
                        print("""       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV" """)
                        print("""        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM" """)
                        print("""        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM""")
                        print("""        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI""")
                        print("""        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI""")
                        print("""        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'""")
                        print("""        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV""")
                        print("""          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM""")
                        print("""            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'""")
                        print("""             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI""")
                        print("""            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'""")
                        print("""            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM""")
                        print("""            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM""")
                        print("""            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.""")
                        print("""            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI""")
                        print("""            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI""")
                        print("""            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV" """)
                        print("""              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'""")
                        print("""               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM" """)
                        print("""                 "::....::.:::..:..::IIIIIHHHHMMMHHMV" """)
                        print("""                   "::.::.. .. .  ...:::IIHHMMMMHMV" """)
                        print("""                     "V::... . .I::IHHMMV"'""")
                        print("""                       '"VHVHHHAHHHHMMV:"'""")
                        print(f"Te quedaste sin dinero y con una deuda de {DU}")
                        exit
                elif DA < 0:
                    DU += DA
                    print(f"Te quedaste sin dinero y con una deuda de {DU} pesos")
                    print("¿Quieres un prestamo?")
                    RE = input("si / no  : ")
                    RE = RE.lower()
                    if RE == "si":
                        print(F"¿De cuanto es el prestamo?")
                        DP = int(input(": "))
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
                        print("""                             ...----.... """)
                        print("""                         ..-:"''         ''"-..""")
                        print("""                      .-'                      '-.""")
                        print("""                    .'              .     .       '.""")
                        print("""                  .'   .          .    .      .    .''.""")
                        print("""                .'  .    .       .   .   .     .   . ..:.""")
                        print("""              .' .   . .  .       .   .   ..  .   . ....::.""")
                        print("""             ..   .   .      .  .    .     .  ..  . ....:IA.""")
                        print("""            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.""")
                        print("""           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.""")
                        print("""           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.""")
                        print("""          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.""")
                        print("""         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA""")
                        print("""         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM""")
                        print("""        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM""")
                        print("""       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.""")
                        print("""       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI""")
                        print("""       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM""")
                        print("""       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM""")
                        print("""       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW""")
                        print("""       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV""")
                        print("""        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI""")
                        print("""       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'""")
                        print("""       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM""")
                        print("""     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.""")
                        print("""     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA""")
                        print("""     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH""")
                        print("""       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV" """)
                        print("""        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM" """)
                        print("""        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM""")
                        print("""        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI""")
                        print("""        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI""")
                        print("""        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'""")
                        print("""        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV""")
                        print("""          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM""")
                        print("""            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'""")
                        print("""             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI""")
                        print("""            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'""")
                        print("""            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM""")
                        print("""            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM""")
                        print("""            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.""")
                        print("""            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI""")
                        print("""            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI""")
                        print("""            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV" """)
                        print("""              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'""")
                        print("""               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM" """)
                        print("""                 "::....::.:::..:..::IIIIIHHHHMMMHHMV" """)
                        print("""                   "::.::.. .. .  ...:::IIHHMMMMHMV" """)
                        print("""                     "V::... . .I::IHHMMV"'""")
                        print("""                       '"VHVHHHAHHHHMMV:"'""")
                        print(f"Te quedaste sin dinero y con una deuda de {DU}")
                        break
if DU > 0 and DA > 0:
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⣀⣤⠖⠛⠉⠉⠛⠀⠀⠀⠸⠉⠛⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⣠⠔⠋⡀⠀⠀⠐⠟⠂⠀⠀⠚⠃⠀⠀⢦⠀⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⢠⠞⠃⠀⠚⠃⢀⣠⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣰⠏⢀⡄⠀⡠⠊⠁⣀⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⠀⠉⠀⠈⢁⠔⠋⠁⢀⣀⣤⠤⠴⠶⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⡏⣠⡀⠀⠰⠃⢀⣴⣚⣉⡴⠋⠙⠓⢦⡀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⡤⠤⢦")
    print("⣇⠉⠀⠀⠀⡴⡿⠋⠉⠹⡇⠀⠀⠀⠀⣿⣤⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⡼")
    print("⠹⡄⠀⠀⠘⢱⡇⠀⠀⣀⣿⡷⢺⣯⠉⠉⢹⡀⠐⣾⣅⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⠀⢀⣀⡀⣠⠞⠁")
    print("⠀⠙⢦⣀⠀⠀⣷⠿⣾⡅⠀⢧⠈⢿⣧⡀⠈⡇⠐⠊⣉⣁⣈⣙⣦⠀⠀⠀⠀⠀⢀⣀⡠⠴⠚⢩⠀⠀⠀⠀⠀⢀⣤⣤⣿⠿⠛⠁⠀⠀")
    print("⠀⠀⠀⠈⠉⠙⠻⡄⠹⣿⣄⡼⠱⢄⣙⣁⣜⣡⠔⠋⠉⠀⠀⠈⠉⠙⠓⠲⢶⠚⠉⠁⠀⢀⣀⡬⠴⠒⠋⠙⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠛⣦⣌⣻⡇⠀⠀⣹⠾⠻⣀⣤⣀⡀⠀⣤⣄⡀⢀⣀⣠⡾⠶⠒⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢠⠞⠀⠀⣸⣀⡤⠊⠁⠀⡴⣟⢿⡟⠛⠶⠿⠿⠖⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⣿⠀⠔⣩⠜⠁⠀⠀⡠⠊⠀⠘⣎⣧⠀⣀⣀⡤⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠘⢲⠞⠁⠀⠀⡠⠊⠀⠀⠀⠀⡿⠉⠈⠻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⢰⢃⠀⠀⢀⠜⠓⠤⣄⣀⣤⠞⠁⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠘⠷⣶⣾⣥⠤⠶⠚⠉⠀⢿⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠋⣀⣠⣤⣤⣀⣀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠉⠁⠀⠀⠀⠀⠉⠙⠾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"Te retiras del juego con {DA} pesos y una deuda de {DU} pesos")
elif DA > 0 and DU == 0:
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠤⠤⠤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠢⡀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠈⢦⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠈⡆⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠰⡜⢠⠂⠀⠀⠀⣧⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⡀⠀⡇⣎⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠹⡄⠀⢠⡤⠴⠚⢧⡀⠁⣮⣴⣦⣀⡀⢠⠟⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠈⠶⢸⡋⠹⠿⢋⡇⠀⢿⡛⢿⣿⣷⡇⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⡞⠀⠀⠀⠀⠈⢉⠩⠟⠀⠀⠀⡿⠮⠉⠀⠙⡆⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠦⣀⠀⢧⡀⠀⠀⠀⠀⠀⢀⡤⠀⠀⠀⡇⠀⠀⢀⡼⠁⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠉⢹⠒⠢⢤⠀⢀⣾⢶⣆⠀⠀⣿⠀⡴⠋⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⢸⠀⠀⢸⠀⡜⠀⠀⣠⣍⣭⡈⡆⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡤⢤⠏⠀⠀⣸⠀⠀⠀⠀⠃⠰⣯⠴⠧⢾⡇⠀⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⣀⣤⠴⠒⠋⠉⠁⢰⠋⠀⠋⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠈⢲⠒⠚⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⣠⡴⠟⠉⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⢧⡀⠀⠀⠀⠀⠀⠀⠀⠢⠤⡀⠀⠙⣆⠀⠀⠀⠀⠀⠀")
    print("⣞⣁⣤⣄⣀⣀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⣀⠀⠀⠀⠀⠀⠀⣁⢀⣀⡼⣦⡀⠀⠀⠀⠀")
    print("⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠸⡄⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⡶⠀⠐⠚⢹⠍⠀⠀⠈⠋⠳⣄⠀⠀")
    print("⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠄⠀⠙⢆⢓⡇⡠⡀⠀⠀⠀⠀⠀⠀⢚⡁⠀⠀⣠⣎⠀⠀⠀⠀⠀⠀⠹⢷⡀")
    print(F"Te retiras del casino virtual con {DA} pesos")
elif DA == 0 and DU > 0:
    print("""                             ...----.... """)
    print("""                         ..-:"''         ''"-..""")
    print("""                      .-'                      '-.""")
    print("""                    .'              .     .       '.""")
    print("""                  .'   .          .    .      .    .''.""")
    print("""                .'  .    .       .   .   .     .   . ..:.""")
    print("""              .' .   . .  .       .   .   ..  .   . ....::.""")
    print("""             ..   .   .      .  .    .     .  ..  . ....:IA.""")
    print("""            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.""")
    print("""           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.""")
    print("""           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.""")
    print("""          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.""")
    print("""         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA""")
    print("""         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM""")
    print("""        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM""")
    print("""       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.""")
    print("""       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI""")
    print("""       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM""")
    print("""       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM""")
    print("""       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW""")
    print("""       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV""")
    print("""        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI""")
    print("""       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'""")
    print("""       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM""")
    print("""     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.""")
    print("""     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA""")
    print("""     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH""")
    print("""       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV" """)
    print("""        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM" """)
    print("""        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM""")
    print("""        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI""")
    print("""        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI""")
    print("""        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'""")
    print("""        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV""")
    print("""          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM""")
    print("""            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'""")
    print("""             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI""")
    print("""            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'""")
    print("""            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM""")
    print("""            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM""")
    print("""            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.""")
    print("""            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI""")
    print("""            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI""")
    print("""            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV" """)
    print("""              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'""")
    print("""               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM" """)
    print("""                 "::....::.:::..:..::IIIIIHHHHMMMHHMV" """)
    print("""                   "::.::.. .. .  ...:::IIHHMMMMHMV" """)
    print("""                     "V::... . .I::IHHMMV"'""")
    print("""                       '"VHVHHHAHHHHMMV:"'""")
    print("Sales del Casino Virtual sin dinero y con una deuda de {DU}")