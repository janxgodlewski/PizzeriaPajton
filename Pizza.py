#!/usr/bin/env python
# coding: utf-8

# In[1]:


#matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')

#do animacji i nałożenia zdjęć
from matplotlib.patches import PathPatch, Circle, Wedge, Polygon
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation

#wyświetlenie wideo w HTML
from IPython.display import HTML
from matplotlib import rc

fig, ax = plt.subplots()

#tytuł subplota
fig.suptitle('Pizzeria Pajton', fontsize=14, fontweight='bold')

#dane do wykresu
totals=[2,5,3]
labels = ["Margherita [20%]", "Hawajska [50%]", "Capriciosa [30%]"]
files = ["Margherita.png", "Hawajska.png", "Capriciosa.png"]


#klatka animacji 
def animate(i):
    #na początku każdej klatki animacji należy wyczyścić plota
    ax.clear()
    ax.set_xlabel('% Udział sprzedaży poszczególnych pizz w listopadzie', fontsize=10, fontweight='bold')
   
    #odległość ćwiartek wykresu od środka
    distance = i * 0.004
    explodes = [distance,distance,distance]

    #rysowanie wykresu
    wedges, texts = ax.pie(totals, startangle=18, labels=labels,  explode = explodes, wedgeprops = { 'linewidth': 3, "edgecolor" :"papayawhip", "fill":False,  })
    
    #nałożenie zdjęcia na każdą ćwiartkę wykresu
    for i in range(3):
        img_to_pie("C:\data\{}".format(files[i]), wedges[i], ax)

    return wedges

#funkcja do nałożenia zdjęcia na ćwiartkę
def img_to_pie(file, wedge, ax):
    #przybliżenie i pozycja zdjęcia w ćwiartce
    zoom = 1
    position=(wedge.center[0], wedge.center[1])
    
    #wczytujemy zdjęcie
    image = plt.imread(file, format='png')
    
    #dopasowujemy zdjęcie do ćwiartki wykresu
    imagebox = OffsetImage(image, zoom, clip_path=wedge)
    
    #stworzenie adnotacji i dodanie jej 
    ab = AnnotationBbox(imagebox, position, xycoords='data', pad=0, frameon=False)
    ax.add_artist(ab)

#40 klatek animacji odtwarzanych co 50 ms. Parametr sprawia, że rysujemy tylko ten fragment wykresu, który się zmienił.
anim = FuncAnimation(fig, animate, frames=75, interval=50, blit=True)

rc('animation', html='html5')
anim


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




