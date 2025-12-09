import words
import tkinter as tk
from tkinter import messagebox
from random import choice

dic = words.word_dic
lis = words.word_list

screen = tk.Tk()
screen.title('单词训练')
W = 500
H = 500
M = screen.maxsize()
L_DIC = (M[0]-W)//2
U_DIC = (M[1]-H)//2

screen.geometry(f'{W}x{H}+{L_DIC}+{U_DIC}')
screen.resizable(width=False,height=False)

wor = tk.StringVar()
input_words = tk.Entry(screen,textvariable=wor,width=20,font=('黑体',18))
input_words.place(x='140',y='150')

newwords = choice(lis)
word = tk.Label(screen,text=dic[newwords],font=('黑体',18))

word.grid(row=1,column=1)

def update_word():
    global word,newwords
    if wor.get() == newwords:
        newwords = choice(lis)
        word.config(text=dic[newwords])  
    else:
        messagebox.showinfo(title='拼写错误',message='单词不正确！')


next_button = tk.Button(screen,text='检查',font=('黑体',20),width=10,command=update_word)
next_button.place(x='180',y='230')

screen.mainloop()