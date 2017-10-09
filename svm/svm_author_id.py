#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

#########################################################
from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000.0)

# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
print "start trining"
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
print "start predict"
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"
print "elem 10: ", pred[10]
print "elem 26: ", pred[26]
print "elem 50: ", pred[50]

count = sum(pred)
print "Chris count ", count 

print("calc accurancy")
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print(acc)