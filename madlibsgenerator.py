import tkinter as tk
import tkinter.messagebox as mg
window=tk.Tk()
frame=tk.Frame(master=window,borderwidth=5)
frame.pack()
def story1():
    window=tk.Tk()
    frame1=tk.Frame(master=window,borderwidth=5)
    frame1.pack()
    story1="The best bee\nLong time ago,there was a bee named Billy.\nBilly was acute little bee ___ he was brave and wise\n__ enjoyed playing __ the garden.\nOnesunny day,he saw a bee hive set on fire,\nHe was brace enough to help others bees out."
    label=tk.Label(master=frame1,text=story1,bg="sky blue")
    label.grid(row=1,column=3,padx=5,pady=5)
    def getting():
        a=entry1.get()
        b=entry2.get()
        c=entry3.get()
        if a=="He" and b=="but" and c=="in":
            s="The best bee\nLong time ago,there was a bee named Billy.\nBilly was acute little bee but he was brave and wise\nHe enjoyed playing in the garden.\nOnesunny day,he saw a bee hive set on fire,\nHe was brace enough to help others bees out."
            label=tk.Label(master=frame1,text=s,bg="gray")
            label.grid(rows=7,column=3,padx=5,pady=5)
            mg.showinfo("congratulation u win the game!...")
        else:
            mg.showinfo("wrong!\ntry again")
    label=tk.Label(master=frame1,text="Guess the missing words....",bg="sky blue")
    label.grid(row=2,column=3,padx=5,pady=5)
    label=tk.Label(master=frame1,text="pronoun",bg="sky blue")
    label.grid(row=3,column=2,padx=5,pady=5)
    entry1=tk.Entry(master=frame1)
    entry1.grid(row=3,column=4,padx=5,pady=5)
    label=tk.Label(master=frame1,text="conjuction",bg="sky blue")
    label.grid(row=4,column=2,padx=5,pady=5)
    entry2=tk.Entry(master=frame1)
    entry2.grid(row=4,column=4,padx=5,pady=5)
    label=tk.Label(master=frame1,text="preposition",bg="sky blue")
    label.grid(row=5,column=2,padx=5,pady=5)
    entry3=tk.Entry(master=frame1)
    entry3.grid(row=5,column=4,padx=5,pady=5)
    button=tk.Button(master=frame1,text="playnow",bg="yellow",fg="red",command=getting)
    button.grid(row=6,column=2,padx=5,pady=5)
def story2():
    window=tk.Tk()
    frame2=tk.Frame(master=window,borderwidth=5)
    frame2.pack()
    story2="The wicked shake\nOnce upon a time,there lives a pair of crows on a huge mango tree.\nThe female crow had hatched some eggs and baby crows were ____.\nUnfortunately,one day ,a snake came to live in a hole at the bottom of the same tree.\nThe crows were not happy __ the arrival of the snake,but they could do nothing."
    label=tk.Label(master=frame2,text=story2,bg="pink")
    label.grid(row=1,column=3,padx=5,pady=5)
    def getting():
        a=entry1.get()
        b=entry2.get()
        if a=="born" and b=="at":
            s="The wicked shake\nOnce upon a time,there lives a pair of crows on a huge mango tree.\nThe female crow had hatched some eggs and baby crows were born.\nUnfortunately,one day ,a snake came to live in a hole at the bottom of the same tree.\nThe crows were not happy at the arrival of the snake,but they could do nothing."
            label=tk.Label(master=frame2,text=s,bg="gray")
            label.grid(rows=7,column=3,padx=5,pady=5)
            mg.showinfo("congratulation u win the game!...")
        else:
            mg.showinfo("wrong!\ntry again")
    label=tk.Label(master=frame2,text="Guess the missing words....",bg="sky blue")
    label.grid(row=2,column=3,padx=5,pady=5)
    label=tk.Label(master=frame2,text="verb",bg="sky blue")
    label.grid(row=3,column=2,padx=5,pady=5)
    entry1=tk.Entry(master=frame2)
    entry1.grid(row=3,column=4,padx=5,pady=5)
    label=tk.Label(master=frame2,text="preposition",bg="sky blue")
    label.grid(row=4,column=2,padx=5,pady=5)
    entry2=tk.Entry(master=frame2)
    entry2.grid(row=4,column=4,padx=5,pady=5)
    button=tk.Button(master=frame2,text="playnow",bg="yellow",fg="red",command=getting)
    button.grid(row=6,column=2,padx=5,pady=5)
def story3():
    window=tk.Tk()
    frame3=tk.Frame(master=window,borderwidth=5)
    frame3.pack()
    story2="Lion and Mouse\nJust then the little mouse\nhappened to pass by,and seeing \nthe sad plight __ which the lion\nwas,ran up to him ___ soon \ngnawed away the ropes that bound\n the king of the Beasts.\"Was _ not right?\" said the little mouse,very\nhappy to help the lion."
    label=tk.Label(master=frame3,text=story2,bg="pink")
    label.grid(row=1,column=3,padx=5,pady=5)
    def getting():
        a=entry1.get()
        b=entry2.get()
        c=entry3.get()
        if a=="in" and b=="and" and c=="I":
            s="Lion and Mouse\nJust then the little mouse\nhappened to pass by,and seeing \nthe sad plight in which the lion\nwas,ran up to him and soon \ngnawed away the ropes that bound\n the king of the Beasts.\"Was I not right?\" said the little mouse,very\nhappy to help the lion."
            label=tk.Label(master=frame3,text=s,bg="pink")
            label.grid(rows=7,column=3,padx=5,pady=5)
            mg.showinfo("congratulation u win the game!...")
        else:
            mg.showinfo("wrong!\ntry again")
    label=tk.Label(master=frame3,text="Guess the missing words....",bg="sky blue")
    label.grid(row=2,column=3,padx=5,pady=5)
    label=tk.Label(master=frame3,text="preposition",bg="sky blue")
    label.grid(row=3,column=2,padx=5,pady=5)
    entry1=tk.Entry(master=frame3)
    entry1.grid(row=3,column=4,padx=5,pady=5)
    label=tk.Label(master=frame3,text="conjuction",bg="sky blue")
    label.grid(row=4,column=2,padx=5,pady=5)
    entry2=tk.Entry(master=frame3)
    entry2.grid(row=4,column=4,padx=5,pady=5)
    label=tk.Label(master=frame3,text="pronoun",bg="sky blue")
    label.grid(row=5,column=2,padx=5,pady=5)
    entry3=tk.Entry(master=frame3)
    entry3.grid(row=5,column=4,padx=5,pady=5)
    button=tk.Button(master=frame3,text="playnow",bg="yellow",fg="red",command=getting)
    button.grid(row=6,column=2,padx=5,pady=5)
label=tk.Label(master=frame,text="welcome to mad lip generator",bg="skyblue")
label.pack(padx=5,pady=5)
label=tk.Label(master=frame,text="click the following widgets to play the game",bg="gray")
label.pack(padx=5,pady=5)
button=tk.Button(master=frame,text="The Best Bee",bg="yellow",fg="red",command=story1)
button.pack(padx=5,pady=5)
button0=tk.Button(master=frame,text="The Wicked Shake",bg="yellow",fg="red",command=story2)
button0.pack(padx=5,pady=5)
button1=tk.Button(master=frame,text=" Lion and Mouse",bg="yellow",fg="red",command=story3)
button1.pack(padx=5,pady=5)
window.mainloop()

    
    
    

