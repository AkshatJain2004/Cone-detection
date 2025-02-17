import cv2 as cv
import numpy as np

image = cv.imread('red.png')

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

lower = np.array([70,70,70])
upper = np.array([255,255,255])

mask = cv.inRange(hsv,lower,upper)
result = cv.bitwise_and(image, image, mask = mask)

gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 150)

contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

cone_centers = []
for contour in contours:
    if cv.contourArea(contour) > 65: 
        M = cv.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cone_centers.append((cx, cy))

cone_centers.sort(key=lambda x: x[1])

mid_x = np.mean([pt[0] for pt in cone_centers]) 
left_boundary = [pt for pt in cone_centers if pt[0] < mid_x]
right_boundary = [pt for pt in cone_centers if pt[0] >= mid_x]

def fit_and_draw_line(points, img, color):
    if len(points) > 1:
        points = np.array(points, dtype=np.int32)
        [vx, vy, x0, y0] = cv.fitLine(points, cv.DIST_L1, 0, 0.01, 0.01)
        slope = vy / vx
        intercept = y0 - slope * x0
        y1, y2 = img.shape[0], 0
        x1 = int((y1 - intercept) / slope)
        x2 = int((y2 - intercept) / slope)
        cv.line(img, (x1, y1), (x2, y2), color, 3)

fit_and_draw_line(left_boundary, image, (0, 0, 255))  
fit_and_draw_line(right_boundary, image, (0, 0, 255))  

cv.imwrite("answer.png", image)
cv.imshow("Detected Path", image)