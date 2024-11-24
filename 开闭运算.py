
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

#开，先腐蚀，后膨胀
img=cv2.imread(r"D:/picture/006.png")

kernel=np.ones((5,5),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow('opening',opening)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[3]:


#闭，先膨胀 后腐蚀
img=cv2.imread(r"D:/picture/006.png")

kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

cv2.imshow('closing',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

