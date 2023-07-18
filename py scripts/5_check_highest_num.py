print("input three numbers to check which one is the highest!")
numero_uno = int(input("a: "))
numero_dos = int(input("b: "))
numero_tres = int(input("c: "))

comp_msg = " is greater than " #comparison message

if numero_uno > numero_dos and numero_tres:
    print(str(numero_uno) + comp_msg + str(numero_dos) + " and " + str(numero_tres))
elif numero_dos > numero_uno and numero_tres:
    print(str(numero_dos) + comp_msg + str(numero_uno) + " and " + str(numero_tres))
elif numero_tres > numero_uno and numero_dos:
    print(str(numero_tres) + comp_msg + str(numero_uno) + " and " + str(numero_dos))
elif numero_uno == numero_dos and numero_tres:
    print("Is this a joke? They are the same")