#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

maxTotal_payments = 0
employee = ""
quantifiedSalary = 0
quantifiedEmail = 0
totalPaymentsNaN = 0
totalPayments = 0
totalPoi = 0

for key, value in enron_data.items():
    if key != "TOTAL" and value["total_payments"] != "NaN" and value["total_payments"] > maxTotal_payments:
        maxTotal_payments = value["total_payments"]
        employee = key
    if value["salary"] != "NaN":
        quantifiedSalary += 1
    if value["email_address"] != "NaN":
        quantifiedEmail += 1
    if value["total_payments"] == "NaN":
        totalPaymentsNaN += 1
    if value["poi"] == True and value["total_payments"] == "NaN":
        totalPayments += 1
    if value["poi"] == True:
        totalPoi += 1

print len(enron_data.keys())
print maxTotal_payments
print employee
print quantifiedSalary
print quantifiedEmail
print "Total number of total payments == NaN: " + str(totalPaymentsNaN)
print "Total POI's with total payments == NaN: " + str(totalPayments)
print "Total POI's: " + str(totalPoi)

import sys
sys.path.append("../tools/")
from feature_format import featureFormat
from feature_format import targetFeatureSplit

feature_list = ["poi", "salary", "bonus"] 
data_array = featureFormat( enron_data, feature_list )
label, features = targetFeatureSplit(data_array)

print enron_data["LAY KENNETH L"]

# print label
# print features

#salary email_address


