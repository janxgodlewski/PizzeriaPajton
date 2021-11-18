#!/usr/bin/env python
# coding: utf-8

# In[1]:

#matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')

#libs to create animation and add images to pie chart
from matplotlib.patches import PathPatch, Circle, Wedge, Polygon
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation

#libs to create video from animation
from IPython.display import HTML
from matplotlib import rc

fig, ax = plt.subplots()

#subplot title
fig.suptitle('Pizzeria Pajton', fontsize=14, fontweight='bold')

#chart data
totals=[2,5,3]
labels = ["Margherita [20%]", "Hawajska [50%]", "Capriciosa [30%]"]
files = ["Margherita.png", "Hawajska.png", "Capriciosa.png"]


#animation frame
def animate(i):
    #at the beginning of every frame axes needs to be cleared
    ax.clear()
    ax.set_xlabel('% Udział sprzedaży poszczególnych pizz w listopadzie', fontsize=10, fontweight='bold')
   
    #distance of every wedge from center of the chart
    distance = i * 0.004
    explodes = [distance,distance,distance]

    #draw chart
    wedges, texts = ax.pie(totals, startangle=18, labels=labels,  explode = explodes, wedgeprops = { 'linewidth': 3, "edgecolor" :"papayawhip", "fill":False,  })
    
    #display image on every wedge 
    for i in range(3):
        img_to_pie("C:\data\{}".format(files[i]), wedges[i], ax)

    return wedges

#function for displaying image on wedge
def img_to_pie(file, wedge, ax):
    #zoom and position of image in wedge
    zoom = 1
    position=(wedge.center[0], wedge.center[1])
    
    #read image
    image = plt.imread(file, format='png')
    
    #adjust image to chart wedge
    imagebox = OffsetImage(image, zoom, clip_path=wedge)
    
    #create annotation and add it to axes
    ab = AnnotationBbox(imagebox, position, xycoords='data', pad=0, frameon=False)
    ax.add_artist(ab)

#75 animation frames playing every 50 ms. Parameter blit ensures that we draw only these parts of chart which changed.
anim = FuncAnimation(fig, animate, frames=75, interval=50, blit=True)

rc('animation', html='html5')
anim


