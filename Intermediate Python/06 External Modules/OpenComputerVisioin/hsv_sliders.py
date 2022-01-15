import tkinter as tk
window = tk.Tk()

label_low = tk.Label(window, text='LOWER BOUND',pady=30)

# creating three sliders for HUE, SATURATION, VALUE for LowerB
low_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
low_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

label_low.pack()
low_H.pack()
low_S.pack()
low_V.pack()

# i've also added some labels and stuff for your understanding...
# low_h.set(int) # to set an initial value for a slider

label_high = tk.Label(window, text='HIGHER BOUND', pady=30)

# creating three sliders for HUE, SATURATION, VALUE for UpperB
high_H = tk.Scale(window, from_=0, to=359, orient='horizontal')
high_S = tk.Scale(window, from_=0, to=359, orient='horizontal')
high_V = tk.Scale(window, from_=0, to=359, orient='horizontal')

label_high.pack()
high_H.pack()
high_S.pack()
high_V.pack()


'''
while True:
 window.update()
'''

if __name__ == '__main__':
 window.mainloop()

