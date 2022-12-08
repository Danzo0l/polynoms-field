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


def basic_polynom():
    pass


def polynom_field():
    pass


def uproshausha_function():
    pass


def generate_dual_view():
    pass


if __name__ == '__main__':
    p = sp.Poly("x+1")
    g = sp.Poly("x+1")
    print(str(g*p))