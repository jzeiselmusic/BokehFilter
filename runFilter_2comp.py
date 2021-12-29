import matplotlib.pyplot as plt
from bokeh_funcs_2comp import *





t = createSpace(50)

parms = setVariables(0.8865,5.2689,0.411,-0.548,1.9605,1.5582,0.513,4.56)

parms = scaleVariables(parms,.001)

img = createImg('deep_space_gray2.jpg')


plt.imshow(img,cmap='gray')
plt.show()

hkernels = createHKernel(parms[0],parms[1],parms[4],parms[5],t)

hkernel1 = hkernels[0]
hkernel2 = hkernels[1]

hkernels = normalizeKernels(hkernel1,hkernel2,parms[2],parms[3],\
                            parms[6],parms[7])
hkernel1 = hkernels[0]
hkernel2 = hkernels[1]


visualizeKernel(hkernel1,hkernel2,parms[2],parms[3],parms[6],parms[7])

visualizeStem(t,hkernel1,hkernel2,parms[2],parms[3],parms[6],parms[7])

Bokeh(hkernel1,hkernel2,img,parms[2],parms[3],parms[6],parms[7])
