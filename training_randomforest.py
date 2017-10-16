import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X = np.load('X.npy')
Y = np.load('Y.npy')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=1000)

accuracy = 0

iteration = 0
folds = 10
kf = KFold(n_splits=folds, shuffle=False, random_state=1000)
for train_index, val_index in kf.split(X_train):
    print '------------------------- Training FOLD ', iteration, ' -------------------------------------------'
    Xtrain, Xval = X_train[train_index], X_train[val_index]
    Ytrain, Yval = Y_train[train_index], Y_train[val_index]
    clf = RandomForestClassifier(n_estimators=30, max_depth=None, min_samples_split=2, random_state=0)
    clf.fit(Xtrain, Ytrain)
    Y_estimated = clf.predict(Xval)
    accuracy += accuracy_score(Yval, Y_estimated)
    iteration += 1

print 'Accuracy: ', (accuracy/folds)
