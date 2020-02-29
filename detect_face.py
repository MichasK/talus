import cv2
import os


def weighted_center_of_face(img_rgb):
    '''

    :param img_rgb:
    :return: if one face is detected return powierzchnia twarzy, else -1
    '''
    # Convert into grayscale
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    # Detect faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) != 1 or faces[0][3] * faces[0][2] > 10000:
        return (-1, -1)
    else:
        scale_vector = int(round(faces[0][3] / 2))
        return (faces[0][0] + scale_vector, faces[0][1] + scale_vector)

'''
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
directory = 'zdjecia/'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):

        img = cv2.imread(r'zdjecia/' + filename)
        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Display the output

        img = cv2.circle(img, weighted_center_of_face(img), 2, (255, 0, 0), 2)
        cv2.imshow('img', img)
        cv2.waitKey()

'''
