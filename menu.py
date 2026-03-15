def menu_principal ():
    print("--- CALCULADORA GEOMETRICA ---")
    print("       1. Figura en 2D")
    print("       2. Figura en 3D")
    print("       3. Salir")

    tipo_figura = int(input("Digite el numero referente a la figura que desea:\n"))
    return tipo_figura

def menu_2d ():
    print("--- Figuras 2D ---")
    print("   1.Triángulo equilatero")
    print("   2.Rectángulo")
    print("   3.Círculo")
    print("   4.Hexágono")
    print("   5.Triángulo rectangulo")

    figura_2d = int(input("Seleccione la figura geometrica:\n"))
    return figura_2d

def menu_3d ():
    print("--- Figuras 3D ---")
    print("     1.Cubo")
    print("     2.Esfera")
    print("     3.Cilindro")
    print("     4.Pirámide")
    
    figura_3d = int(input("Seleccione la figura geometrica:\n"))
    return figura_3d

def menu_perimetro_area ():
    print("¿Que desea calcular?")
    print("     1.Perimetro")
    print("     2.Area")

    calcular = int(input("Seleccione una opción:\n"))
    return calcular


def menu_triangulo_rectangulo ():
    print("¿Que desea calcular?")
    print("     1.Perimetro")
    print("     2.Area")
    print("     3.Angulos")

    triangulo = int(input("Seleccione una opción:\n"))
    return triangulo
