
def analizar_cadena():
    palabra = input("Ingrese una palabra: ").lower()
    cont = 0
    for letra in palabra: 
        if letra == "a":
            cont += 1 
        else: break
    if (cont*"a" + (2*cont)*"b" == palabra)and len(palabra)!=0:
        return print("\nLa palabra ingresada pertenece al Lenguaje")
    else:
        return print("\nLa palabra ingresada no pertenece al Lenguaje")


def analizar_cadena_pap():
    palabra = ""
    cant_a = 0
    cant_b = 0
    while True:
        caracter = input("ingrese un caracter: ").lower()
        if caracter == "":#SI DOY ENTER IMPRIMO PALABRA
            if 2*cant_a == cant_b:
                return print(f"\nPalabra: {palabra}")
            else: 
                return print("\nFALSE")
        elif len(caracter) > 1:#SI INGRESO MAS DE UN CARACTER PIDO DE NUEVO UN CARACTER
            print("\nDebe ingresar un solo caracter")
            continue
        elif caracter != "a" and caracter != "b":#SI UN CARACTER ES DISTINO DE A O B, IMPRIMO FALSE
            return print("FALSE")
        else: # UNA VEZ CONTROLADO LO BASICO PASO A LA PALABRA DEL LENGUAJE
            if caracter == "a" and ("b" not in palabra): #SI INGRESO UNA A, MIRO QUE NO HAYA B
                cant_a += 1 #CUENTO LA CANTIDAD DE A PARA LA CONDICION QUE SEAN EL DOBLE DE B QUE DE A
                palabra += caracter
            elif (caracter == "b") and (cant_b/2 < cant_a) and (cant_a > 0): 
                cant_b +=1
                palabra += caracter
            else: return print("FALSE")




