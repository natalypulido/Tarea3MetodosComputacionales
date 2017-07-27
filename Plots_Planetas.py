# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from datetime import datetime

sol = np.loadtxt("sol.txt")
mer = np.loadtxt("mercurio.txt")
ven = np.loadtxt("venus.txt")
tie = np.loadtxt("tierra.txt")
mar = np.loadtxt("marte.txt")
jup = np.loadtxt("jupiter.txt")
sat = np.loadtxt("saturno.txt")
ura = np.loadtxt("urano.txt")
nep = np.loadtxt("neptuno.txt")
plu = np.loadtxt("pluton.txt")

#pos = np.zeros((10,len(sol), 3))
#pos[0,:] = sol


labels = ["Sol", "Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton"]
colors = ["yellow", "grey", "orange", "blue", "red", "orange", "yellow", "cyan", "blue", "black"]

step = 50

todos = np.array([sol, mer,ven,tie,mar,jup,sat,ura,nep, plu])

corto = todos[:,::step]

fig = plt.figure()
ax = p3.Axes3D(fig)

text = ax.text(-40, -30, 5, "")
fixed = [ax.plot(corto[i, :, 0], corto[i, :, 1], corto[i, :, 2], c = colors[i]) for i in range(10)]
plots = [ax.plot([], [], [], "o", label = labels[i], color = colors[i])[0] for i in range(10)]
plots[0].set_marker("*")
plots[0].set_markersize(20)

ax.set_xlabel("$x$ (AU)")
ax.set_ylabel("$y$ (AU)")
ax.set_zlabel("$z$ (AU)")

plt.legend(numpoints=1)
fig.savefig("Orbitas.png")


ref_time = datetime(1970,1,1, 0, 0)
init_time = datetime(2016, 12, 11, 0, 0)
init_time = (init_time - ref_time).total_seconds()
largo = len(corto[0,:])
otroLargo = len(sol)
dt = 1.0/37
anoSec = 365.25*60*60*24


def init():
    for (j, line) in enumerate(plots):
        line.set_data([], [])
        line.set_3d_properties([])
    text.set_text("")
    return plots, text

def update(k):
    for (j, line) in enumerate(plots):
        line.set_data(corto[j, k, 0], corto[j, k, 1])
        line.set_3d_properties(corto[j, k, 2])
    cons = 1.0*dt*anoSec*otroLargo/largo
    tiemp = k*cons+init_time
    tiempo = datetime.utcfromtimestamp(tiemp)
    text.set_text(tiempo.strftime('%Y-%m-%d'))
    return plots, text


ani = animation.FuncAnimation(fig, update, largo, init_func = init)
ani.save("Planets.gif", writer = "imagemagick", fps = largo/30, dpi = 50)
plt.show()
ani.save("heh.gif", writer = "imagemagick")

