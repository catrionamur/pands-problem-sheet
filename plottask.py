# plottask.py
# This program plots x^2 against y^3 for range of numbers from 0 to 4
# Author: Catriona Murray
import matplotlib.pyplot as plt #import mathplotlib library                                                                                                                                                                                                                                                           
import numpy as np #import numpy to use array 
range = np.array(range(0,4))
gpoints = range * range #multiply each entry by itself range squared
hpoints = range * range * range #range cubed
plt.style.use('dark_background') #set the color of the background to plack
plt.plot(gpoints, hpoints, color='#aa77cc', label = "f(x)=x" ) #plot graph set color of line to purple and set the label
plt.title("plottask.py",size=18) #set the title and set the font of the title to 18
plt.xlabel("$g(x)=_{x^2}$", size=16) #Set x axis label with x squared in italic
plt.ylabel("$h(x)=_{x^3}$",size=16) #Set y axis label with y in italic
plt.legend(loc ='upper center') #Place the legend in the center
plt.show()