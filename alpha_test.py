from tkinter import *
from math import pi

def selection():
    # inital setup of view
    selection_page = Tk()
    selection_page.title("math function")
    
    # ScrollBar/Listbox of all the math function
    math_functions = ["Quadratic Equation", "Y = Mx + C", "Area of circle", "Sets", "empty 1","empty 2"]

    def CurSelet(event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        print(picked)
        selection_page.destroy()
        if picked == "Quadratic Equation": Quad_Eqn(picked)
        elif picked == "Area of circle": Area_Circle(picked)
        
    scrollbar = Scrollbar(selection_page)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(selection_page, width=15, height=4, yscrollcommand=scrollbar.set, font="none 40 bold")
    for function in math_functions:
        listbox.insert(END, function)
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    listbox.bind('<<ListboxSelect>>',CurSelet)

    scrollbar.config(command=listbox.yview)

    # Display window
    selection_page.mainloop()

def Quad_Eqn(name):
    # inital setup of view
    Quad_Eqn = Tk()
    Quad_Eqn.title(name)

    #Back button
    def back():
        Quad_Eqn.destroy()
        selection()

    Button (Quad_Eqn,text='Back',command=back,activebackground='grey',activeforeground='grey',padx='10px',pady='3px') .grid(row=0, column=0, sticky=W)
    
    # Title
    Label (Quad_Eqn, text=name, borderwidth=1, font="none 30 bold") .grid (row=1, column=0, sticky=W)

    # Image of quadratic equation formula
    quad_formula_image = PhotoImage(file="Quad_formula.png")
    Label (Quad_Eqn, image=quad_formula_image) .grid (row=2, column=0)

    # Input for a, b, c
    Label (Quad_Eqn, text=" a = ", borderwidth=1, font="30") .grid (row=3, column=0, sticky=W)
    input_a = Entry(Quad_Eqn, width=29, bg='white')
    input_a.grid(row=3, column=0, sticky=E)

    Label (Quad_Eqn, text=" b = ", borderwidth=1, font="30") .grid (row=4, column=0, sticky=W)
    input_b = Entry(Quad_Eqn, width=29, bg='white')
    input_b.grid(row=4, column=0, sticky=E)

    Label (Quad_Eqn, text=" c = ", borderwidth=1, font="30") .grid (row=5, column=0, sticky=W)
    input_c = Entry(Quad_Eqn, width=29, bg='white')
    input_c.grid(row=5, column=0, sticky=E)

    # Calculate button
    def calculate():
        a, b, c = input_a.get(), input_b.get(), input_c.get()
        output.delete(0.0, END)
        # check if input is valid
        try:
            a, b, c = int(a), int(b), int(c)
        # show if invalid input
        except:
            output.insert(END, "Please ensure input is a, b and c is an integer.")
        # Solve for x
        else:
            # calulation
            x1 = (-b+(b**2-4*a*c)**0.5) / 2*a
            x2 = (-b-(b**2-4*a*c)**0.5) / 2*a
            # displaying answer
            if x1 == x2: output.insert(END, "x = {}".format(x1))
            else: output.insert(END, "x = {} or x = {}".format(x1, x2))
        
    Button (Quad_Eqn,text='Calculate',command=calculate,activebackground='grey',activeforeground='grey',padx='10px',pady='3px') .grid(row=6, column=0)
    
    # Answer textbox
    output = Text (Quad_Eqn, width=41, height=6, background="white")
    output.grid(row=7, column=0)
    output.insert(END, "answer will be shown here")
    
    # Display window
    Quad_Eqn.mainloop()

def Area_Circle(name):
    # inital setup of view
    Area_Circle = Tk()
    Area_Circle.title(name)
    
    #Back button
    def back():
        Area_Circle.destroy()
        selection()

    Button (Area_Circle,text='Back',command=back,activebackground='grey',activeforeground='grey',padx='10px',pady='3px') .grid(row=0, column=0, sticky=W)

    # Title
    Label (Area_Circle, text=name, borderwidth=1, font="none 30 bold") .grid (row=1, column=0, sticky=W)

    # Image of quadratic equation formula
    circle_formula_image = PhotoImage(file="Area_Circle_formula.png")
    Label (Area_Circle, image=circle_formula_image) .grid (row=2, column=0)

    # Input for radius
    Label (Area_Circle, text=" Radius = ", borderwidth=1, font="30") .grid (row=3, column=0, sticky=W)
    radius = Entry(Area_Circle, width=37, bg='white')
    radius.grid(row=3, column=0, sticky=E)

    # Calculate button
    def calculate():
        r = radius.get()
        output.delete(0.0, END)
        
        # check if input is valid
        if r.isdigit():
            #calculate area & circumference of circle
            r = int(r)
            area, circumference = pi*r*r, pi*(2*r)
            # displaying answer
            output.insert(END, "area = {}\ncircumference = {}".format(area, circumference))
        # show is input is invalid
        else: output.insert(END, "Please ensure input of radius is an positive integer.")
        
    Button (Area_Circle,text='Calculate',command=calculate,activebackground='grey',activeforeground='grey',padx='10px',pady='3px') .grid(row=4, column=0)

    # Answer textbox
    output = Text (Area_Circle, width=55, height=6, background="white")
    output.grid(row=5, column=0)
    output.insert(END, "answer will be shown here")
    
    # Display window
    Area_Circle.mainloop()
    
# Main program
selection()
