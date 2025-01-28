import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Image//download.jpg")
# visualize pixel intensitiy distribution using histogram like a graph or the plot

# for grey scale histogram
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
grey_hist = cv.calcHist([grey],[0], None, [256], [0,256])
plt.figure()
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(grey_hist)
plt.xlim([0,256])
plt.show()

# lets create masking and focus on that part nd see how the histogram look
blank = np.zeros(img.shape[:2],'uint8')
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(grey,grey,mask=mask)

grey_hist_mask = cv.calcHist([grey],[0], mask, [256], [0,256])
plt.figure()
plt.title("masked")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(grey_hist_mask)
plt.xlim([0,256])
plt.show()

# compute color histogram
# instead of convert the color to grey scale 
color = ('b','g','r')
plt.figure()
plt.title("color histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],masked, [256], [0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)