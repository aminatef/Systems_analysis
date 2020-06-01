from tkinter import * 
import random
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

def binomial_ceofficient(n, i):
	return (math.factorial(n))/(math.factorial(i)*math.factorial((n-i)))

def finite_difference(y,k,i):
	return y[k-i]

def numerical_diff_finite_difference(n,k,u,h):
	FD_nth_diff = 0
	# print("order of diff:",n)
	for i in range(0,n+1):
		if i % 2 == 0:
			sign = 1
		else:
			sign = -1 
		FD_nth_diff += (sign * binomial_ceofficient(n,i) * finite_difference(u,k,i)) 
	return FD_nth_diff/pow(h,n)

def part_diff_y(n,k,y,h):
	FD_nth_diff = 0
	for i in range(1,n+1):
		if i % 2 == 0:
			sign = 1
		else:
			sign = -1 
		FD_nth_diff += (sign * binomial_ceofficient(n,i) * finite_difference(y,k,i)) 
	return FD_nth_diff/pow(h,n)

def jth_derivative(y,j,h):
	y_jth = []
	for i in range(j+1,len(y)):
		y_jth.append(numerical_diff_finite_difference(j,i,y,h))
	return y_jth


def System_response(n, m, h, iterations, u, coefficients_of_Ys, coefficients_of_Us):

	states = [[0 for i in range(0,iterations)] for j in range(n+1)]
	ceofficients_denominator=[(1/pow(h,i))*coefficients_of_Ys[i] for i in range(n+1)]
	y_of_t=[]

	for i in range(n+1,iterations):
		list_diffs_Z = [part_diff_y(order,i,states[0],h) * coefficients_of_Ys[order] for order in range(1,n+1)]
		sum_ceofficient_denominator = math.fsum(ceofficients_denominator)
		sum_diffs_Z = math.fsum(list_diffs_Z)
		states[0][i] = (-(sum_diffs_Z)+u[i])/(sum_ceofficient_denominator)

	for j in range(1,len(states)):
		states[j] = jth_derivative(states[0],j,h)

	for i in range(iterations-(n+1)):
		sum1=0
		for j in range(m+1):
			sum1 += states[j][i] * coefficients_of_Us[j]
		y_of_t.append(sum1)
		
	return [y_of_t,states]
def draw_1(x,y,fig_name,x_lab,y_lab,new_win,n):
	f1=plt.figure(figsize=(7,3))
	plt.grid()
	plt.xlabel(x_lab)
	plt.ylabel(y_lab)
	plt.title(fig_name)
	plt.plot(x,y)	
	canvas = FigureCanvasTkAgg(f1, master=new_win)
	canvas.draw()
	canvas.get_tk_widget().grid(row=n)

def calculate():
	ceofficients_Y = e1.get().split()
	ceofficients_U = e2.get().split()
	ceofficients_Y.reverse()
	ceofficients_U.reverse()
	time = t.get()
	plot_states = var1.get()
	state_space = var2.get()
	print(plot_states,state_space)
	for i in range(len(ceofficients_Y)):
		ceofficients_Y[i] = float(ceofficients_Y[i])
	for i in range(len(ceofficients_U)):
		ceofficients_U[i] = float(ceofficients_U[i])
	n = len(ceofficients_Y)-1
	m = len(ceofficients_U)-1
	delta_x = 0.0005
	iterations = int((float(time) / delta_x))
	if v.get() == 3:
		u = [i*delta_x for i in range(0,iterations)]
		Sys_response = System_response(n, m, delta_x, iterations, u, ceofficients_Y, ceofficients_U)
		x = [i*delta_x for i in range(len(Sys_response[0]))]
		draw_1(x,Sys_response[0],"ramp response","time(sec)","y(t)",master,20)
	elif v.get()==1:
		u = [1 for i in range(0,iterations)]
		Sys_response = System_response(n, m, delta_x, iterations, u, ceofficients_Y, ceofficients_U)
		x = [i*delta_x for i in range(len(Sys_response[0]))]
		draw_1(x,Sys_response[0],"unit step response","time(sec)","y(t)",master,20)
	elif v.get()==2:
		u = [1 for i in range(0,iterations)]
		Sys_response = System_response(n, m, delta_x, iterations, u, ceofficients_Y, ceofficients_U)
		Sys_response[0] =jth_derivative(Sys_response[0],1,delta_x)
		x = [i*delta_x for i in range(len(Sys_response[0]))]
		draw_1(x,Sys_response[0],"impulse response","time(sec)","y(t)",master,20)	
	if plot_states:
		fig,axes = plt.subplots(len(Sys_response[1])-1)
		fig.suptitle('States')
		num = 0
		for i in range(len(Sys_response[1])-1):
			num+=1
			x = [i*delta_x for i in range(len(Sys_response[1][i]))]
			plt.xlabel("time(sec)")
			plt.ylabel("x{}()".format(num))
			axes[i].plot(x,Sys_response[1][i])
		canvas = FigureCanvasTkAgg(fig, master=new_win)
		canvas.draw()
		canvas.get_tk_widget().grid(row=1)
	# if state_space:

master = Tk(className="System response")
new_win = Tk(className="States")
text1 = 'System response for  ==>  an * y^(n) + a(n-1) * y^(n-1) + ... + a0 * y = bn * U^(n) + b(n-1) * U^(n-1) +...+ b0 * U'
Label(master, text=text1).grid(row=0,sticky=W)

text2 = 'Enter differential equation ceofficients separeted with spaces'
Label(master, text=text2).grid(row=1,sticky=W)

text3 = 'Example: 9y^(2) + 8y^(1) + 5y = 11u^(2) + 8u^(1)+2u'
Label(master, text=text3).grid(row=2,sticky=W)

text4 = '     ceofficients of Y:9 8 5'
Label(master, text=text4).grid(row=3,sticky=W)

text5 = '     ceofficients of U:11 8 2'
Label(master, text=text5).grid(row=4,sticky=W)

Label(master, 
      text="enter the ceofficients of differential equation:").grid(row=5,sticky=W)
Label(master, 
      text="          ceofficients of Y:").grid(row=6,sticky=W)
e1 = Entry(master)
e1.grid(row=6, column=0)
Label(master, 
      text="          ceofficients of U:").grid(row=8,sticky=W)
e2 = Entry(master)
e2.grid(row=8, column=0)

v = IntVar() 
Radiobutton(master, text='unit step', variable=v, value=1).grid(row=10, sticky=W) 
Radiobutton(master, text='impulse', variable=v, value=2).grid(row=11, sticky=W) 
Radiobutton(master, text='ramp', variable=v, value=3).grid(row=12, sticky=W)
Label(master, 
      text="          Simulation time (sec)").grid(row=13,sticky=W)
t = Entry(master)
t.grid(row=13, column=0)

var1 = IntVar() 
Checkbutton(master, text='Plot states', variable=var1).grid(row=14, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='State Space representation', variable=var2).grid(row=15, sticky=W) 
Button(master, 
          text='calculate', command=calculate).grid(row=16,sticky=W,column=0)

master.mainloop() 
