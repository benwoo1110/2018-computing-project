from tkinter import *

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

    # Answer textbox
    output = Text (Quad_Eqn, width=75, height=6, warp=WORD, background="white")
    output.grid(row=6, column=0, sticky=W)

    # Calculate button
    def calculate():
        return 0
        
    Button (Quad_Eqn,text='Calculate',command=calculate,activebackground='grey',activeforeground='grey',padx='10px',pady='3px') .grid(row=6, column=0)

    # Display window
    Quad_Eqn.mainloop()

# Main program
selection()
