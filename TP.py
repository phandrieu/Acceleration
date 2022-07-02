#Import des bibliothèques

import math
import matplotlib.pyplot as plt

#Récupération des lignes du fichier

fileName = "Aller-Retour.csv"
file = open(fileName, 'r')
fileLines = list(file)
file.close()

#Extraction des données

t, ax, ay = [], [], []
vx, vy= [0],[0]
x, y = [0], [0]

for i in range(2, len(fileLines)):
    currentLine = fileLines[i].rstrip()
    data = currentLine.split(";")
    t.append(float(data[0]))
    ax.append(float(data[1]))
    ay.append(float(data[2]))

#Correction des données en soustrayant la moyenne des données obtenues

meanx = sum(ax)/len(ax)
meany = sum(ay)/len(ay)

for i in range(len(t)):
    ax[i] = ax[i]-meanx
    ay[i] = ay[i]-meany

#Méthode d'Euler : Primitivation de l'accélération et de la vitesse

for i in range(1, len(t)):
    vx.append((t[i]-t[i-1])*ax[i]+vx[i-1])
    vy.append((t[i]-t[i-1])*ay[i]+vy[i-1])

for i in range(1, len(t)):
    x.append((t[i]-t[i-1])*vx[i]+x[i-1])
    y.append((t[i]-t[i-1])*vy[i]+y[i-1])

plt.plot(x, y)
plt.show()

#Calcul de la distance max

xmax = max(x)
ymax = max(y)
d = (math.sqrt(xmax**2 + ymax**2))
print(d)
