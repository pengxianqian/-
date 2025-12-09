import words
import tkinter as tk
from tkinter import messagebox
from random import choice

class WordTrainer:
    def __init__(self):
        self.dic = words.word_dic
        self.lis = words.word_list
        self.newwords = choice(self.lis)
        
        self.screen = tk.Tk()
        self.screen.title('单词训练')
        
        W = 500
        H = 500
        M = self.screen.maxsize()
        L_DIC = (M[0]-W)//2
        U_DIC = (M[1]-H)//2
        
        self.screen.geometry(f'{W}x{H}+{L_DIC}+{U_DIC}')
        self.screen.resizable(width=False, height=False)
        
        self._create_widgets()
    
    def _create_widgets(self):
        """创建界面组件"""
        self.wor = tk.StringVar()
        self.input_words = tk.Entry(self.screen, textvariable=self.wor, width=20, font=('黑体', 18))
        self.input_words.place(x='140', y='150')
        
        self.word_label = tk.Label(self.screen, text=self.dic[self.newwords], font=('黑体', 18))
        self.word_label.grid(row=1, column=1)
        
        self.next_button = tk.Button(self.screen, text='检查', font=('黑体', 20), width=10, command=self.update_word)
        self.next_button.place(x='180', y='230')
    
    def update_word(self):
        """更新单词"""
        if self.wor.get() == self.newwords:
            self.newwords = choice(self.lis)
            self.word_label.config(text=self.dic[self.newwords])
            self.wor.set('')  # 清空输入框
        else:
            messagebox.showinfo(title='拼写错误', message='单词不正确！')
    
    def run(self):
        self.screen.mainloop()

if __name__ == '__main__':
    app = WordTrainer()
    app.run()