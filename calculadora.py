from menu import *
from calcular_2d import *
from calcular_3d import *

pi = 3.1416
tipo_figura = 0
tipo_figura = menu_principal()
while tipo_figura != 3:
    if tipo_figura == 1:
            escogio = 1
            while escogio==1:
                figura_2d = menu_2d()
                if figura_2d == 1:
                    calcular = menu_perimetro_area()
                    calculos_triangulo_equilatero(calcular) 
                elif figura_2d == 2:
                    calcular = menu_perimetro_area()
                    calculos_rectangulo(calcular)
                elif figura_2d == 3:
                    calcular = menu_perimetro_area()
                    calculos_circulo(calcular)
                elif figura_2d == 4: 
                    calcular = menu_perimetro_area()
                    calculos_hexagono (calcular)
                elif figura_2d == 5:
                    triangulo = datos_triangulo()
                    calculos_triangulo_rectangulo(triangulo)
                escogio = menu_escoger()
                if escogio==2:
                    tipo_figura=4
                elif escogio==3:
                    tipo_figura=3

    if tipo_figura == 2:
        escogio = 1
        while escogio ==1:
            figura_3d = menu_3d()
            if figura_3d == 1:
                calcular = menu_area_volumen()
                calculos_cubo(calcular)
            if figura_3d == 2:
                calcular = menu_area_volumen()
                calculos_esfera(calcular)
            if figura_3d == 3:
                calcular = menu_area_volumen()
                calculos_cilindro(calcular)
            if figura_3d == 4:
                calcular = menu_area_volumen()
                calculos_piramide(calcular)
            escogio = menu_escoger()
            if escogio==2:
                tipo_figura=4
            elif escogio==3:
                tipo_figura=3      

    if tipo_figura==4:
        tipo_figura = menu_principal()
    
print("Gracias por utilizar la calculadora")
