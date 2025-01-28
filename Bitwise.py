import cv2 as cv
import numpy as np
# pixel is turn off is the value is 0 and on if its value is 1

blank = np.zeros((400,400), 'uint8')
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle", circle)

# bitwise: AND = it return an intersection or what is common it both img
bit_and = cv.bitwise_and(rectangle,circle)
cv.imshow("AND",bit_and)

# bitwise: OR = it return both intersection and the not intersection
bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow("OR",bit_or)

# bitwise: XOR = it return the non intersection
bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",bit_xor)

# bitwise: NOT = it invert the binary color and only take 1 img
bit_not = cv.bitwise_not(rectangle)
cv.imshow("NOT",bit_not) # so it invert from black to white and white to black sth like that
cv.waitKey(0)