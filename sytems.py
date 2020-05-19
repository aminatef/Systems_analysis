import random
import math
import matplotlib.pyplot as plt

y = [0 for i in range(0,10000)]
h=0.001
n=int(input("enter order of system : " ))
coefficient_of_diff=[]
for i in range(n+2):
	coefficient_of_diff.append(float(input("enter a"+str(i)+" : ")))
free_term = coefficient_of_diff[-1]
c2=[(1/pow(h,i))*coefficient_of_diff[i] for i in range(n+1)]
print("c1",coefficient_of_diff)
print('c2',c2)
def blinomial_coeffcient(n,i):
	return (math.factorial(n))/(math.factorial(i)*math.factorial((n-i)))
def get_diff_of_n(n,k,y,h):
	FD_nth_diff = 0
	def finite_diffrance(y,k,i):
		return y[k-i]
	# print("order of diff:",n)
	for i in range(1,n+1):
		if i % 2 == 0:
			sign = 1
		else:
			sign = -1 
		# print(sign,blinomial_coeffcient(n,i),"y[k-",i,"]")
		FD_nth_diff += (sign * blinomial_coeffcient(n,i) * finite_diffrance(y,k,i)) 
	return FD_nth_diff/pow(h,n)
for i in range(n+1,10000):
	list_diffs=[get_diff_of_n(order,i,y,h) * coefficient_of_diff[order] for order in range(1,n+1)]
	sum_coef = math.fsum(c2)
	# print("f\'--  ", list_diffs[0])
	# print("f\'\'--  ", list_diffs[1])
	sum_diffs = math.fsum(list_diffs)
	y[i] = (-(sum_diffs)+free_term)/(sum_coef)
	# print(y[i])
y_dash=[]
for i in range(len(y)-1):
	y_dash.append(abs(y[i+1]-y[i])/h)
f=plt.figure()
plt.plot(y)
f1=plt.figure()
plt.plot(y_dash)
plt.show()

