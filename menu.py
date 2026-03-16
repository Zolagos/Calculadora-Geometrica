def menu_principal ():
    cond = False
    while not cond:
        print("--- CALCULADORA GEOMETRICA ---")
        print("       1. Figura en 2D")
        print("       2. Figura en 3D")
        print("       3. Salir")
        
        try:
            tipo_figura = int(input("Digite el numero referente a la figura que desea:\n"))
            if tipo_figura !=1 and tipo_figura !=2 and tipo_figura !=3:
                print("El numero ingresado no es valido\n")
                cond = False
            else:
                cond = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return tipo_figura

def menu_2d ():
    con = False
    while not con:
        print("--- Figuras 2D ---")
        print("   1.Triángulo equilatero")
        print("   2.Rectángulo")
        print("   3.Círculo")
        print("   4.Hexágono")
        print("   5.Triángulo rectangulo")
        try:   
            figura_2d = int(input("Seleccione la figura geometrica:\n"))
            if figura_2d !=1 and figura_2d !=2 and figura_2d !=3 and figura_2d !=4 and figura_2d !=5:
                print("El numero ingresado no es valido\n")
                con = False
            else:
                con = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return figura_2d

def menu_3d ():
    cond = False
    while not cond:
        print("--- Figuras 3D ---")
        print("     1.Cubo")
        print("     2.Esfera")
        print("     3.Cilindro")
        print("     4.Pirámide")
        try:
            figura_3d = int(input("Seleccione la figura geometrica:\n"))
            if figura_3d !=1 and figura_3d !=2 and figura_3d !=3 and figura_3d !=4:
                print("El numero ingresado no es valido\n")
                cond = False
            else:
                cond = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return figura_3d

def menu_perimetro_area ():
    con = False
    while not con:
        print("¿Que desea calcular?")
        print("     1.Perimetro")
        print("     2.Area")
        try:
            calcular = int(input("Seleccione una opción:\n"))
            if calcular !=1 and calcular !=2:
                print("El numero ingresado no es valido\n")
                con = False
            else:
                con = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return calcular


def menu_triangulo_rectangulo ():
    cond = False
    while not cond:
        print("¿Que desea calcular?")
        print("     1.Perimetro")
        print("     2.Area")
        print("     3.Angulos")
        try:
            triangulo = int(input("Seleccione una opción:\n"))
            if triangulo !=1 and triangulo !=2 and triangulo !=3:
                print("El numero ingresado no es valido\n")
                cond = False
            else:
                cond = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return triangulo

def menu_escoger():
    con = False
    while not con:
        print("¿Que desea hacer?")
        print("1.Escoger otra figura")
        print("2.Volver al menu principal")
        print("3.Salir")
        try:
            escoger = int(input("Seleccione una opción:\n"))
            if escoger !=1 and escoger !=2 and escoger !=3:
               print("El numero ingresado no es valido\n")
               con = False
            else:
                con = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return escoger

def menu_area_volumen():
    cond = False
    while not cond:
        print("¿Que desea calcular?")
        print("     1.Volumen")
        print("     2.Area")
        try:
            calcular = int(input("Seleccione una opción:\n"))
            if calcular !=1 and calcular !=2:
                print("El numero ingresado no es valido\n")
                con = False
            else:
                con = True
        except ValueError:
            print("El tipo de dato ingresado no es un entero\n")
    return calcular
