import Tkinter
import sys
import tkMessageBox
    
#Centra la ventana
def centrar(ventana):
    ventana.update_idletasks()
    w=ventana.winfo_width()
    h=ventana.winfo_height()
    extraW=ventana.winfo_screenwidth()-w
    extraH=ventana.winfo_screenheight()-h
    ventana.geometry("%dx%d%+d%+d" % (w,h,extraW/2,extraH/2))
    
def main():

    def tomarDatos():
        #Valida que el numero de puntos esta en el rango
        if (txtCantidad.get() == "") or (txtCantidad.get().isalpha()) or (int(txtCantidad.get())<0):
            tkMessageBox.showwarning('Atencion', 'N debe ser un numero entero positivo.')
        else:
            if (txtGrupos.get() == "") or (txtGrupos.get().isalpha()) or (int(txtGrupos.get())<0):
                tkMessageBox.showwarning('Atencion', 'K debe ser un numero entero positivo.')
            else:
                global cantidad
                cantidad = int(txtCantidad.get())
                k = int(txtGrupos.get())
                ventanaPrincipal.destroy()
                import graficador as g
                g.main(cantidad, k)            
                
    #VENTANA Inicial
    ventanaPrincipal = Tkinter.Tk()
    ventanaPrincipal.title("Datos de entrada")
    ventanaPrincipal.geometry("350x250")
    centrar(ventanaPrincipal)

    #OBJETOS PARA LA ENTRADA DE DATOS
    lblInstruccion = Tkinter.Label(ventanaPrincipal, text= "  Digite el valor de N (cantidad de puntos aleatorios):")
    lblInstruccion.pack()
    lblInstruccion.place(x=20,y=10)
    txtCantidad = Tkinter.Entry(ventanaPrincipal)
    txtCantidad.pack(padx=30, pady=50, ipadx=5, ipady=5)
    
    lblInstruccion2 = Tkinter.Label(ventanaPrincipal, text= "  Digite el valor de K (cantidad de grupos):")
    lblInstruccion2.pack()
    lblInstruccion2.place(x=20,y=100)
    txtGrupos = Tkinter.Entry(ventanaPrincipal)
    txtGrupos.pack(padx=30, pady=5, ipadx=5, ipady=5)

    btnAceptar = Tkinter.Button(ventanaPrincipal, text = "Aceptar", command = tomarDatos)
    btnAceptar.pack()
    btnAceptar.place(x=60, y=190)
    
    ventanaPrincipal.mainloop()
    

if __name__ == '__main__':
    main()

