from tkinter import *

main= Tk()


main.title("Proyecto")
main.config(bg="Brown1")


top_frame = Frame(main,bd=2,relief=FLAT)
left_frame = Frame(main,bd=1,relief=FLAT)

# Colocación de los elementos de la ventana principal
top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)

# Elementos del frame superior
top_frame_lbl = Label(top_frame,font=("Verdana",40),text="Recetas",fg="DarkSlateGray")

# Colocación de los elementos del frame superior
top_frame_lbl.pack()

# Elementos del frame izquierdo
caracteristicas_frame = Frame(left_frame,bd=1,relief=FLAT)


# Colocación de los elementos del frame izquierdo
meal_frame.grid(row=0,column=0)


# Elementos del frame de comidas
meal_frame_lbl = LabelFrame(meal_frame,font=("Verdana",24),text="Caracteristicas",fg="Blue")

# Colocación de los elementos del frame de comidas
meal_frame_lbl.pack(side=TOP)



# Listas de productos
meal_list = ["Vegano", "Vegetariano", "Gluten-Free", "No Lactosa", "Todo"]


# Generar Checkbuttons para la comida
meal_options = list()
meal_cont = list()
cont = 0
for meal in meal_list:
    # Añadir variable de control para recoger el valor del elemento Checkbutton
    meal_options.append(IntVar())
    Checkbutton(meal_frame_lbl,text=meal,font=("Verdana",18),onvalue=1,offvalue=0,variable=meal_options[cont]).grid(row=cont,column=0,sticky=W)
    # Generar Entry para recoger la cantidad
    # meal_cont.append(Entry(meal_frame_lbl,font=("Verdana",18),justify=CENTER,bd=1,width=3,state=DISABLED))
    # meal_cont[cont].grid(row=cont,column=1,sticky=W)
    # Aumentar contador para la siguiente iteración
    cont += 1





#GUARDAMOS LOS VALORES DE LOS CALCULOS

var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()





















main.mainloop()