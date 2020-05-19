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
#comparaison des coordoner
def triSelection_2(a) :
    n = len(a)
    for i in range(0,n-1,2) : 
        k = i
        for j in range(i+1,n-1,2) :
            if a[k] > a[j] : k = j
        a[k],a[i] = a[i],a[k]
        a[k+1],a[i+1]=a[i+1],a[k+1]
def comp_1(y,z):
     y=co1
     z=co2
     indice=[]
     element=co1[-2]
     triSelection_2(co1)
     triSelection_2(co2)
     prer=[]
     a = 0
     b = len(co1)-1
     m = (a+b)//2
     
     while a < b :
         if co1[m] == element :
               indice.append(m)
               return m
         elif co1[m] > element :
             b = m-2
         else :
             a = m+2
         m = (a+b)//2
     for i in indice:
          prer.append(co2[i+1])
     element=co1[-1]
     a = 0
     b = len(prer)-1
     m = (a+b)//2
     while a < b :
         if prer[m] == element :
             return m
         elif prer[m] > element :
             b = m-2
         else :
             a = m+2
         m = (a+b)//2
         if a!=0:
              print("game over")

def comp_2(co1,co2):
     indice=[]
     element=co1[-2]
     triSelection_2(co1)
     triSelection_2(co2)
     prer=[]
     a = 0
     b = len(co2)-1
     m = (a+b)//2
     while a < b :
         if co2[m] == element :
             return m
         elif co2[m] > element :
             b = m-1
         else :
             a = m+1
         m = (a+b)//2
         indice.append(a)
     for i in indice:
          prer.append(co1[i+1])
     element=co1[-1]
     a = 0
     b = len(prer)-1
     m = (a+b)//2
     while a < b :
         if prer[m] == element :
             return m
         elif prer[m] > element :
             b = m-1
         else :
             a = m+1
         m = (a+b)//2
         if a!=0:
          print("game over")
# gestionnaires d'événements :
def depl_gauche(event):
     avance(-10, 0)
     co1.append(x1)
     co1.append(y1)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_droite(event):
     avance(10, 0)
     co1.append(x1)
     co1.append(y1)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_haut(event):
     avance(0, -10)
     co1.append(x1)
     co1.append(y1)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_bas(event):
     avance(0, 10)
     co1.append(x1)
     co1.append(y1)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_gauche2(event):
     avance2(-10, 0)
     co2.append(x2)
     co2.append(y2)
     comp1(co1,co2)
     comp2(co1,co2)
def depl_droite2(event):
     avance2(10, 0)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_gauche2(event):
     avance2(-10, 0)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_haut2(event):
     avance2(0, -10)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_gauche2(event):
     avance2(-10, 0)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_bas2(event):
     avance2(0, 10)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
def depl_gauche2(event):
     avance2(-10, 0)
     co2.append(x2)
     co2.append(y2)
     comp_1(co1,co2)
     comp_2(co1,co2)
#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 # coordonnées initiales
x2, y2 = 20,20
co1=[]
co2=[]
co1.append(x1)
co1.append(y1)
co2.append(x2)
co2.append(y2)
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

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
