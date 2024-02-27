# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 09:26:22 2023

@author: urmii
"""

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.show()

#multiline plots
import matplotlib.pyplot as plt
x=range(1,5)
plt.plot(x,[xi*1.5 for xi in x])
plt.plot(x,[xi*3.0 for xi in x])
plt.plot(x,[xi/3 for xi in x])
plt.show()

#note how matplotlib aumatically
#choose different color
#for each line green for
#the first line blue for the second line
#and red for the third one(from top to bottom)
#grid axes and labels
#adding a grid
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*1.5,x,x*3.0,x,x/3.0)
plt.grid(True)
plt.show()


#handling axes
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,x*2.0,x,x*3.0,x,x/3.0)
plt.axis() #show the current axis limits values
plt.axis([0,5,-1,13]) #set new axes limits
#[xmin,smax,ymin,ymax]
#p0,5,-1,13]
plt.show()

#adding labels
import matplotlib.pyplot as plt
import numpy as np
plt.plot([1,2,3,4])
plt.xlabel("This is x axis")
plt.ylabel("This is y axis")
plt.show()

#adding titles
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.title("Simple plot")
plt.show()

#matplotlib provides a simple function, plt.title() to
#give the title to graph
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, x*1.5, label="Normal")
plt.plot(x, x*3.0, label="Fast")
plt.plot(x, x/3, label="Slow")
plt.legend()
plt.show()

#color abbriviation
#m=magenta
##y=yellow
#k=black
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x, 'y')
plt.plot(x+1, 'k')
plt.plot(x+2, 'm')
plt.show()

#specify styles in multiline plots
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,5)
plt.plot(x,'--')
plt.plot(x+1,'-')
plt.plot(x+2,':')
plt.show()

#marker abbreviation marker style
import matplotlib.pyplot as plt
import numpy as np
y=np.arange(1,3,0.2)
plt.plot(y,'x',y+0.5,'o',y+1,'D',y+1.5,'^',y+2,'s',y+2,'+',y+2.5,'h',y+3,'d',y+3.5,'H')
plt.show()

#Histogram chart
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)
plt.hist(x)
plt.show()

#bar graph
import matplotlib.pyplot as plt
plt.bar([1,2,3],[3,2,5])
plt.show()

#scatter plot
import matplotlib.pyplot as plt
import numpy as np
x=np.random.rand(1000)
y=np.random.rand(1000)
plt.scatter(x, y)
plt.show()


size=50*np.random.randn(1000)
colors=np.random.rand(1000)
plt.scatter(x,y, s=size,c=colors);
plt.show()

#adding text
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-4,4,1024)
y=.25*(x+4.)*(x+1.)*(x-2.)
plt.text(-0.5,0.25,'Brackmard minimum')
plt.plot(x,y,c='k')
plt.show()


















