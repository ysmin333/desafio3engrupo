print("AGENDA")
print("1.Nuevo contacto")
print("2.Buscar contacto")
print("3.Ver la agenda")
agenda={}
while True:
    n=int(input("Opción número[1/2/3]:-"))
    if n==1:
        nombre=input("Nombre: ")
        telefono=int(input("Numero de teléfono: "))
        agenda[nombre]=telefono
    elif n==2:
        nombre=input("Buscar nombre: ")
        print ("El número de teléfono de ",nombre," es ",agenda[nombre])
    else:
        print (agenda)
        break 