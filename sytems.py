import random
import math
import matplotlib.pyplot as plt

h = 0.0005

iterations = 10000
u = [1 for i in range(0,iterations)]

n = int(input("enter order of Y :" ))
m = int(input("enter order U :" )) 

y = [[0 for i in range(0,iterations)] for j in range(n+1)]

coefficient_of_diff_Ys = []
coefficient_of_diff_Us = []

for i in range(n+1):
	coefficient_of_diff_Ys.append(float(input("enter a"+str(i)+" : ")))
for i in range(m+1):
	coefficient_of_diff_Us.append(float(input("enter b"+str(i)+" : ")))

c2=[(1/pow(h,i))*coefficient_of_diff_Ys[i] for i in range(n+1)]

print("c1",coefficient_of_diff_Ys)
print('c2',c2)

def blinomial_coeffcient(n,i):
	return (math.factorial(n))/(math.factorial(i)*math.factorial((n-i)))


def finite_diffrance(y,k,i):
	return y[k-i]


def numercal_diff_finite_diffrance(n,k,u,h):
	FD_nth_diff = 0
	# print("order of diff:",n)
	for i in range(0,n+1):
		if i % 2 == 0:
			sign = 1
		else:
			sign = -1 
		# print(sign,blinomial_coeffcient(n,i),"y[k-",i,"]")
		FD_nth_diff += (sign * blinomial_coeffcient(n,i) * finite_diffrance(u,k,i)) 
	return FD_nth_diff/pow(h,n)

def get_diff_of_n(n,k,y,h):
	FD_nth_diff = 0
	# print("order of diff:",n)
	for i in range(1,n+1):
		if i % 2 == 0:
			sign = 1
		else:
			sign = -1 
		# print(sign,blinomial_coeffcient(n,i),"y[k-",i,"]")
		FD_nth_diff += (sign * blinomial_coeffcient(n,i) * finite_diffrance(y,k,i)) 
	return FD_nth_diff/pow(h,n)
def numircal_diff_2(y,j,h):
	y_dash=[]
	for i in range(j+1,len(y)):
		y_dash.append(numercal_diff_finite_diffrance(j,i,y,h))
	return y_dash

y1=[]

for i in range(n+1,iterations):
	list_diffs_Ys = [get_diff_of_n(order,i,y[0],h) * coefficient_of_diff_Ys[order] for order in range(1,n+1)]
	sum_coef_Ys = math.fsum(c2)
	sum_diffs_Ys = math.fsum(list_diffs_Ys)
	y[0][i] = (-(sum_diffs_Ys)+u[i])/(sum_coef_Ys)

for j in range(1,len(y)):
	y[j] = numircal_diff_2(y[0],j,h)

for i in range(iterations-(n+1)):
	sum1=0
	for j in range(m+1):
		sum1 += y[j][i] * coefficient_of_diff_Us[j]
	y1.append(sum1)

f1=plt.figure()
plt.plot(y1)

# for i in range(len(y)):
# 	f1=plt.figure()
# 	plt.plot(y[i])

for i in range(n):
	print("[q{}\']".format(i+1),end="")
	print("[ ",end="")
	if i == n-1:
		for j in range(n):
			print("-{} ".format((coefficient_of_diff_Ys[j])/(coefficient_of_diff_Ys[n])),end="")
	else:
		for j in range(n):
			if j == i+1 :
				print("1 ",end="")
			else:
				print("0 ",end="")
	print("] ",end="")
	print("[q{}]".format(i+1),end=" ")
	if i == n-1:
		print("[{}]".format(1/coefficient_of_diff_Ys[n]))
	else:
		print('[0]')






plt.show()

