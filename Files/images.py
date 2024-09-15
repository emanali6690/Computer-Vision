import cv2

# Load an image from the Images folder
img = cv2.imread('Images/sample_image.jpg')

# Display the image in a window
cv2.imshow('Image', img)

# Wait until a key is pressed to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

