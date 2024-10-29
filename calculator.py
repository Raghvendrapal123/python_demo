from tkinter import *

root=Tk()
root.title("calculator")
root.geometry("280x380")
root.config(background="black")

def get_digit(digit):
   #print(digit)
    current=result_label['text']
    new=current+str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number,operator
    first_number=int(result_label['text'])
    operator=op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number=int(result_label['text'])
    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator=='-':
        result_label.config(text=str(first_number-second_number))
    elif operator=='*':
        result_label.config(text=str(first_number*second_number))
    else:
        if second_number==0:
            result_label.config(text='error')
        else:
            result_label.config(text=str(round(first_number/second_number,2)))

result_label=Label(root,text='',bg="black",fg="white")
result_label.config(font="verdana 30 bold")
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')



btn7=Button(root,text='7',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(7)
           ).grid(row=1,column=0)

btn8=Button(root,text='8',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(8)
           ).grid(row=1,column=1)

btn9=Button(root,text='9',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(9)
           ).grid(row=1,column=2)

btn_add=Button(root,text='+',font='verdana 14 bold', bg='magenta',fg='white',
width=5,height=2,command=lambda:get_operator('+')
           ).grid(row=1,column=3)




btn4=Button(root,text='4',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(4)
           ).grid(row=2,column=0)

btn5=Button(root,text='5',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(5)
           ).grid(row=2,column=1)

btn6=Button(root,text='6',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(6)
           ).grid(row=2,column=2)

btn_sub=Button(root,text='-',font='verdana 14 bold', bg='magenta',fg='white',
width=5,height=2,command=lambda:get_operator('-')
           ).grid(row=2,column=3)





btn1=Button(root,text='1',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(1)
           ).grid(row=3,column=0)

btn2=Button(root,text='2',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(2)
           ).grid(row=3,column=1)

btn3=Button(root,text='3',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(3)
           ).grid(row=3,column=2)

btn_mul=Button(root,text='*',font='verdana 14 bold', bg='magenta',fg='white',
width=5,height=2,comman=lambda:get_operator('*')
           ).grid(row=3,column=3)



btn_clr=Button(root,text='clear',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:clear()
           ).grid(row=4,column=0)

btn0=Button(root,text='0',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_digit(0)
           ).grid(row=4,column=1)

btn_equal=Button(root,text='=',font='verdana 14 bold', bg='magenta',fg='white',
    width=5,height=2,command=lambda:get_result()
           ).grid(row=4,column=2)

btn_div=Button(root,text='/',font='verdana 14 bold', bg='magenta',fg='white',
width=5,height=2,command=lambda:get_operator('/')
           ).grid(row=4,column=3)





















