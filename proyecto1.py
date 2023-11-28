from tkinter import *



main= Tk()


main.title("Proyecto")
main.config(bg="Brown1")



top_frame = Frame(main,bd=2,relief=FLAT)
left_frame = Frame(main,bd=1,relief=FLAT)
right_frame = Frame(main,bd=1,relief=FLAT)


top_frame.pack(side=TOP)
left_frame.pack(side=LEFT)
right_frame.pack(side=RIGHT)


top_frame_lbl = Label(top_frame,font=("Verdana",40),text="Recetas",fg="DarkSlateGray")
top_frame_lbl.pack()

caracteristicas_frame = Frame(left_frame,bd=1,relief=FLAT)
caracteristicas_frame.pack()

caracteristicas_frame_lbl = Label(caracteristicas_frame,font=("Verdana",30),text="Caracteristicas",fg="Black")
caracteristicas_frame_lbl.pack(side=TOP)



var=IntVar



Radiobutton(caracteristicas_frame, text="Vegano", variable=var, 
            value=1,font=("Verdana",28)).pack(anchor=W)
Radiobutton(caracteristicas_frame, text="Vegetariano", variable=var, 
            value=2,font=("Verdana",28)).pack(anchor=W)
Radiobutton(caracteristicas_frame, text="Sin Lactosa", variable=var,   
            value=3,font=("Verdana",28)).pack(anchor=W)
Radiobutton(caracteristicas_frame, text="Gluten-Free", variable=var,   
            font=("Verdana",28)).pack(anchor=W)
Radiobutton(caracteristicas_frame, text="Todo", variable=var,   
                font=("Verdana",28)).pack(anchor=W)








main.mainloop()


