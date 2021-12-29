import numpy as np
import math
import scipy.signal as signal
import matplotlib.pyplot as plt


def createSpace(radius):
    space = np.linspace(-radius,radius,radius+radius+1,dtype='float64')[np.newaxis]
    spacefloat = space.astype('float64')
    return spacefloat


def setVariables(a1,b1,A1,B1,a2,b2,A2,B2,a3,b3,A3,B3,a4,b4,A4,B4):
    parms = np.array([a1,b1,A1,B1,a2,b2,A2,B2,a3,b3,A3,B3,a4,b4,A4,B4])
    return parms

def scaleVariables(parms,amount):
    parms[0] *= amount
    parms[1] *= amount
    parms[4] *= amount
    parms[5] *= amount
    parms[8] *= amount
    parms[9] *= amount
    parms[12]*= amount
    parms[13]*= amount
    return parms


def createImg(image):
    img = plt.imread(image)
    img = img.astype('float64')
    return img


def createHKernel(a1,b1,a2,b2,a3,b3,a4,b4,space):
    # This function is mostly taken from Dr. Mike Pount at
    # https://github.com/mikepound/convolve
    size = space.shape
    lengt = size[1]
    
    kernel1_complex = np.zeros(lengt,dtype='complex64')[np.newaxis]
    kernel1_complex.real = np.exp(-a1* (space**2)) * np.cos(b1 * (space**2))
    kernel1_complex.imag = np.exp(-a1* (space**2)) * np.sin(b1 * (space**2))

    kernel2_complex = np.zeros(lengt,dtype='complex64')[np.newaxis]
    kernel2_complex.real = np.exp(-a2* (space**2)) * np.cos(b2 * (space**2))
    kernel2_complex.imag = np.exp(-a2* (space**2)) * np.sin(b2 * (space**2))

    kernel3_complex = np.zeros(lengt,dtype='complex64')[np.newaxis]
    kernel3_complex.real = np.exp(-a3* (space**2)) * np.cos(b3 * (space**2))
    kernel3_complex.imag = np.exp(-a3* (space**2)) * np.sin(b3 * (space**2))

    kernel4_complex = np.zeros(lengt,dtype='complex64')[np.newaxis]
    kernel4_complex.real = np.exp(-a4* (space**2)) * np.cos(b4 * (space**2))
    kernel4_complex.imag = np.exp(-a4* (space**2)) * np.sin(b4 * (space**2))
    return np.array([kernel1_complex,kernel2_complex,\
                     kernel3_complex,kernel4_complex])


def createVKernel(hkernel):
    kernel = hkernel.T
    return kernel



def visualizeKernel(kernel_1,kernel_2,kernel_3,kernel_4,\
                    A1,B1,A2,B2,A3,B3,A4,B4):  
    kernel1 = np.multiply(kernel_1,kernel_1.T)
    kernel2 = np.multiply(kernel_2,kernel_2.T)
    kernel3 = np.multiply(kernel_3,kernel_3.T)
    kernel4 = np.multiply(kernel_3,kernel_3.T)
    fullkernel = A1*kernel1.real + B1*kernel1.imag +\
                 A2*kernel2.real + B2*kernel2.imag +\
                 A3*kernel3.real + B3*kernel3.imag +\
                 A4*kernel4.real + B4*kernel4.imag
                
                 
    f,axarr = plt.subplots(1,3)
    axarr[0].imshow(kernel1.real+kernel2.real+kernel3.real+kernel4.real\
                    ,cmap='gray',interpolation='nearest')
    axarr[1].imshow(kernel1.imag+kernel2.imag+kernel3.imag+kernel4.imag\
                    ,cmap='gray',interpolation='nearest')
    axarr[2].imshow(fullkernel,cmap='gray',interpolation='nearest')
    plt.show()


def Bokeh(img,kernel_h1,kernel_h2,kernel_h3,kernel_h4,\
          A1,B1,A2,B2,A3,B3,A4,B4):
    kernel_v1 = kernel_h1.T
    kernel_v2 = kernel_h2.T
    kernel_v3 = kernel_h3.T
    kernel_v4 = kernel_h4.T
    img_h_1 = signal.convolve2d(img,kernel_h1,boundary='symm')
    img_v_1 = signal.convolve2d(img_h_1,kernel_v1,boundary='symm')
    img_out1 = A1*img_v_1.real + B1*img_v_1.imag

    img_h_2 = signal.convolve2d(img,kernel_h2,boundary='symm')
    img_v_2 = signal.convolve2d(img_h_2,kernel_v2,boundary='symm')
    img_out2 = A2*img_v_2.real + B2*img_v_2.imag

    img_h_3 = signal.convolve2d(img,kernel_h3,boundary='symm')
    img_v_3 = signal.convolve2d(img_h_3,kernel_v3,boundary='symm')
    img_out3 = A3*img_v_3.real + B3*img_v_2.imag

    img_h_4 = signal.convolve2d(img,kernel_h4,boundary='symm')
    img_v_4 = signal.convolve2d(img_h_4,kernel_v4,boundary='symm')
    img_out4 = A4*img_v_4.real + B4*img_v_4.imag 

    img_out = img_out1 + img_out2 + img_out3 + img_out4

    plt.imshow(img_out,cmap='gray')
    plt.show()

    

def visualizeStem(t,hkernel1,hkernel2,hkernel3,hkernel4,\
                  A1,B1,A2,B2,A3,B3,A4,B4):
    kernel1 = np.multiply(hkernel1,hkernel1.T)
    kernel1_real = kernel1.real
    kernel1_imag = kernel1.imag

    kernel2 = np.multiply(hkernel2,hkernel2.T)
    kernel2_real = kernel2.real
    kernel2_imag = kernel2.imag

    kernel3 = np.multiply(hkernel3,hkernel3.T)
    kernel3_real = kernel3.real
    kernel3_imag = kernel3.imag

    kernel4 = np.multiply(hkernel4,hkernel4.T)
    kernel4_real = kernel4.real
    kernel4_imag = kernel4.imag

    
    shape = kernel1_real.shape
    length = shape[0]
    half_length = (length-1)/2
    
    kernel1_real_1d = kernel1_real[int(half_length),:][np.newaxis]
    kernel1_imag_1d = kernel1_imag[int(half_length),:][np.newaxis]

    kernel2_real_1d = kernel2_real[int(half_length),:][np.newaxis]
    kernel2_imag_1d = kernel2_imag[int(half_length),:][np.newaxis]

    kernel3_real_1d = kernel3_real[int(half_length),:][np.newaxis]
    kernel3_imag_1d = kernel3_imag[int(half_length),:][np.newaxis]

    kernel4_real_1d = kernel4_real[int(half_length),:][np.newaxis]
    kernel4_imag_1d = kernel4_imag[int(half_length),:][np.newaxis]

    total = A1*kernel1_real_1d.T + B1*kernel1_imag_1d.T \
            + A2*kernel2_real_1d.T + B2*kernel2_imag_1d.T\
            + A3*kernel3_real_1d.T + B3*kernel3_imag_1d.T\
            + A4*kernel4_real_1d.T + B4*kernel4_imag_1d.T

    plt.plot(total)
    plt.show()


def normalizeKernels(hkernel1,hkernel2,hkernel3,\
                     hkernel4,A1,B1,A2,B2,A3,B3,A4,B4):
    #normalizes so that A1*real1 + B1*imag1 + A2*real2 + B2*imag2 ...etc. = 1
    sum1 = A1*np.sum(hkernel1.real)
    sum2 = B1*np.sum(hkernel1.imag)
    sum3 = A2*np.sum(hkernel2.real)
    sum4 = B2*np.sum(hkernel2.imag)
    sum5 = A3*np.sum(hkernel3.real)
    sum6 = B3*np.sum(hkernel3.imag)
    sum7 = A4*np.sum(hkernel4.real)
    sum8 = B4*np.sum(hkernel4.imag)
    
    total= sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8
    kernels = np.array([(1/total)*hkernel1,(1/total)*hkernel2,\
                       (1/total)*hkernel3,(1/total)*hkernel4])
    return kernels









