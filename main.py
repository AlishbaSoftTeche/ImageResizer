import cv2

source= "image.jpg"
destination = 'newimage.jpg'
scale_percent = 50

image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
cv2.imshow("title", image)
cv2.waitKey(0)


width = int(image.shape[1]*scale_percent /100)
height = int(image.shape[0]*scale_percent /100)

desize = (width,height)

output = cv2.resize(image,desize)

cv2.imwrite(destination,output)
cv2.waitKey(0)