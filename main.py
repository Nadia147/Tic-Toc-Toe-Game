from tkinter import *
root=Tk()
root.geometry("700x700")
root.title("Tic Tac Toe")
f1=Frame(root)
f1.pack()
tlebel=Label(f1,text="Tic Tac Toe",font=("Arial",26),bg="sky blue")
tlebel.pack()
f3=Frame(root)
f3.pack()

f2=Frame(root)
f2.pack()
possition={1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
turn="x"
def check(ply):
    if possition[1]== possition[2]and  possition[2]== possition[3] and  possition[3]==ply:
        return True
    elif possition[4]== possition[5]and  possition[5]== possition[6] and  possition[6]==ply:
        return True
    elif possition[7]== possition[8]and  possition[8]== possition[9] and  possition[9]==ply:
        return True
    elif possition[1]== possition[4]and  possition[4]== possition[7] and  possition[7]==ply:
        return True
    elif possition[2]== possition[5]and  possition[5]== possition[8] and  possition[8]==ply:
        return True
    elif possition[3]== possition[6]and  possition[6]== possition[9] and  possition[9]==ply:
        return True
    elif possition[1]== possition[5]and  possition[5]== possition[9] and  possition[9]==ply:
        return True
    elif possition[3]== possition[5]and  possition[5]== possition[7] and  possition[7]==ply:
        return True
    return 7
def drow():
    for i in possition.keys():
        if possition[i]=="":
         return False
    
    return True
def restart():
    for button in btns:
        button["text"]=""


def play(event):
    global turn
    button = event.widget
    buttonT=str(button)
    clk=buttonT[-1]
    if clk=="n":
        clk=1
    else:
        clk=int(clk)
    
    
    if button["text"]=="":
     


     if turn=="x":
       button["text"]="X"
       possition[clk]=turn
       if check(turn)==True:
        winl=Label(f3,text=f"'{turn}' wins the game",font=("Arial",20), bg="green")
        winl.grid(row=0,column=1,columnspan=3)
       turn="o" 
        
        
       
      
     else:
       button["text"]="O"
       possition[clk]=turn
       if check(turn)==True:
        winl=Label(f3,text=f"'{turn}' wins the game",font=("Arial",20), bg="green")
        winl.grid(row=0,column=1,columnspan=3)
        print(turn,"wins")
       turn="x"
    
    if drow()==True:
        winld=Label(f2,text=f"nobody wins the game",font=("Arial",20), bg="green")
        winld.grid(row=3,column=1,columnspan=3)



     
       
  
    

b1=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b1.grid(row=0,column=0)
b1.bind("<Button-1>",play)

b2=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b2.grid(row=0,column=1)
b2.bind("<Button-1>",play)

b3=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b3.grid(row=0,column=2)
b3.bind("<Button-1>",play)

b4=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b4.grid(row=1,column=0)
b4.bind("<Button-1>",play)
b5=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b5.grid(row=1,column=1)
b5.bind("<Button-1>",play)
b6=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b6.grid(row=1,column=2)
b6.bind("<Button-1>",play)

b7=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b7.grid(row=2,column=0)
b7.bind("<Button-1>",play)
b8=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b8.grid(row=2,column=1)
b8.bind("<Button-1>",play)
b9=Button(f2,text="",width=4,height=2,font=("Arial",35), bg="sky blue")
b9.grid(row=2,column=2)
b9.bind("<Button-1>",play)
btns=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
#b10=Button(f2,text="Restart",width=12,height=1,font=("Arial",35), bg="blue",relief=RAISED,command=restart())
#b10.grid(row=4,column=0,columnspan=3)


root.mainloop()