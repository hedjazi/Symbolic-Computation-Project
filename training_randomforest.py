import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = np.load('X.npy')
Y = np.load('Y.npy')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.10, random_state=1000)

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
    target_names = ['class 0', 'class 1', 'class 2']
    print classification_report(Yval, Y_estimated, target_names=target_names)
    iteration += 1

Y_estimated = clf.predict(X_test)
target_names = ['class 0', 'class 1', 'class 2']
print classification_report(Y_test, Y_estimated, target_names=target_names)
