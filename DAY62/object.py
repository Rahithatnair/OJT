

import cv2
import matplotlib.pyplot as plt

# Load the pretrained classifier of Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Upload an image for test
image = cv2.imread('face.jpg')
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(grey_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print(f"No of faces detected: {len(faces)}")

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Convert BGR image to RGB for display
img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
