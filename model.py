from sklearn.svm import LinearSVC
import numpy as np
import cv2 as cv
import PIL
from PIL import Image

class Model:
    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        if counters[0] <= 1 or counters[1] <= 1:
            print("Not enough data to train the model. Please capture more images.")
            return

        img_list = []
        class_list = []

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:,:,0]
            img = cv.resize(img, (120, 140))  # Resize if necessary
            img_list.append(img.flatten())  # Flatten the image
            class_list.append(1)

        for i in range(1, counters[1]):
            img = cv.imread(f'2/frame{i}.jpg')[:,:,0]
            img = cv.resize(img, (120, 140))  # Resize if necessary
            img_list.append(img.flatten())  # Flatten the image
            class_list.append(2)

        img_list = np.array(img_list)
        class_list = np.array(class_list)

        self.model.fit(img_list, class_list)
        print(f"Model successfully trained with {len(img_list)} samples!")
    
    def predict(self, frame):
        frame = frame[1]
        cv.imwrite('frame.jpg', cv.cvtColor(frame, cv.COLOR_RGB2GRAY))
        img = Image.open('frame.jpg')
        img = img.resize((120, 140), Image.ANTIALIAS)
        img.save('frame.jpg')

        img = cv.imread('frame.jpg')[:,:,0]
        img = img.reshape(120 * 140)  # Updated size
        prediction = self.model.predict([img])

        return prediction[0]