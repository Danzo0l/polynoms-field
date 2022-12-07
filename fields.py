import numpy as np


def polynom_field(polynom: np.poly1d, field: GF):
    arr = []
    for i in polynom:
        if i >= 0:
            arr.append(i % field.number)
        else:
            arr.append((field.number + i) % field.number)
    return np.poly1d(arr)





class GF:
    def __init__(self, number: int, power: int):
        self.number = number
        self.power = power
        self.value = self.number**self.power


class Fields:
    def __init__(self, field: GF, polynom: np.poly1d):
        self.polynom = polynom
        self.poly_field = []
        self.field = field
        self.basis_poly = []

    def polynom_field(self):
        arr = []
        for i in self.polynom:
            if i >= 0:
                arr.append(i % self.field.number)
            else:
                arr.append((self.field.number + i) % self.field.number)
        self.polynom = np.poly1d(arr)
        return np.poly1d(arr)

    def basic_polynom(self):
        counter = 0
        arr = []

        for i in self.polynom:
            if counter == 0 or i == 0:
                counter += 1
                continue
            arr.append(i)
        self.basis_poly = self.polynom_field()
        return self.polynom_field()

    def recalc_polynom(self):
        polynom = polynom_field(polynom, gf)
        print(polynom)
        # базовый полином - это когда полином в степени преобразуется
        base_poly = np.poly1d([2, 1])
        # множитель  - это будет a или (a+1), в зависимости от выбранного элемента
        mnozhitel = np.poly1d([1, 0])
        result_mul = np.polymul(polynom, mnozhitel)
        new_result = result_mul
        print("result multiply: \n", result_mul)
        if (len(result_mul) > 1):
            # replacer
            arr = []
            for i in result_mul:
                arr.append(i)
            bufer = arr[0]
            arr[0] = 0
            # new poly using in the end
            new_poly = np.poly1d(arr)
            poly_for_multiply = np.polymul(base_poly, np.poly1d(bufer))
            poly_for_multiply = polynom_field(poly_for_multiply, gf)
            print("poly_for_multiply: \n", poly_for_multiply)
            # base_poly * new_poly

            # new poly
            new_result = np.polyadd(poly_for_multiply, new_poly)
            new_result = polynom_field(new_result, gf)
        # print(bufer)
        print("result new: \n", new_result)

    def generate_dual_view(self):
        for i in range(len(self.polynom)):
            pass


a = GF(2, 4)
b = Fields(a, np.poly1d([3, 0, 0, 1]))
b.polynom_field()
compact_print(b.polynom)
