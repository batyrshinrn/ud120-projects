#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    to_remove = getmaxerrors(predictions, net_worths, 10)
    print "Remove inexes: ", to_remove

    cleaned_data = [(age[0], net_worths[i][0], predictions[i][0] - net_worths[i][0]) for i, age in enumerate(ages) if i not in to_remove]
    
    return cleaned_data


def getmaxerrors(predictions, net_worths, portion):
   
    count = int(len(predictions)*portion/100)
    maxerrors = []
    for i in range(count):
        maxerrors.append({ "err": 0, "index": 0})
    
    for i, item in enumerate(predictions):
        c_err = (predictions[i][0] - net_worths[i][0])**2
        appendmax(maxerrors, c_err, i)        

    return map(lambda x:x["index"], maxerrors)

def appendmax(array, value, i):
   result = min(array, key=lambda x:x['err'])
   if(result["err"] < value):
        result["err"] = value
        result["index"] = i


