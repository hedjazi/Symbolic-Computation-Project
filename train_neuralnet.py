import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import classification_report

import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
from keras.utils.np_utils import to_categorical

X = np.load('X_additional_position.npy')
Y = np.load('Y_additional_position.npy')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=1000)

num_classes = 3
batch_size = 128
epochs = 30

Y_train = to_categorical(Y_train, num_classes)
Y_test = to_categorical(Y_test, num_classes)

sgd = SGD(lr=0.01, decay=0.9, momentum=0.99, nesterov=False)

model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='random_uniform', input_shape=(8,)))
model.add(Dense(10, activation='relu', kernel_initializer='random_uniform'))
model.add(Dense(10, activation='relu', kernel_initializer='random_uniform'))
model.add(Dense(10, activation='relu', kernel_initializer='random_uniform'))
model.add(Dense(num_classes, activation='softmax'))
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

iteration = 0
folds = 10
kf = KFold(n_splits=folds, shuffle=False, random_state=1000)
for train_index, val_index in kf.split(X_train):
    print '------------------------- Training FOLD ', iteration, ' -------------------------------------------'
    Xtrain, Xval = X_train[train_index], X_train[val_index]
    Ytrain, Yval = Y_train[train_index], Y_train[val_index]
    history = model.fit(Xtrain, Ytrain, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(Xval, Yval))
    Y_estimated = model.predict(Xval)
    Y_estimated = np.argmax(Y_estimated, axis=1)
    Yval = np.argmax(Yval, axis=1)
    target_names = ['class 0', 'class 1', 'class 2']
    print classification_report(Yval, Y_estimated, target_names=target_names)
    iteration += 1
