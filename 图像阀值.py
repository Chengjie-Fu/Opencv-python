
# coding: utf-8

# In[4]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

image_gray=cv2.imread(r"D:/picture/003.webp",cv2.IMREAD_GRAYSCALE)


# In[6]:


ret,thresh1=cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY)


# In[7]:


ret,thresh2=cv2.threshold(image_gray,127,255,cv2.THRESH_BINARY_INV)


# In[8]:


ret,thresh3=cv2.threshold(image_gray,127,255,cv2.THRESH_TRUNC)


# In[9]:


ret,thresh4=cv2.threshold(image_gray,127,255,cv2.THRESH_TOZERO)


# In[12]:


ret,thresh5=cv2.threshold(image_gray,127,255,cv2.THRESH_TOZERO_INV)


# In[15]:


titles=["Original Image","Binary","Binary_Inv","Trunc","Tozero","Tozero_Inv"]
images=[image_gray,thresh1,thresh2,thresh3,thresh4,thresh5]


# In[21]:


for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


# In[22]:


ret

