# Symbolic-Computation-Project

In this project, we are going to predict the number of solutions given a polynomial (2nd degree) using ML methods.
After that, we will try to generalize it for a d-degree (3rd, 4th, and maybe more) polynomial.

Using Random Forest Model, we got the following scores for:

- The validation set:
             precision    recall  f1-score   support
    class 0       0.99      0.99      0.99     17777
    class 1       1.00      0.90      0.95        50
    class 2       1.00      1.00      1.00     45173
avg / total       1.00      1.00      1.00     63000

- The test set:
             precision    recall  f1-score   support
    class 0       0.99      0.99      0.99     19758
    class 1       0.98      0.98      0.98        46
    class 2       1.00      1.00      1.00     50196
avg / total       1.00      1.00      1.00     70000

We see that the precision is almost 99% given that we have little samples from class 1 (46 only).

