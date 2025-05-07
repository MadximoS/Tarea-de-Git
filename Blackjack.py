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
DA = int(input(Ingresa la cantidad de dinero en numeros))
print(f"Ingresaste {DA} pesos, estas seguro?")
input()
print("No importa ya esta depositado")
while DA >= 0:
    AV = False
    while AV == True:
        print("Ccuanto quieres apostar?")
        AC = input()
        if AC.isdigit():
            if AC > DA:
                print("No tienes el dinero suficiente para apostar esa cantidad, intentalo de nuevo")
            else:
                AV = True
        else:
            print("No entendi cuanto dinero quieres apostar asi que supondre que quieres apostar todo")
            AC = DA
            AV = True
        print(f"Tu apuesta es de {AC} pesos, ¿estas seguro?")
        input()
        print("Muy tarde para arrepentirse")
        C1 = random.randint(0, 13)
        if C1 == 0:
            C1 = joker
        elif C1 == 1:
            C1 = A
        elif C1 == 11:
            C1 = J
        elif C1 == 12:
            C1 = Q
        elif C1 == 13:
            C1 = K
        C2 = random.randint(0, 13)
        if C2 == 0:
            C2 = joker
        elif C2 == 1:
            C2 = A
        elif C2 == 11:
            C2 = J
        elif C2 == 12:
            C2 = Q
        elif C2 == 13:
            C2 = K
        print(f"tus cartas son C1 y C2")
        if C1 == A and C2 == K:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == A and C2 == Q:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == A and C2 == J:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == A and C2 == joker:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == K and C2 == A:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == Q and C2 == A:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == J and C2 == A:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == joker and C2 == A:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == joker and C2 == joker:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == joker and C2 == J:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == joker and C2 == Q:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == joker and C2 == K:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == J and C2 == joker:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == Q and C2 == joker:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        elif C1 == K and C2 == joker:
            AC = AC * 2
            DA += AC
            print("Blackjack, tu ganas")
            print(f"Tu dinero actual es de {DA}")
        else:
            if C1 == joker:
                V1 = 10
            elif C1 == A:
                V1 = 1
            elif C1 == J:
                V1 = 10
            elif C1 == Q:
                V1 = 10
            elif C1 == K:
                V1 = 10
            else:
                V1 = C1
            if C2 == joker:
                V2 = 10
            elif C2 == A:
                V2 = 1
            elif C2 == J:
                V2 = 10
            elif C2 == Q:
                V2 = 10
            elif C2 == K:
                V2 = 10
            else:
                V1 = C2
            VM = [V1, V2]
            while VA >= 21:
                VA = 0
                CC = len(VM)
                for i in range(0,CC):
                    VA += VM[i]
                print(f"El valor de tus cartas es de {VA}, ¿Quieres quedarte o robar?")
                print("Escribe textualmente: me quedo o robo")
                Is = input("me quedo / robo")
                if Is == robo:
                    C = random.randint(1, 13)
                    if C == 0:
                        print("Te salio un Joker")
                        VM += C
                        VA += C
                    elif C1 == 1:
                        C1 = A
                    elif C1 == 11:
                        C1 = J
                    elif C1 == 12:
                        C1 = Q
                    elif C1 == 13:
                        C1 = K