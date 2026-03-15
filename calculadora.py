from menu import menu_principal, menu_2d, menu_3d, menu_perimetro_area, menu_triangulo_rectangulo

pi = 3.1416
tipo_figura = 0
while tipo_figura != 3:
    try:
        tipo_figura = menu_principal()
        if tipo_figura == 1:
            figura_2d = menu_2d()
            if figura_2d == 1:
                calcular = menu_perimetro_area()
                lados = float(input("Digite la medida de los lados:\n"))
                if calcular == 1:
                    total_perimetro = lados * 3
                    print(f"El perimetro de su triangulo equilatero es: {total_perimetro}\n")
                elif calcular == 2:
                    area = ((3**(1/2))/4)*(lados**2)
                    print(f"El área de su triangulo equilatero es:{area}\n")
            elif figura_2d == 2:
                calcular = menu_perimetro_area()
                lado_a = float(input("Digite la medida del lado a:\n"))
                lado_b = float(input("Digite la medida del lado b:\n"))
                if calcular == 1:
                    total_perimetro = 2*(lado_a+lado_b)
                    print(f"El perimetro de su rectángulo es:{total_perimetro}\n")
                elif calcular == 2:
                    area = lado_a * lado_b
                    print(f"El area de su rectángulo es:{area}\n")
            elif figura_2d == 3:
                calcular = menu_perimetro_area()
                radio = float(input("Digite el radio"))
                if calcular == 1:
                    total_perimetro = 2 * pi * radio
                    print(f"El perimetro de su circulo es:{total_perimetro}\n")
                elif calcular == 2:
                    area = pi * (radio**2)
                    print(f"El area de su circulo es:{area}\n")
            elif figura_2d == 4: 
                calcular = menu_perimetro_area()
                lado = float(input("Digite la medida del lado:\n"))
                if calcular == 1:
                    total_perimetro = lado * 6
                    print(f"El perimetro de su hexágono es:{total_perimetro}\n")
                elif calcular == 2:
                    area = ((3*(3**(1/2)))/2) * lado**2
                    print(f"El area de su hexágono es:{area}\n")
            elif figura_2d == 5:
                triangulo = menu_triangulo_rectangulo()
                base = float(input("Digite la medida de su base:\n"))
                altura = float(input("Digite la medida de su altura:\n"))
                hipotenusa = ((altura**2)+(base**2))**(1/2)
                if triangulo == 1:
                    total_perimetro = altura + base + hipotenusa
                    print(f"El perimetro de su triangulo rectangulo es:{total_perimetro}\n")
                elif triangulo == 2:
                    area = (base*altura)/2
                    print(f"El area de su triangulo rectangulo es:{area}\n")
    except:
        print("El dato ingresado no es valido\n")            





