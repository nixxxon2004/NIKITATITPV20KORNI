from tkinter import *
import math

def calc(a, b, c):
	D = b**2 - (4*a*c)
	if D > 0:
		x1 = (-b + math.sqrt(D))/(2*a)
		x2 = (-b - math.sqrt(D))/(2*a)
		return x1,x2
	elif D == 0:
		x = (-b)/(2*a)
		return x, "КОРЕНЬ ОДИН", x
	else:
		return "КОРНЕЙ НЕТУ", ""



def show_ans(event):
	global input_a
	global input_b
	global input_c
	global answer

	x1,x2 = calc(float(input_a.get()),float(input_b.get()),float(input_c.get()))
	answer.config(text="РЕШЕНИЕ = " + str(x1) + " ; " + str(x2))






window = Tk()
button = Button(window, text="Calculate")
input_a = Entry(window)
input_b = Entry(window)
input_c = Entry(window)
window.geometry('300x500')
input_a.pack(side=LEFT)
l = Label(window, text="x^2 +")
l.pack(side=LEFT)
input_b.pack(side=LEFT)
l = Label(window, text="x +")
l.pack(side=LEFT)
input_c.pack(side=LEFT)
l = Label(window, text=" = 0")
l.pack(side=LEFT)

answer = Label(window, text="РЕШЕНИЕ = ", font="Arial 26")
answer.pack(side=BOTTOM)


button.pack(side=LEFT)
button.bind("<Button-1>",func=show_ans)
window.mainloop()
