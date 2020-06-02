import tkinter as tk
def triSelection_2(a) :
    n = len(a)
    for i in range(0,n-1,2) : 
        k = i
        for j in range(i+1,n-1,2) :
            if a[k] > a[j] : k = j
        a[k],a[i] = a[i],a[k]
        a[k+1],a[i+1]=a[i+1],a[k+1]
def comp_1(y,z):
     co1=y
     co2=z
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
motion = {
    'q': (-10, 0),
    's': (10, 0),
    'z': (0, -10),
    'w': (0, 10),
    'p': (-10, 0),
    'l': (10, 0),
    'm': (0, -10),
    ':': (0, 10),
    }
 
motion1 = {
    'q': (-10, 0),
    's': (10, 0),
    'z': (0, -10),
    'w': (0, 10),
    }
motion2 = {
    'p': (-10, 0),
    'l': (10, 0),
    'm': (0, -10),
    ':': (0, 10),
    }
 
def on_key1(event):
    co1=[]
    co2=[]
    if not event.char in motion.keys():
        return
    if event.char in motion2.keys():
        x20, y20=10,0
        d2x, d2y = motion2[event.char]
        canvas.move('ball2', d2x, d2y)
        x20, y20, x21, y21 = canvas.bbox('ball2')
        c20 = (x20+x21)/2
        c21 = (y20+y21)/2
        line.extend([c20, c21])
        canvas.coords('line2', line)
        print("c20=",c20,c21)
        co2.append(x20)
        co2.append(y20)
        
 
    if event.char in motion1.keys() :
        x10, y10= -10, 0
        d1x, d1y = motion1[event.char]
        canvas.move('ball1', d1x, d1y)
        x10, y10, x11, y11 = canvas.bbox('ball1')     
        c10 = (x10+x11)/2
        c11 = (y10+y11)/2
        line.extend([c10, c11])
        canvas.coords('line1', line)
        print("c1=",x10, y10)
        co1.append(x10)
        co1.append(y10)
    comp_2(co2,co1)
    comp_1(co1, co2)

 
   
canvas = tk.Canvas(width=600, height=600)
canvas.pack()
 
canvas.create_oval(5, 5, 15, 15, fill='red', tag='ball1')
canvas.create_oval(5, 5, 15, 15, fill='red', tag='ball2')
line = [10, 10, 10, 10]
canvas.create_line(line, tag='line1')
canvas.create_line(line, tag='line2')
canvas.bind('<Key>', on_key1)
canvas.focus_set()
tk.mainloop()
