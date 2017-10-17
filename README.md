# Symbolic-Computation-Project

In this project, we are going to predict the number of solutions given a polynomial (2nd degree) using ML methods.
After that, we will try to generalize it for a d-degree (3rd, 4th, and maybe more) polynomial.

Using Random Forest Model, we got the following scores for:

- The validation set:

                precision    recall  f1-score   support:
              
      class 0       0.99      0.99      0.99     17777.
      
      class 1       1.00      0.90      0.95        50.
      
      class 2       1.00      1.00      1.00     45173.
      
      avg / total       1.00      1.00      1.00     63000.
      

- The test set:

                precision    recall  f1-score   support.
                
      class 0       0.99      0.99      0.99     19758.
      
      class 1       0.98      0.98      0.98        46.
      
      class 2       1.00      1.00      1.00     50196.
      
      avg / total       1.00      1.00      1.00     70000.
      

We see that the precision is almost 99% given that we have little samples from class 1 (46 only).

Using Neural Net Model, we got the following scores for the validation set:

                precision    recall  f1-score   support
             
      class 0       0.99      0.89      0.94     17777

      class 1       0.00      0.00      0.00        50

      class 2       0.96      1.00      0.98     45173

      avg / total       0.96      0.96      0.96     63000

The results are not quite well because the precision fo class 1 is 0 which means it's misclassifying all of it, this is due to the fact that we have few samples (50), in the other hand, Random Forest seems not to be affected by this.

In the following experiment we tried to augment the number of samples for class 1 and test an NN to see the difference:

- Validation set:

             precision    recall  f1-score   support
             
      class 0       0.98      0.93      0.95     17967

      class 1       0.99      0.88      0.94      1851

      class 2       0.97      0.99      0.98     44982

      avg / total       0.97      0.97      0.97     64800


- Test set:

             precision    recall  f1-score   support
             
      class 0       0.98      0.93      0.95     19792

      class 1       0.99      0.88      0.93      2040

      class 2       0.97      0.99      0.98     50168

      avg / total       0.97      0.97      0.97     72000

