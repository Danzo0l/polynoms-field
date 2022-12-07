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


def compact_print(polynom: np.poly1d):
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
            print(str(i) + variable, end="")
            counter -= 1
            poly -= 1
        elif poly > 1:
            print(str(i) + variable + "^" + str(poly), end="")
            counter -= 1
            poly -= 1
        elif poly == 0:
            print(str(i), end="")
            counter -= 1
            poly -= 1
        if poly >= 0:
            if counter != 0:
                print(" + ", end="")


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
    compact_print(polynom)
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
        compact_print(i[1])
        if i[1] == np.poly1d(0) or i[1] == np.poly1d(1):
            print(end=" \t\t| ")
        else:
            print(end="\t\t| ")
        compact_print(i[2])
        print(end="\033[0m\n")

    return dual_view


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    polynom = np.poly1d([1, 1, 2], variable="x")
    gf = GF(3, 2)
    generate_dual_view(polynom, gf, np.poly1d([1, 0], variable="x"), "x")
    x = sp.Symbol('x')
    a = (x+1)**4
    res = np.polymul(np.poly1d([2, 0]), np.poly1d([1, 1]))
    print(polynom_field(res, gf, "x"))
