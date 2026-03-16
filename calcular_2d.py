def calculos_triangulo_equilatero(calcular):

    try:
        lados = float(input("Digite la medida de los lados:\n"))
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
        radio = float(input("Digite el radio"))
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
        if calcular == 1:
            total_perimetro = lado * 6
            print(f"El perimetro de su hexágono es:{total_perimetro:.2f}\n")
        elif calcular == 2:
            area = ((3*(3**(1/2)))/2) * lado**2
            print(f"El area de su hexágono es:{area:.2f}\n")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_triangulo_rectangulo(triangulo):
    try:
        if triangulo == 1:
            base = float(input("Digite la medida de su base:\n"))
            altura = float(input("Digite la medida de su altura:\n"))
            hipotenusa = ((altura**2)+(base**2))**(1/2)
            total_perimetro = altura + base + hipotenusa
            print(f"El perimetro de su triangulo rectangulo es:{total_perimetro:.2f}\n")
        elif triangulo == 2:
            base = float(input("Digite la medida de su base:\n"))
            altura = float(input("Digite la medida de su altura:\n"))
            area = (base*altura)/2
            print(f"El area de su triangulo rectangulo es:{area:.2f}\n")
        elif triangulo == 3:
            angulo = float(input("Digite un angulo:\n"))
            angulos = 90 - angulo 
            if angulo > 90:
                print("El angulo no puede ser mayor a 90°")
            else:
                print((f"Sus angulos son: 90°, {angulos:.2f°}, {angulo:.2f}°\n"))     
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")


