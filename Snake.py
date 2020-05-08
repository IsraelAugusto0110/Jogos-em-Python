#jogo Snake em python

from tkinter import *
from threading import Timer
import random

janela=Tk()
jogo=Canvas(janela,width=600,height=480)
jogo.pack()
for x in range(0,24):
	jogo.create_rectangle(0,20*x,20,20*(x+1),fill="green")
	jogo.create_rectangle(580,20*x,600,20*(x+1),fill="green")
for x in range(0,30):
	jogo.create_rectangle(20*x,0,20*(x+1),20,fill="green")
	jogo.create_rectangle(20*x,460,20*(x+1),480,fill="green")
cobra=[[1,10]]
jogo.gomo=[jogo.create_rectangle(0,0,20,20,fill="blue")]
jogo.posmaca=[1+random.randint(0,27),1+random.randint(0,21)]
jogo.maca=jogo.create_rectangle(20*(jogo.posmaca[0]),20*(jogo.posmaca[1]),20*(jogo.posmaca[0]+1),20*(jogo.posmaca[1]+1),fill="red")
jogo.direcao=2
def anda():
	if jogo.direcao==0:
        cobra[0][0]-=1;
	if jogo.direcao==1:cobra[0][1]-=1;
	if jogo.direcao==2:cobra[0][0]+=1;
	if jogo.direcao==3:cobra[0][1]+=1;
	for gomo in jogo.gomo:
		jogo.delete(gomo)
	for gomo in cobra:
		jogo.gomo.append(jogo.create_rectangle(20*(gomo[0]),20*(gomo[1]),20*(gomo[0]+1),20*(gomo[1]+1),fill="blue"))
	vivo=True
	for x in range(1,len(cobra)):
		if (cobra[0][0]==cobra[x][0])and(cobra[0][1]==cobra[x][1]):vivo=False
	if(cobra[0][0]>0)and(cobra[0][1]>0)and(cobra[0][0]<29)and(cobra[0][1]<23)and(vivo):
		t=Timer(.1,anda)
		t.start()
def key(event):
	if str(event.keycode)=="37":jogo.direcao=0
	if str(event.keycode)=="38":jogo.direcao=1
	if str(event.keycode)=="39":jogo.direcao=2
	if str(event.keycode)=="40":jogo.direcao=3
janela.bind("<Key>",key)
t=Timer(.1,anda)
t.start()
mainloop()