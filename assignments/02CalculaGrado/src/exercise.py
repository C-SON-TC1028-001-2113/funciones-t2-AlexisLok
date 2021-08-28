def calcula_grado(val):
    if val >= 0.9 and val <= 1:
        return 'A'
        pass
    elif val > 0.8 and val <= 0.9:
        return 'B'
        pass
    elif val > 0.7 and val <= 0.8:
        return 'C'
        pass
    elif val > 0.6 and val <= 0.7:
        return 'D'
        pass
    elif val >= 0 and val <= 0.6:
        return 'F'
        pass
    else:
        return 'score incorrecto'
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
