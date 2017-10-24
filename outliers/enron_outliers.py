#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

def getBonuses(seq):
    for el in seq:
        if el["bonus"] == "NaN":
            yield 0
        else:
            yield el["bonus"]

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]

maxBonus = max(getBonuses(data_dict.values()))
print "max bonus: ", maxBonus
outlier = [ k for k, v in data_dict.iteritems() if v["bonus"] == maxBonus ].pop()
print outlier
data_dict.pop(outlier, 0)

print [k for k, v in data_dict.iteritems() if v["bonus"] != "NaN" and v["bonus"] > 5000000 and v["salary"] > 1000000]



data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()




