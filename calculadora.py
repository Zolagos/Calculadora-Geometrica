from menu import menu_principal, menu_2d, menu_3d, menu_perimetro_area
from menu import menu_triangulo_rectangulo, menu_escoger, menu_area_volumen
from calcular_2d import calculos_triangulo_equilatero,calculos_rectangulo,calculos_circulo 
from calcular_2d import calculos_hexagono, calculos_triangulo_rectangulo
from calcular_3d import calculos_cubo, calculos_esfera, calculos_cilindro, calculos_piramide

pi = 3.1416
tipo_figura = 0
while tipo_figura != 3:
    tipo_figura = menu_principal()
    if tipo_figura == 1:
        figura_2d = menu_2d()
        if figura_2d == 1:
            calcular = menu_perimetro_area()
            calculos_triangulo_equilatero(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_2d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        elif figura_2d == 2:
            calcular = menu_perimetro_area()
            calculos_rectangulo(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_2d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        elif figura_2d == 3:
            calcular = menu_perimetro_area()
            calculos_circulo(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_2d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        elif figura_2d == 4: 
            calcular = menu_perimetro_area()
            calculos_hexagono (calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_2d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        elif figura_2d == 5:
            triangulo = menu_triangulo_rectangulo()
            calculos_triangulo_rectangulo(triangulo)
            escoger = menu_escoger()
            if escoger == 1:
                menu_2d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3

    if tipo_figura == 2:
        figura_3d = menu_3d
        if figura_3d == 1:
            calcular = menu_area_volumen()
            calculos_cubo(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_3d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        if figura_3d == 2:
            calcular = menu_area_volumen()
            calculos_esfera(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_3d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        if figura_3d == 3:
            calcular = menu_area_volumen()
            calculos_cilindro(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_3d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3
        if figura_3d == 4:
            calcular = menu_area_volumen()
            calculos_piramide(calcular)
            escoger = menu_escoger()
            if escoger == 1:
                menu_3d()
            elif escoger == 2:
                menu_principal()
            elif escoger == 3:
                print("Gracias por utilizar la calculadora")
                tipo_figura = 3

    if tipo_figura == 3:
        print("Gracias por utilizar la calculadora")

