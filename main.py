# This is a sample Python script.
import numpy as np
import sympy as sp


# ░██████╗░██╗░░░██╗░█████╗░██╗░░██╗██╗
# ██╔════╝░██║░░░██║██╔══██╗██║░░██║██║
# ██║░░██╗░██║░░░██║██║░░╚═╝███████║██║
# ██║░░╚██╗██║░░░██║██║░░██╗██╔══██║██║
# ╚██████╔╝╚██████╔╝╚█████╔╝██║░░██║██║
# ░╚═════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝
# ╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮
# ╱╱╱╱╱╱┃┃╱╱╱╱╱╱┃┃╱╱╭╯╰╮
# ╭━━┳━━┫┃╭━━┳╮╭┫┃╭━┻╮╭╋━━┳━╮
# ┃╭━┫╭╮┃┃┃╭━┫┃┃┃┃┃╭╮┃┃┃╭╮┃╭╯
# ┃╰━┫╭╮┃╰┫╰━┫╰╯┃╰┫╭╮┃╰┫╰╯┃┃
# ╰━━┻╯╰┻━┻━━┻━━┻━┻╯╰┻━┻━━┻╯
class GF:
    def __init__(self, number: int, power: int):
        self.number = number
        self.power = power
        self.value = self.number**self.power


class InputData:
    def __init__(self, polynom: list, field: GF, parametr: int):
        self.polynom = np.poly1d(polynom)
        self.field = field
        self.parametr = parametr


def compact_print(polynom: np.poly1d, parametr: int):
    sec_part = ''
    opened = ''
    closed = ''
    if parametr > 0:
        sec_part = '+' + str(parametr)
        opened = '('
        closed = ')'
    counter = np.count_nonzero(polynom, axis=None)
    if counter == 0:
        print(0, end="")
    variable = polynom.variable
    poly = len(polynom)
    for i in polynom:
        if i == 0:
            poly -= 1
            continue
        elif poly == 1:
            print(opened + str(i) + variable + sec_part + closed, end="")
            counter -= 1
            poly -= 1
        elif poly > 1:
            print(opened + str(i) + variable + sec_part + closed + "^" + str(poly), end="")
            counter -= 1
            poly -= 1
        elif poly == 0:
            print(str(i), end="")
            counter -= 1
            poly -= 1
        if poly >= 0:
            if counter != 0:
                print(" + ", end="")


def uproshausha_function(polynom: np.poly1d, base_poly: np.poly1d, field: GF, start_polynom: np.poly1d, variable: str):
    l_polynom = polynom_field(polynom, field, variable)
    # base_poly - это когда полином в степени преобразуется
    # mnozhitel  - это будет a или (a+1), в зависимости от выбранного элемента
    result_mul = polynom
    new_result = result_mul
    # print(result_mul)
    if len(result_mul) >= len(start_polynom):
        # replacer
        arr = []
        for i in result_mul:
            arr.append(i)
        # bufer - for multiply base_poly
        bufer = arr[0]
        arr[0] = 0
        # new poly using in the end in ADD
        new_poly = np.poly1d(arr, variable=variable)
        poly_for_multiply = np.polymul(base_poly, np.poly1d(bufer, variable=variable))
        poly_for_multiply = polynom_field(poly_for_multiply, gf, variable)
        # base_poly * new_poly
        new_result = np.polyadd(poly_for_multiply, new_poly)
        new_result = polynom_field(new_result, gf, variable)

    return new_result


def basic_polynom(polynom: np.poly1d, field: GF, variable: str):
    counter = 0
    arr = []

    for i in polynom:
        if counter == 0 or i == 0:
            counter += 1
            continue
        arr.append(-i)
    return polynom_field(np.poly1d(arr, variable=variable), field, variable)


def polynom_field(polynom: np.poly1d, field: GF, variable: str):
    arr = []
    for i in polynom:
        if i >= 0:
            arr.append(i % field.number)
        else:
            arr.append((field.number + i) % field.number)
    return np.poly1d(arr, variable=variable)


def recalc_polynom(polynom: np.poly1d, base_poly: np.poly1d, mnozhitel: np.poly1d,
                   field: GF, start_polynom: np.poly1d, variable: str):
    l_polynom = polynom_field(polynom, field, variable)
    # base_poly - это когда полином в степени преобразуется
    # mnozhitel  - это будет a или (a+1), в зависимости от выбранного элемента
    result_mul = np.polymul(l_polynom, mnozhitel)
    new_result = result_mul
    # print(result_mul)
    if len(result_mul) >= len(start_polynom):
        # replacer
        arr = []
        for i in result_mul:
            arr.append(i)
        # bufer - for multiply base_poly
        bufer = arr[0]
        arr[0] = 0
        # new poly using in the end in ADD
        new_poly = np.poly1d(arr, variable=variable)
        poly_for_multiply = np.polymul(base_poly, np.poly1d(bufer, variable=variable))
        poly_for_multiply = polynom_field(poly_for_multiply, gf, variable)
        # base_poly * new_poly
        new_result = np.polyadd(poly_for_multiply, new_poly)
        new_result = polynom_field(new_result, gf, variable)
    return new_result


def generate_dual_view(polynom: np.poly1d, field: GF, mnozhitel: np.poly, variable: str):
    base_poly = basic_polynom(polynom, field, variable)
    dual_view = []
    counter = 0
    current_poly = 0
    prev_polynom = 0
    print("========================\nPOLYNOM:", end=" ")
    compact_print(polynom, 0)
    print("\nGF (" + str(field.number) + "^" + str(field.power) + ")\n========================")
    for i in range(field.value + 1):
        dual_view_elem = []
        # first append
        dual_view_elem.append("a" + str(i))
        if i == 0: current_poly = np.poly1d(0, variable=variable)
        elif i == 1: current_poly = np.poly1d(1, variable=variable)
        elif i == 2: current_poly = np.poly1d([1, 0], variable=variable)
        dual_view_elem.append(current_poly)
        # print(current_poly)
        # second append

        if i < len(polynom)+1:
            # third append
            dual_view_elem.append(current_poly)
            prev_polynom = current_poly
        else:
            new_poly = recalc_polynom(prev_polynom, base_poly, mnozhitel, field, polynom, variable)
            prev_polynom = new_poly
            # third append
            dual_view_elem.append(new_poly)
        current_poly = np.polymul(current_poly, mnozhitel)
        # dual_view_elem.append(current_poly)
        # print(dual_view_elem)
        dual_view.append(dual_view_elem)
        counter += 1

    for i in dual_view:
        if (i[2] == np.poly1d(1)) and (i[1] != np.poly1d(1)) and (i[0] != "a"+str(counter-1)):
            print(end="\033[31m")
        print(i[0], end="\t\t |")
        compact_print(i[1], 0)
        if i[1] == np.poly1d(0) or i[1] == np.poly1d(1):
            print(end=" \t\t| ")
        else:
            print(end="\t\t| ")
        compact_print(i[2], 0)
        print(end="\033[0m\n")

    return dual_view


def generate_dual_views(polynom: np.poly1d, field: GF, mnozhitel: np.poly, variable: str, parametr: int):
    base_poly = basic_polynom(polynom, field, variable)
    dual_view = []
    counter = 0
    current_poly = 0
    prev_polynom = 0
    rashet_poly = np.poly1d([1, parametr])
    print(base_poly)
    print("========================\nPOLYNOM:", end=" ")
    compact_print(polynom, 0)
    print("\nGF (" + str(field.number) + "^" + str(field.power) + ")\n========================")
    for i in range(field.value + 1):
        dual_view_elem = []
        # first append
        dual_view_elem.append("a" + str(i))
        if i == 0: current_poly = np.poly1d(0, variable=variable)
        elif i == 1: current_poly = np.poly1d(1, variable=variable)
        elif i == 2: current_poly = np.poly1d([1, 0], variable=variable)
        # second append
        dual_view_elem.append(current_poly)
        # print(current_poly)


        if i <= len(polynom):
            # third append

            if (parametr != 0) and (i == len(polynom)):
                poly = converter_polynomov(dual_view_elem[1], parametr)
                poly = polynom_field(poly, field, variable)
                dual_view_elem.append(poly)
            else:
                dual_view_elem.append(current_poly)
                prev_polynom = rashet_poly


        else:
            new_poly = 0
            if parametr != 0:
                new_poly = converter_polynomov(current_poly, parametr)
                new_poly = recalc_polynom(prev_polynom, base_poly, rashet_poly, field, polynom, variable)
            else:
                new_poly = recalc_polynom(prev_polynom, base_poly, current_poly, field, polynom, variable)
            # new_poly = np.polymul(converter_polynomov(current_poly, parametr), rashet_poly)
            # new_poly = polynom_field(new_poly, field, variable)
            # new_poly = uproshausha_function(new_poly, base_poly, field, polynom, variable)
            prev_polynom = new_poly
            # third append
            dual_view_elem.append(new_poly)
            # rashet_poly = np.polymul(current_poly, mnozhitel)
        current_poly = np.polymul(current_poly, mnozhitel)
        # dual_view_elem.append(current_poly)
        # print(dual_view_elem)
        dual_view.append(dual_view_elem)
        counter += 1

    for i in dual_view:
        if (i[2] == np.poly1d(1)) and (i[1] != np.poly1d(1)) and (i[0] != "a"+str(counter-1)):
            print(end="\033[31m")
        print(i[0], end="\t\t |")
        compact_print(i[1], parametr)
        if i[1] == np.poly1d(0) or i[1] == np.poly1d(1):
            print(end=" \t\t| ")
        else:
            print(end="\t\t| ")
        compact_print(i[2], 0)
        print(end="\033[0m\n")

    return dual_view


def converter_polynomov(polynom: np.poly1d, parametr: int):
    arr = []
    variable = "x+" + str(parametr)
    stepen = len(polynom)
    str_poly = ''
    for i in polynom: arr.append(i)
    for i in arr:
        str_poly += str(i) + "*(" + variable + ")**" + str(stepen) + "+"
        stepen -= 1
    str_poly = str_poly[:-1]
    x = sp.Symbol('x')
    raschet = str(eval(str_poly).expand()).replace(' ', '')
    coeffs = sp.Poly(raschet, x).all_coeffs()
    # print(sp.Poly(raschet, x).all_coeffs())
    # print(eval(raschet).coeff(x**4))
    return np.poly1d(coeffs)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("ENTER GF expample(3^2): ", end="")
    g_field = input()
    gf = GF(int(g_field[0]), int(g_field[2]))
    print("\033[32m ENTER SENOIR COEFFICIENT: \033[0m", end="")
    steps = int(input())
    print("\033[33m ENTER POLYNOM/ example(x^0+x^1+x^2...): \033[0m")
    poly_arr = []
    for i in range(steps+1):
        print("x^"+str(steps-i) + "*", end="")
        elem_poly = int(input())
        poly_arr.append(elem_poly)
    poly_arr = poly_arr[::-1]
    print("\033[34m ENTER a-ELEM: \033[0ma + ", end="")
    premitiv = int(input())

    inputing = InputData(poly_arr, gf, premitiv)

    if inputing.parametr == 0:
        generate_dual_view(inputing.polynom, inputing.field, np.poly1d([1, 0], variable="x"), "x")
    else:
        generate_dual_views(inputing.polynom, inputing.field, np.poly1d([1, 0], variable="x"), "x", inputing.parametr)
    # polynom = np.poly1d([1, 1, 1], variable="x")
    # gf = GF(5, 2)
    # generate_dual_view(polynom, gf, np.poly1d([1, 0], variable="x"), "x")

    # x = sp.Symbol('x')
    # a = eval('(x+2)**2 + 1')
    # print(str(a.expand()))

    # polynom1 = np.poly1d([1, 0, 1])
    # print(polynom1)
    # print(converter_polynomov(polynom1, 0))
    # x**2 + 2*x + 1
