import matplotlib.pyplot as plt
import random

#En esta seccion se definen cuantas canicas/bolas caeran y posteriormente en cuantas lineas
BOLAS_TOTALES = 3000
LINEAS_TOTALES = 12


def galton(bolas, lineas) -> list:
	dist = [0] * ((lineas * 2) + 1)

	for ball in range(0, bolas):
		total = 0
		
		for line in range(1, lineas+1):	
			outcome = random.uniform(0, 1)
			if(outcome >= 0.5):
				total += 1
			else:
				total -= 1	
		dist[total + lineas] += 1 

	for i in range(0, lineas + 1):
		dist[i] = dist[i*2]	

	return dist[0:lineas+1]

def plot_galton(dist, lineas):
	plt.bar([str(i) for i in range(0, lineas + 1)], dist[0:lineas+1])
	plt.xticks([])
	plt.show()

dist = galton(BOLAS_TOTALES, LINEAS_TOTALES)
plot_galton(dist, LINEAS_TOTALES)
plt.show()