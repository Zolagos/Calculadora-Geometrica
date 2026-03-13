op = ""
while op!=2:
    print("--- CALCULADORA GEOMETRICA ---")
    print("       1. Figura en 2D")
    print("       2. Figura en 3D")
    print("       3. Salir")

    op = int(input("Seleccione una opcion:\n"))
    if op == 1:
        print("--- Figuras 2D ---")
        print("   1.Triángulo equilatero")
        print("   2.Rectángulo")
        print("   3.Círculo")
        print("   4.Pentágono")
        print("   5.Triángulo rectangulo")
        figura_2d = int(input("Seleccione una opcion:\n"))
        if figura_2d == 1:
            print("¿Que desea calcular?")
            print("     1.Perimetro")
            print("     2.Area")
            calcular = int(input("Seleccione una opción:\n"))
            lados = float(input("Digite la medida de los lados:\n"))
            if calcular == 1:
                total_perimetro = lados * 3
                print(f"El perimetro de su triangulo equilatero es: {total_perimetro}")
            elif calcular == 2:
                area = ((3**(1/2))/4)*(lados**2)
                print(f"El área de su triangulo equilatero es:{area}")
        elif figura_2d == 2:
            print("¿Que desea calcular?")
            print("     1.Perimetro")
            print("     2.Area")
            calcular = int(input("Seleccione una opción:\n"))
            lado_a = float(input("Digite la medida del lado a:\n"))
            lado_b = float(input("Digite la medida del lado b:\n"))
            if calcular == 1:
                total_perimetro = 2*(lado_a+lado_b)
                print(f"El perimetro de su rectángulo es:{total_perimetro}")
            elif calcular == 2:
                area = lado_a * lado_b
                print(f"El area de su rectángulo es:{area}")
        elif figura_2d == 3:
            print("¿Que desea calcular?")
            print("     1.Perimetro")
            print("     2.Area")
        elif figura_2d == 4:
            print("¿Que desea calcular?")
            print("     1.Perimetro")
            print("     2.Area")
        elif figura_2d == 5:
            d
    elif op == 2:
        print("--- Figuras 3D ---")
        print("     1.Cubo")
        print("     2.Esfera")
        print("     3.Cilindro")
        print("     4.Pirámide")
