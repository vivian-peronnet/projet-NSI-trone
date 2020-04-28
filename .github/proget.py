from tkinter import*
import tkinter as tk
# procédure générale de déplacement :
def avance(gd, hb):
     global x1, y1
     x1, y1 = x1 +gd, y1 +hb
     can1.coords(oval1, x1,y1, x1+30,y1+30)
def avance2(gd, hb):
     global x2, y2
     x2, y2 = x2 +gd, y2 +hb
     can1.coords(oval2, x2,y2, x2+30,y2+30)
# gestionnaires d'événements :
X1=[]
X2=[]
Y1=[]
Y2=[]
def depl_gauche(event):
     avance(-10, 0)
     X1.append(x1)
     Y1.append(y1)
     
def depl_droite(event):
     avance(10, 0)
     X1.append(x1)
     Y1.append(y1)
def depl_haut(event):
     avance(0, -10)
     X1.append(x1)
     Y1.append(y1)
def depl_bas(event):
     avance(0, 10)
     X1.append(x1)
     Y1.append(y1)
def depl_gauche2(event):
     avance2(-10, 0)
     X2.append(x2)
     Y2.append(y2)
def depl_droite2(event):
     avance2(10, 0)
     X2.append(x2)
     Y2.append(y2)
def depl_haut2(event):
     avance2(0, -10)
     Y2.append(y2)
def depl_bas2(event):
     avance2(0, 10)
     X2.append(x2)
     Y2.append(y2)
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 # coordonnées initiales
x2, y2 = 20,20

# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
# comparaison des coordonnée
coordonée1=[]
for i in range(len(X1)):
     coordonée1.append(X1[i])
     coordonée1.append(y1[i])
     print(fait)
coordonée2=[]
for i in range(len(X2)):
     coordonée2.append(X2[i])
     coordonée2.append(y2[i])
# création des widgets "esclaves" :
app = tk.Tk()
can1 = Canvas(fen1,bg='dark grey',height=600,width=600)
oval1 = can1.create_oval(x1,y1,x1+3,y1+3,width=1,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
app.bind("<KeyPress-d>",depl_gauche)
app.bind("<KeyPress-x>",depl_droite)
app.bind("<KeyPress-z>",depl_haut)
app.bind("<KeyPress-s>",depl_bas)
oval2 = can1.create_oval(x2,y2,x2+3,y2+3,width=1,fill='red')
app.bind("<KeyPress-l>",depl_gauche2)
app.bind("<KeyPress-m>",depl_droite2)
app.bind("<KeyPress-p>",depl_haut2)
app.bind("<KeyPress-:>",depl_bas2)
# démarrage du réceptionnaire d’évènements (boucle principale) :
fen1.mainloop()

