import cv2
import numpy as np
import imutils

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

ortogonal = cv2.imread(".\example-asset.png", 4)
h,w = ortogonal.shape[:2]
print ('image height and width = ' +str(h) + " x " + str(w)) # 318 * 348 pixels
divition_size = 16

numcol = int(w / divition_size)
numrow = int(h / divition_size)

start_x = 0
start_y = 0
for countx in range(0,numcol-1):
    for county in range(0,numrow-1):
        
        isometric = ortogonal[county*divition_size:county*divition_size + divition_size, countx*divition_size:countx*divition_size+ divition_size]  # crop image at [h1:h2, w1:w2]
        isometric_rotated = imutils.rotate_bound(isometric, angle=45)
        isometric_resized = cv2.resize(isometric_rotated, (0,0), fx=2, fy=1) 
        #img_vacia[0:int(rotated_width),0:int(rotated_width)] = rotate_image(isometric, 45)
        cv2.imwrite('asset' + str(countx) + "_" + str(county) + '.png',isometric_resized)
        start_x = start_x + divition_size
        print(str(start_y) + " : " + str(start_y + divition_size) + " ,  " + str(start_x)+ " : " + str(start_x+ divition_size))
    




primera = cv2.imread('asset0_0.png',4)
height = primera.shape[0]
width = primera.shape[1]
start_x = 0
start_y = 0

nueva_img = np.zeros((height*(numrow-1), width*(numcol-1),3), dtype=np.uint8)
for countx in range(0,numcol-1):
    for county in range(0,numrow-1):
        nueva_img[county*height:county*height + height, countx*width:countx*width+ width] = cv2.imread('asset' + str(countx) + "_" + str(county) + '.png')
        start_x = start_x + width
    start_y = start_y + height

cv2.imwrite("./created-asset.png", nueva_img)

