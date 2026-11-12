from tkinter import *

ventana = Tk()
ventana.title("Actividad TK1 - Tres Marcos")
ventana.geometry("1200x1450") 
ventana.iconbitmap("icono.ico") 
ventana.config(bg="gray")

marco_sup = Frame(ventana)
marco_sup.place(x=50, y=20)
marco_sup.config(width=591, height=614, bg="lightblue", bd=10, relief="sunken", cursor="hand2")

marco_inf_izq = Frame(ventana)
marco_inf_izq.place(x=50, y=660) # Lo bajamos a y=660 para que no tape al de arriba
marco_inf_izq.config(width=314, height=400, bg="lightgreen", bd=15, relief="raised", cursor="cross")

marco_inf_der = Frame(ventana)
marco_inf_der.place(x=400, y=660) # Lo movemos a la derecha (x=400) y abajo (y=660)
marco_inf_der.config(width=773, height=725, bg="lightcoral", bd=5, relief="ridge", cursor="circle")

imagen1 = PhotoImage(file="imagen1.png")
Label(marco_sup, image=imagen1, bg="lightblue").place(x=0, y=0, relwidth=1, relheight=1)

imagen2 = PhotoImage(file="imagen2.gif")
Label(marco_inf_izq, image=imagen2, bg="lightgreen").place(x=0, y=0, relwidth=1, relheight=1)

imagen3 = PhotoImage(file="imagen3.png")
Label(marco_inf_der, image=imagen3, bg="lightcoral").place(x=0, y=0, relwidth=1, relheight=1)

# --- Textos ---
Label(marco_sup, text="Marco Superior - Principal").place(x=280, y=20)
Label(marco_inf_izq, text="Marco Izquierdo").place(x=110, y=20)
Label(marco_inf_der, text="Marco Derecho").place(x=110, y=20)

ventana.mainloop()