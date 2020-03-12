# -*- coding: utf-8 -*-

import cv2

import numpy as np




def removeRedEye():







    img = cv2.imread('lab12_image.png')

    cv2.imshow("Lab 12 Image", img) #(first field is name of window, second field is

    #height = img.shape[0]

    #height, width, channels = img.shape

    height, width, channels = img.shape

    # img2 = np.zeros(shape =(height,width))

    #(B,G,R)

    #nested for loop needed-- scans line by line,row by row

    for i in range(height):

        for j in range(width):

            if img[i,j,1] < n and img[i,j,0] < n: #brightness level

                img[i,j,2] = 0

                img[i,j,0] = 0

                img[i,j,1] = 0




    cv2.imshow("Red Eye Removed", img)

    cv2.waitKey()

    cv2.destroyallWindows()

    '''
    
    • img[i,j,0] = blue channel of pixel (i,j) • img[i,j,1] = green channel of pixel (i,j) • img[i,j,2] = red channel of pixel (i,j)
    
    '''

    # WILL ONLY OPEN USING COMMAND PROMPT

    #Need to access (B,G,R) tuple for indidivudal pixels and get rid of red. each pixel has this tuple.

    #check for blue and green channels being less than 40 to find red. If both are less than 40, it's red. Then change all channels to black (which is 0)

    # look at opencv documentation

    n=40







removeRedEye()