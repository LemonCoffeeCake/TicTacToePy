#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 10:18:55 2019

@author: generaljewish
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import S, N, E, W

root = tk.Tk()

turn = 1
clicks = 0

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for r in range(0, 3):
    for c in range(0, 3):
        buttons[r][c] = Button(root, text="_", font='Papyrus 26 bold', height=5, width=10, command=lambda: check(root, turn, clicks))
        buttons[r][c].grid(row=r, column=c, sticky=S + N + E + W)


def resetboard():
    for i in range(0, 3):
        for j in range(0, 3):
            buttons[i][j] = Button(root, text='_')


def check(bu, t, cl):
    for i in range(0, 3):
        for j in range(0, 3):
            if buttons[i][j] is bu:
                if t % 2 == 1:
                    bu = tk.Label(root, text='X')
                else:
                    bu = tk.Label(root, text='O')

    cl += 1

    if(buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text'] == 'X' or
       buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text'] == 'X' or
       buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text'] == 'X' or
       buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] == 'X' or
       buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] == 'X' or
       buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] == 'X' or
       buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == 'X' or
       buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] == 'X'):
        messagebox.showinfo('Game over', 'X has won!')
        resetboard()
    elif(buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text'] == 'O' or
         buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text'] == 'O' or
         buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text'] == 'O' or
         buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] == 'O' or
         buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] == 'O' or
         buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] == 'O' or
         buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == 'O' or
         buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] == 'O'):
            messagebox.showinfo('Game over', 'O has won!')
            resetboard()
    elif c == 9:
        messagebox.showinfo('Game over', 'Tie.')
        resetboard()
    else:
        t += 1


tk.mainloop()
