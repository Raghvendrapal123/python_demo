import tkinter as tk
import random

root=tk.Tk()
root.title('Random number game')
root.config(bg='dark orange')
root.minsize(350,400)


def rand(n,num):
    #print(n)

    if num<n:
        label.config(font='arial 30',text='guess is low')
    elif num>n:
        label.config(font='arial 30',text='guess is high')
    else:
        label.config(font='arial 30',text='you guessed it')

def rules():
    label.config(font='arial 15',text='this program generates a random\
                 \n integer and you have to guess that')





label=tk.Label(root,fg='indigo',bg='dark orange')
label.grid(row=0,column=0,pady=20,columnspan=4)

n=random.randint(1,9)
#print(n)


tk.Button(root,text='1',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,1)
          ).grid(row=4,column=1)

tk.Button(root,text='2',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,2)
          ).grid(row=4,column=2)

tk.Button(root,text='3',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,3)
          ).grid(row=4,column=3)


tk.Button(root,text='4',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,4)
          ).grid(row=5,column=1)

tk.Button(root,text='5',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,5)
          ).grid(row=5,column=2)

tk.Button(root,text='6',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,6)
          ).grid(row=5,column=3)



tk.Button(root,text='7',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,7)
          ).grid(row=6,column=1)

tk.Button(root,text='8',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,8)
          ).grid(row=6,column=2)

tk.Button(root,text='9',font='arial 25 bold',bg='maroon',fg='white',
          width=6,height=1,border=8,command=lambda:rand(n,9)
          ).grid(row=6,column=3)

tk.Button(root,text='Exit',font='arial 20 bold',bg='red',fg='black',
          width=6,height=1,border=8,command=root.destroy
          ).grid(row=7,column=0,columnspan=3)

tk.Button(root,text='Rules',font='arial 20 bold',bg='green',fg='black',
          width=6,height=1,border=8,command=lambda:rules()
          ).grid(row=7,column=2,columnspan=2)

