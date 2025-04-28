from tkinter import *
root=Tk()


thelabel= Label(root,text='CHITKARA UNIVERSITY INSTITUTE OF ENGINEERING AND TECHNOLOGY '  ,fg='white',bg='black',font=( 24))
thelabel.grid(row=1, columnspan=5)

label_1=Label(root, text='Department', font=(16))
label_2=Label(root, text='Year',font=(16))
entry_1=Entry(root,font=(16))
entry_2=Entry(root,font=(16))
label_3=Label(root, text='Section Name',font=(16))
entry_3=Entry(root,font=(16))

label1=Label(root)
label1.grid(row=2)
label1=Label(root)
label1.grid(row=3)
label1=Label(root)
label1.grid(row=6)

label_1.grid(row=5,column=0)
label_2.grid(row=7,column=0)
entry_1.grid(row=5,column=1)
entry_2.grid(row=7,column=1)
label_3.grid(row=9,column=0)
entry_3.grid(row=9,column=1)

label1=Label(root)
label1.grid(row=8)

thelabel= Label(root,text='DASHBOARD                                                  '  ,fg='black',bg='yellow',font=( 30))
thelabel.grid(row=12)

label1=Label(root)
label1.grid(row=10)
label1=Label(root)
label1.grid(row=11)
label1=Label(root)
label1.grid(row=13)


