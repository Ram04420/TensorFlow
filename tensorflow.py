# -*- coding: utf-8 -*-
"""Tensorflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lnw_hQMyljR01c_kVJma501xtXcYVmeQ
"""

import tensorflow as tf

from tensorflow import keras

print(tf.__version__)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mnist = keras.datasets.fashion_mnist

type(mnist)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train.shape, y_train.shape

np.max(x_train)

y_train

class_names =['top', 'trouser','pullover', 'dress', 'coat', 'sandal', 'shirt','sneaker','bag','ankle']

plt.figure()
plt.imshow(x_train[1])
plt.colorbar()

x_train = x_train/255.0
x_test = x_test/255.0

plt.figure()
plt.imshow(x_train[1])
plt.colorbar()

"""**Build the Model with TF 2.0**"""

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

model = Sequential()
model.add(Flatten(input_shape = (28,28)))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.summary()

784*128+128

"""**Model Compaliation**
* Loss Function
* Optimizer
* Metrics
"""

model.compile(optimizer='adam',loss ='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train,epochs=10)

test_loss, test_acc = model.evaluate(x_test, y_test)
print(test_acc)

from sklearn.metrics import accuracy_score

y_pred = model.predict_classes(x_test)

accuracy_score(y_test, y_pred)

pred = model.predict(x_test)

pred

y_pred

pred[0]

np.argmax(pred[0])

np.argmax(pred[1])

