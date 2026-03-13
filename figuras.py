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
            if calcular == 1:
                perimetro = float(input("Digite la medida de los lados:\n"))
                total_perimetro = perimetro * 3
                print(f"El perimetro de su triangulo equilatero es: {total_perimetro}")
            elif calcular == 2:
                a

        elif figura_2d == 2:
            print("¿Que desea calcular?")
            print("     1.Perimetro")
            print("     2.Area")
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
