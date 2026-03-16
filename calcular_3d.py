def calculos_cubo(calcular):
    try:
        lados = float(input("Digite la medida de los lados:\n "))
        if calcular == 1:
            volumen = lados **3
            print(f"El volumen de su cubo es:{volumen:.2f}")
        elif calcular == 2:
            area = 6 * (lados**2)
            print(f"El area de su cubo es:{area:.2f}")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_esfera(calcular):
    pi = 3.1416
    try:
        radio = float(input("Digite la medida del radio:\n "))
        if calcular == 1:
            volumen = (4/3) * pi * (radio**3)
            print(f"El volumen de su esfera es:{volumen:.2f}")
        elif calcular == 2:
            area = 4 * pi * (radio**2)
            print(f"El area de su esfera es:{area:.2f}")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_cilindro(calcular):
    pi = 3.1416
    try:
        radio = float(input("Digite la medida del radio:\n "))
        altura = float(input("Digite la medida de su altura:\n "))
        if calcular == 1:
            volumen = pi * (radio**2) * altura
            print(f"El volumen de su cilindro es:{volumen:.2f}")
        elif calcular == 2:
            area = (2*pi) * radio * (altura + radio)
            print(f"El area de su cilindro es:{area:.2f}")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

def calculos_piramide(calcular):
    try:
        lado = float(input("Digite el lado de la base cuadrada:\n "))
        altura = float(input("Digite la medida de su altura:\n "))
        area_base = lado**2
        if calcular == 1:
            volumen = (area_base * altura) / 3
            print(f"El volumen de su piramide es:{volumen:.2f}")
        elif calcular == 2:
            apontema = ((altura**2)+((lado/2))**2)**(1/2)
            perimetro = lado * 4
            area = area_base + ((perimetro * apontema) / 2)
            print(f"El area de su piramide es:{area:.2f}")
    except ValueError:
        print("El tipo de dato ingresado no es valido\n")

