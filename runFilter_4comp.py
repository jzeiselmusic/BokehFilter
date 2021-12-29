import matplotlib.pyplot as plt
from bokeh_funcs_4comp import *





t = createSpace(50)

parms = setVariables(4.338,1.553,-5.767,46.164,\
                     3.839993, 4.693183, 9.795391, -15.227561,\
                     2.791880, 8.178137, -3.048324, 0.302959, \
                     1.342190, 12.328289, 0.010001, 0.244650)

parms = scaleVariables(parms,.001)

img = createImg('deep_space_gray2.jpg')


plt.imshow(img,cmap='gray')
plt.show()

hkernels = createHKernel(parms[0],parms[1],parms[4],parms[5],parms[8],parms[9],\
                         parms[12],parms[13],t)

hkernel1 = hkernels[0]
hkernel2 = hkernels[1]
hkernel3 = hkernels[2]
hkernel4 = hkernels[3]

hkernels = normalizeKernels(hkernel1,hkernel2,hkernel3,hkernel4,parms[2],parms[3],\
                            parms[6],parms[7],parms[10],parms[11],\
                            parms[14],parms[15])
hkernel1 = hkernels[0]
hkernel2 = hkernels[1]
hkernel3 = hkernels[2]
hkernel4 = hkernels[3]


visualizeKernel(hkernel1,hkernel2,hkernel3,hkernel4,\
                parms[2],parms[3],parms[6],parms[7],\
                parms[10],parms[11],parms[14],parms[15])

visualizeStem(t,hkernel1,hkernel2,hkernel3,hkernel4,\
              parms[2],parms[3],parms[6],parms[7],parms[10],\
              parms[11],parms[14],parms[15])

Bokeh(img,hkernel1,hkernel2,hkernel3,hkernel4,\
      parms[2],parms[3],parms[6],parms[7],parms[10],parms[11],\
      parms[14],parms[15])

