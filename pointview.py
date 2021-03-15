import sys

if len(sys.argv) == 3:
    import graficador as g
    g.graficarKMeans(int(sys.argv[1]), int(sys.argv[2]))

else:
    print("Uso >>>")
    print("\tpython3 graficador.py <cantidad de vectores en R2> <k>")
