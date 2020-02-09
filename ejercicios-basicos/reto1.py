
def suma_recursiva(numero, veces):
    if veces == 0:
        return 0
    else:
        return numero + suma_recursiva(numero, veces-1)


if __name__ == '__main__':
    print(suma_recursiva(800, 500))
