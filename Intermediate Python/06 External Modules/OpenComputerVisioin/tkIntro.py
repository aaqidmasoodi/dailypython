# this has nothing to do with in
import tkinter as tk


window = tk.Tk()

# creating three sliders for HUE, SATURATION, VALUE for LowerB
low_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

low_H.pack()
low_S.pack()
low_V.pack()

# creating three sliders for HUE, SATURATION, VALUE for UpperB
High_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
High_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
High_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

High_H.pack()
High_S.pack()
High_V.pack()




while True:
 print(f'LOW: {low_H.get()}, {low_S.get()}, {low_V.get()}')
 print(f'HIGH: {High_H.get()}, {High_S.get()}, {High_V.get()}')
 window.update()