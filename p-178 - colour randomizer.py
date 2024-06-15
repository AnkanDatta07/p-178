# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:37:11 2024

@author: Ankan Datta
"""

from tkinter import *
import random

root = Tk()
root.title("Encapsulation")
root.geometry("400x300")
root.config(bg = "lightblue")

label_color = Label(root, font = ("Comic Sans MS", 20, "bold"), bg = "white")
label_color.place(relx = 0.5, rely = 0.4, anchor = CENTER)

class Score():
    
    def __init__(self):
        self.__score = 0
        
    def updateScore(self):
        self.text = ["BLACK", "PINK", "GREEN", "BLUE", "YELLOW", "RED"]
        self.random_text = random.randint(0, 5)
        
        self.color = ["BLACK", "PINK", "GREEN", "BLUE", "YELLOW", "RED"]
        self.random_color = random.randint(0, 5)
        
        label_color["text"] = self.text[self.random_text]
        label_color["fg"] = self.color[self.random_color]

obj = Score()
        
btn = Button(root, text = "Start", command = obj.updateScore, relief = FLAT, bg = "dark olive green", fg = "white", padx = 10, pady = 1, font = ("Arial", 15))
btn.place(relx = 0.6, rely = 0.8, anchor = CENTER)

root.mainloop()