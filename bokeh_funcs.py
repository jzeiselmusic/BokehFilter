import numpy as np
import math
import scipy.signal as signal
import matplotlib.pyplot as plt


def createSpace(radius):
    space = np.linspace(-radius,radius,radius+radius+1,dtype='float64')[np.newaxis]
    spacefloat = space.astype('float64')
    return spacefloat


def setVariables(a1,b1,A,B):
    parms = np.array([a1,b1,A,B])
    return parms


def scaleVariables(mult,parms):
    return mult*parms



def createImg(image):
    img = plt.imread(image)
    img = img.astype('float64')
    return img


def createHKernel(a,b,space):
    kernel = np.exp(-a * (space**2)) * np.exp(b*1j* (space**2))
    return kernel


def createVKernel(hkernel):
    kernel = hkernel.T
    return kernel



def visualizeKernel(kernel_h,kernel_v,A,B):
    kernel1 = np.multiply(kernel_h,kernel_v)

    f,axarr = plt.subplots(1,3)
    axarr[0].imshow(kernel1.real,cmap='gray',interpolation='nearest')
    axarr[1].imshow(kernel1.imag,cmap='gray',interpolation='nearest')
    axarr[2].imshow((A*kernel1.real+B*kernel1.imag)/(A+B),cmap='gray',interpolation='nearest')
    plt.show()


def separateBokeh(kernel_h,kernel_v,img,A,B):
    img_h_1 = signal.convolve2d(img,kernel_h,boundary='symm')
    img_v_1 = signal.convolve2d(img_h_1,kernel_v,boundary='symm')
    img_out = (A*img_v_1.real + B*img_v_1.imag)/(A+B)

    plt.imshow(img_out,cmap='gray')
    plt.show()

    

def visualizeStem(t,hkernel,A,B):
    kernel = np.multiply(hkernel,hkernel.T)
    kernel_real = kernel.real
    kernel_imag = kernel.imag
    shape = kernel_real.shape
    length = shape[0]
    half_length = (length-1)/2
    
    kernel_real_1d = kernel_real[int(half_length),:][np.newaxis]
    kernel_imag_1d = kernel_imag[int(half_length),:][np.newaxis]

    plt.stem(A*t.T,kernel_real_1d.T + B*kernel_imag_1d.T)
    plt.show()


def normalizeKernel(hkernel,A,B):
    #normalizes so that A*real + B*imag = 1
    sum1 = A*np.sum(hkernel.real)
    sum2 = B*np.sum(hkernel.imag)
    total= sum1+sum2
    return (1/total)*hkernel












    
