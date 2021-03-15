import turtle
import clustering as clus


colores = ["green","blue","orange","orchid","cyan","pink","yellow","purple","crimson","brown","red","black","white"]
ventana = turtle.Screen()
ventana.setup(500, 500, 400, 200)
ventana.title("Tarea programada, parte 1")
tortu = turtle.Turtle()
tortu.speed(0)
s = 240
escala = 5


def dibujar_punto(a, b, color):
    '''
    Dibuja un punto en el plano cartesiano del color seleccionado
    '''
    tortu.color(colores[color])
    tortu.pensize(3)
    tortu.speed(1)
    tortu.ht()
    tortu.penup()
    tortu.setpos(a * 3, b * 3)
    tortu.pendown()
    tortu.dot(8)


def graficar_puntos(puntos):
    '''
    Grafica en negro todos los puntos del espacio
    '''
    for i in range(0, len(puntos)):
        dibujar_punto(puntos[i][0], puntos[i][1], colores.index("black"))


def graficar_grupos(puntos, matriz):
    '''
    Grafica en color los grupos de vectores
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                dibujar_punto(puntos[j][0], puntos[j][1], i)


def graficar_reps(reps):
    '''
    Grafica los representantes (centroides)
    '''
    for e in range(len(reps)):
        dibujar_punto(reps[e][0], reps[e][1], colores.index("red"))


def limpiarReps(reps):
    '''
    Marca en blanco los antiguos centroides
    '''
    for e in range(len(reps)):
        dibujar_punto(reps[e][0], reps[e][1], colores.index("white"))


def escribir_k(p):
    '''
    Escribe en la esquina superior izquierda del plano el area del poligono
    '''
    salida = "K optimo: "
    k = clus.calcularRk(p)
    tortu.color("black")
    tortu.speed(0)
    tortu.penup()
    tortu.setpos(-200, 200)
    tortu.pendown()
    tortu.write(salida + str(k), False, align="center")


def escribir_iteracion(i):
    '''
    Escribe en la esquina superior izquierda del plano el area del poligono
    '''
    tortu.color("white")
    tortu.speed(0)
    tortu.penup()
    tortu.setpos(200, 200)
    tortu.pendown()
    tortu.write("Iteracion: " + str(i - 1), False, align="center")

    tortu.color("black")
    tortu.speed(0)
    tortu.penup()
    tortu.setpos(200, 200)
    tortu.pendown()
    tortu.write("Iteracion: " + str(i), False, align="center")


def graficarKMeans(pCantidad, k):
    i = 1
    escribir_iteracion(i)
    i = i + 1
    usados = []
    cantidad = pCantidad
    p = clus.generarPuntos(cantidad)
    graficar_puntos(p)
    reps = clus.elegirRep(p, k)
    terminado = False
    while not terminado:
        m = clus.calcularMatriz(p, reps)
        graficar_grupos(p, m)
        graficar_reps(reps)
        q = clus.calcularQ(m, p, reps)
        escribir_iteracion(i)
        limpiarReps(reps)
        graficar_grupos(p, m)
        reps = clus.actualizarVectores(p, reps, m)
        k = clus.calcularQ(m, p, reps)
        graficar_reps(reps)
        diferencia = q - k
        if diferencia <  0.001 and diferencia > -0.001:
            terminado = True
        i = i+1

    print("Fin, puede cerrar la ventana emergente")
    escribir_k(p)
    ventana.exitonclick()
