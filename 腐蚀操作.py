
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

img=cv2.imread(r"D:/picture/006.png")
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)

cv2.imshow('erosion',erosion)
cv2.waitKey()
cv2.destroyAllWindows()


# In[6]:


pie=cv2.imread(r"D:/picture/007.webp")
cv2.imshow('pie',pie)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[9]:


kernel=np.ones((30,30),np.uint8)
erosion_1=cv2.erode(pie,kernel,iterations=1)
erosion_2=cv2.erode(pie,kernel,iterations=2)
erosion_3=cv2.erode(pie,kernel,iterations=3)
res=np.hstack((erosion_1,erosion_2,erosion_3))
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

