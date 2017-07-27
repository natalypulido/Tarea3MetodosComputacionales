import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation  


puntos=300
x=30.0
y=30.0
c=1.0
r=0.5


udelpasado=np.zeros((302,302))
udelinicio=np.zeros((302,302))
udelinicio[100, 151]=-0.5
udelpresente=np.zeros((302,302))
udelfuturo=np.zeros((302,302))

delta_x=(x/(float(puntos-1.0)))
delta_y=(y/(float(puntos-1.0)))
delta_t=(float(delta_x*r))/c

gamma=(2*(c**2)*delta_t/delta_x)
tetha=(float(c*delta_t)/delta_x)**2

tde60=1200
tde30=600

milista=[]


def mi_funcion(tiempo):
	matriz_de_mask=np.ones((302, 302))
	matriz_de_mask[200,:]=np.zeros((1,302))
	matriz_de_mask[200,140:170]=np.ones((1,30))


	for i in range (1, puntos-1):
		for j in range (1, puntos-1):
			udelfuturo[i,j]=gamma*(udelinicio[i+1,j]-udelinicio[i-1,j])+gamma*(udelinicio[i,j+1]-udelinicio[i,j-1])
	

	udelpasado=udelinicio.copy()
	udelpresente=udelfuturo.copy()*matriz_de_mask
	milista.append(udelpresente)


	for n in range (1, tiempo):
		for i in range (1,puntos-1):
			for j in range (1,puntos-1):
				udelfuturo[i,j]=tetha*(udelpresente[i+1,j]-2*udelpresente[i,j]+udelpresente[i-1,j])+tetha*(udelpresente[i,j+1]-2*udelpresente[i,j]+udelpresente[i,j-1])+2*udelpresente[i,j]-udelpasado[i,j]

		
		udelpasado=udelpresente.copy()
		udelpresente=udelfuturo.copy()*matriz_de_mask
		milista.append(udelpresente)
		
	return udelpresente, milista
	


plt.imshow(mi_funcion(tde60)[0], cmap="hot")
plt.title('Resultado de 60 segundos')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.savefig("Resultado_60.png")
plt.close()

plt.imshow(mi_funcion(tde30)[0])
plt.title('Resultado de 30 segundos')
plt.savefig("Resultado_30.png")
plt.close()


primero=mi_funcion(350)[1]
cubeta=plt.figure()
cubetin=plt.imshow(np.abs(primero[0]), extent=(30+delta_x, 30-delta_x, 30+delta_y, 30-delta_y))	
color_bar=plt.colorbar()
color_bar.ax.set_ylabel('Amplitud', rotation=0)

def animacion(time):
	cubetin.set_array(abs(primero[time]))
	return cubetin
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Nataly'), bitrate=1800)

animacionshis = animation.FuncAnimation(cubeta, animacion, np.arange(1, len(milista)), interval=20, blit=False)
plt.title('Propagacion de la onda')
plt.show()

im_ani.save('Onda.mp4', write=write)







##iterar en tiempo, y, x 
##for i in tiempo
	##for n
		##for m 
##gradiente=0

##Animacion: lo primero es poner plt.show()
#funcAnimate recibe 2 parametros: la figura y la funcion que va a animar
##funcAnimate(fig, func)
#fig=plt.figure
#funcion= def func (i): mi i sera la n 
##def funcion (i):
	#datos=lista[i]
	#cubeta.set_array(datos)
	#return cubeta, 
##quien es cubeta: cubeta,=plt.plot(x,y) o tambien: cubeta,=plt.imshow()
#hacer un plot imshow()
#plot.setdata 

#fig =plt.figure()
#cubetin,=plt.imshow(f[0])

#def animacion (m):
#	losdatos=f[m]
#	cubetin.set_array(losdatos)
#	return cubetin,
#anim = animation.FuncAnimation(fig, animacion, frames=200, interval=20, blit=True)
	

