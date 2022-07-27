import pytesseract
import cv2

# image = cv2.imread('card_1.jpg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imwrite('temp/gray.png', gray)

# blur = cv2.GaussianBlur(gray, (15, 15), 0)
# cv2.imwrite('temp/blur.png', blur)

# thresh = cv2.threshold(blur, 0, 225, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
# cv2.imwrite('temp/thresh.png', thresh)


# kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 10))
# cv2.imwrite('temp/kernal.png', kernal)

# dilate = cv2.dilate(thresh, kernal, iterations=1)
# cv2.imwrite('temp/dilate.png', dilate)

# cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0] if len(cnts) == 2 else cnts[1]
# cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

# for c in cnts:
#     x, y, w, h = cv2.boundingRect(c)
#     cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)
# cv2.imwrite('temp/bbox.png', image)


# Let's load a simple image with 3 black squares
image = cv2.imread('scorecards/card_1.jpg')
  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (15, 15), 0)
cv2.imwrite('temp/card_blur.png', blur)
  
edged = cv2.Canny(blur, 30, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if h>100 and w > 100:
        cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)
cv2.imwrite('temp/old_new_edge.png', image)


  
cv2.imshow('Canny Edges After Contouring', edged)
  
print("Number of Contours found = " + str(len(contours)))
  
# Draw all contours
# -1 signifies drawing all contours
contour_img = cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
  
cv2.imwrite('temp/contour_img.png', contour_img)