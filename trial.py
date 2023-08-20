import tkinter




# .............................................................

def password_generator(min,max):
    import random
    global basic_password
    random_length = random.randint(min,max)
    basic_password = ""
    strings = "abcdefghijklmnopqrstuvwxyz"
    numbers = "123456789"
    upper_strings = strings.upper()
    symbol = "!@#$%^&*(){}[]"
    list_character = [strings , numbers , upper_strings , symbol ]
    if ul != 1 :
        list_character.remove(upper_strings)
    if ll != 1 :
        list_character.remove(strings)
    if n != 1 :
        list_character.remove(numbers)
    if sy != 1 :
        list_character.remove(symbol)
    for i in range (1):
        if ul == 1 and ll == 1 and  sy == 1 and n == 1 :
            basic_password += random.choice(strings)
            basic_password += random.choice(upper_strings)
            basic_password += random.choice(numbers)
            basic_password += random.choice(symbol)
        else :
            title = random.choice(list_character)
            basic_password += random.choice(title)
            title = random.choice(list_character)
            basic_password += random.choice(title)
            title = random.choice(list_character)
            basic_password += random.choice(title)
            title = random.choice(list_character)
            basic_password += random.choice(title)
    for i in range (random_length-4):
        title = random.choice(list_character)
        basic_password += random.choice(title)





# ....................................................


def bottun_create(min , max):
    min=int(textbox1.get())
    max=int(textbox2.get())

    looper = True

    while looper :
         if (5 < min < 17 ) and (5 < max < 17 ) and ( min < max ) :
             looper = False
         else :
             textbox1.delete(0,tkinter.END)
             textbox2.delete(0,tkinter.END)
             break

    basicpass= open("trial password generator.txt", "w")
    counter = 1
    number = int(textbox3.get())
    for i in range (number):
        password_generator(min,max)
        basicpass.write(f"{counter})")
        basicpass.write(basic_password)
        basicpass.write("\n")
        counter += 1


# ............................................
def checkbox():
    print(lower_letter.get())
    print(upper_letter.get())
    print(symbols.get())
    print(numbers.get())
    global ll
    global ul
    global sy
    global n
    ll = lower_letter.get()
    ul = upper_letter.get()
    sy = symbols.get()
    n = numbers.get()




# ...........................
def nightmode():
    global textbox1
    global textbox2
    global textbox3
    textbox1.config(fg="white")
    textbox1.config(bg="black")
    textbox2.config(fg="white")
    textbox2.config(bg="black")
    textbox3.config(fg="white")
    textbox3.config(bg="black")



#.............................................................
def lightmode():
    global textbox1
    global textbox2
    global textbox3
    textbox1.config(fg="black")
    textbox1.config(bg="white")
    textbox2.config(fg="black")
    textbox2.config(bg="white")
    textbox3.config(fg="black")
    textbox3.config(bg="white")

#.............................................................
def done():
    window.destroy()
    window1 = tkinter.Tk()
    label9 = tkinter.Label(window1, text="!done!" , borderwidth=40)
    label9.grid(row=0 , column=0 , columnspan=4)



# .........................................................
window = tkinter.Tk()
window.title("password generator")


label1 = tkinter.Label(window,text="min password length :")
label1.grid(row=0,column=0)
textbox1=tkinter.Entry(window,width=20 , fg="black" , bg="white")
textbox1.grid(row=0,column=1,columnspan=3)

label2 = tkinter.Label(window,text="max password length :")
label2.grid(row=1,column=0)
textbox2=tkinter.Entry(window,width=20 , fg="black" , bg="white")
textbox2.grid(row=1,column=1,columnspan=3)

min = textbox1.get()
max = textbox2.get()





label3 = tkinter.Label(window,text="number of password :")
label3.grid(row=2,column=0)
textbox3=tkinter.Entry(window,width=20 , fg="black" , bg="white")
textbox3.grid(row=2,column=1,columnspan=3)

number = textbox3.get()


lower_letter=tkinter.IntVar()
choice1=tkinter.Checkbutton(window,text="lower_letter",variable=lower_letter , command=checkbox)
choice1.grid(row=3,column=0)


upper_letter=tkinter.IntVar()
choice2=tkinter.Checkbutton(window,text="upper_letter",variable=upper_letter , command=checkbox )
choice2.grid(row=3,column=1)


numbers=tkinter.IntVar()
choice3=tkinter.Checkbutton(window,text="numbers",variable=numbers , command=checkbox)
choice3.grid(row=4,column=0)


symbols=tkinter.IntVar()
choice4=tkinter.Checkbutton(window,text="symbols",variable=symbols , command=checkbox)
choice4.grid(row=4,column=1)



btn1 = tkinter.Button(window,text="create",padx=25,pady=2.5 , borderwidth=8 , command=lambda :bottun_create(min , max))
btn1.grid(row=8 , column=0 , columnspan=3)

btn2 = tkinter.Button(window,text="night mode",padx=1,pady=2.5 , borderwidth=8 , command=nightmode)
btn2.grid(row=9 , column=0 , columnspan=3)


btn3 = tkinter.Button(window,text="light mode",padx=1,pady=2.5 , borderwidth=8 , command=lightmode)
btn3.grid(row=10 , column=0 , columnspan=3)


btn4 = tkinter.Button(window,text="Exit",padx=1,pady=2.5 , borderwidth=8 , command=done )
btn4.grid(row=12 , column=0 , columnspan=3)

window.mainloop()





