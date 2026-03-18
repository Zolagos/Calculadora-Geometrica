def calculos_triangulo_equilatero(calcular):
    try:
        lados = float(input("Digite la medida de los lados:\n"))
        if lados <=0:
            print("No se puede numeros negativos")
            raise ValueError
        if calcular == 1:
            total_perimetro = lados * 3
            print(f"El perimetro de su triangulo equilatero es: {total_perimetro:.2f}\n")
        elif calcular == 2:
            area = ((3**(1/2))/4)*(lados**2)
            print(f"El área de su triangulo equilatero es:{area:.2f}\n")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_rectangulo(calcular):
    try:
        lado_a = float(input("Digite la medida del lado a:\n"))
        lado_b = float(input("Digite la medida del lado b:\n"))
        if lado_a <= 0 or lado_b <=0:
            print("No se puede numeros negativos")
            raise ValueError
        if calcular == 1:
            total_perimetro = 2*(lado_a+lado_b)
            print(f"El perimetro de su rectángulo es:{total_perimetro:.2f}\n")
        elif calcular == 2:
            area = lado_a * lado_b
            print(f"El area de su rectángulo es:{area:.2f}\n")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_circulo(calcular):
    pi = 3.1416
    try:
        radio = float(input("Digite el radio\n"))
        if radio <=0:
            print("No se puede numeros negativos")
            raise ValueError
        if calcular == 1:
            total_perimetro = 2 * pi * radio
            print(f"El perimetro de su circulo es:{total_perimetro:.2f}\n")
        elif calcular == 2:
            area = pi * (radio**2)
            print(f"El area de su circulo es:{area:.2f}\n")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_hexagono (calcular):
    try:
        lado = float(input("Digite la medida del lado:\n"))
        if lado <= 0:
            print("No se puede numeros negativos")
            raise ValueError
        if calcular == 1:
            total_perimetro = lado * 6
            print(f"El perimetro de su hexágono es:{total_perimetro:.2f}\n")
        elif calcular == 2:
            area = ((3*(3**(1/2)))/2) * lado**2
            print(f"El area de su hexágono es:{area:.2f}\n")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_triangulo_rectangulo(triangulo):
    valido = False
    while not valido:
        try:
            base = 0
            altura = 0
            hipotenusa = 0
            valido = True
            if triangulo == 1:
                base = float(input("Digite la medida de su C. Opuesto:\n"))
                altura = float(input("Digite la medida de su C. Adyacente:\n"))
                hipotenusa = ((altura**2)+(base**2))**(1/2)
                total_perimetro = altura + base + hipotenusa
                area = (base*altura)/2
                print(f"El perimetro de su triangulo rectangulo es:{total_perimetro:.2f}")
                print(f"La hipotenusa es:{hipotenusa:.2f}\n")
                print(f"El area de su triangulo rectangulo es:{area:.2f}\n")
            elif triangulo == 2:
                altura = float(input("Digite la medida de su C. Adyacente:\n"))
                hipotenusa = float(input("Digite la medida de su hipotenusa:\n"))
                if hipotenusa <= altura:
                    print("La hipotenusa debe ser mayor que el C. Adyacente\n")
                    valido = False
                else:
                    base = (hipotenusa**2 - altura**2)**(1/2)
                    area = (base*altura)/2
                    total_perimetro = altura + base + hipotenusa
                print(f"El perimetro de su triangulo rectangulo es:{total_perimetro:.2f}")
                print(f"El C. Opuesto de su triangulo rectangulo es:{base:.2f}")
                print(f"El area de su triangulo rectangulo es:{area:.2f}\n")
            elif triangulo == 3:
                base = float(input("Digite la medida de su C. Opuesto:\n"))
                hipotenusa = float(input("Digite la medida de su hipotenusa:\n"))
                if hipotenusa <= base:
                    print("La hipotenusa debe ser mayor que el C. Opuesto\n")
                    valido = False
                else:
                    altura = (hipotenusa**2 - base**2)**(1/2)
                    area = (base*altura)/2
                    total_perimetro = altura + base + hipotenusa
                print(f"El perimetro de su triangulo rectangulo es:{total_perimetro:.2f}")
                print(f"El C. Adyacente de su triangulo rectangulo es:{base:.2f}")
                print(f"El area de su triangulo rectangulo es:{area:.2f}\n")
            elif triangulo == 4:
                angulo = float(input("Digite su angulo:\n"))
                angulos = 90 - angulo
                if angulo >= 90 or angulo <= 0:
                    print("El angulo ingresado debe ser mayor a 0 y menor a 90°\n")
                else:
                    print(f"Sus angulos son: 90°, {angulo:.2f}, {angulos:.2f}\n")
        except ValueError:
            print("El tipo de dato ingresado no es valido\n")


