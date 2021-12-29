import matplotlib.pyplot as plt
from bokeh_funcs import *


t = createSpace(20)

parms = setVariables(.00917,.00904,1.8,1.0)

parms = scaleVariables(1.0,parms)

img = createImg('deepspace_gray.jpg')


plt.imshow(img,cmap='gray')
plt.show()

hkernel = createHKernel(parms[0],parms[1],t)
hkernel = normalizeKernel(hkernel,parms[2],parms[3])

vkernel = hkernel.T

visualizeKernel(hkernel,vkernel,parms[2],parms[3])
visualizeStem(t,hkernel,parms[2],parms[3])

separateBokeh(hkernel,vkernel,img,parms[2],parms[3])
