import joblib
import cgitb
import cgitb

import joblib

cgitb.enable()
import sys



header = ['State_Name', 'District_Name', 'Season', 'Crop'] 

class Question:
    def __init__(self,column,value):
        self.column =column
        self.value=value
    def match(self,example):
        val = example[self.column]
        return val == self.value
    def match2(self,example):
        if example == 'True' or example == 'true' or example == '1':
            return True
        else:
            return False
    def __repr__(self):
        return "Is %s %s %s?" %(
            header[self.column],"==",str(self.value))
            
            
def class_counts(Data):
    counts= {}
    for row in Data:
        label =row[-1]
        if label not in counts:
             counts[label] = 0
        counts[label] += 1
    return counts


class Leaf:
    def __init__(self,Data):
        self.predictions = class_counts(Data)



class Decision_Node:
    def __init__(self,question,true_branch,false_branch):
        self.question=question
        self.true_branch = true_branch
        self.false_branch = false_branch




def print_tree(node,spacing=""):
    if isinstance(node,Leaf):
        print(spacing + "Predict",node.predictions)
        return
    print(spacing+str(node.question))
    print(spacing + "--> True:")
    print_tree(node.true_branch,spacing + " ")

    print(spacing + "--> False:")
    print_tree(node.false_branch,spacing + " ")




def print_leaf(counts):
    total = sum(counts.values())*1.0
    probs = {}
    for lbl in counts.keys():
        probs[lbl] =str(int(counts[lbl]/total * 100)) + "%"
    return probs




def classify(row,node):
    if isinstance(node,Leaf):
        return node.predictions
    if node.question.match(row):
        return classify(row,node.true_branch)
    else:
        return classify(row,node.false_branch)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

dt_model_final= joblib.load('C:/xampp/htdocs/agriculture-portal-main/farmer/ML/crop_prediction/filetest2.pkl') 

data = pd.read_csv('preprocessed2.csv')
data.head()
data['Season'] = data['Season'].str.rstrip()
del data['Unnamed: 0']

training_data = list(np.array(data))
testing_data = training_data[100:120]
for row in testing_data:
    Predict_dict = (print_leaf(classify(row,dt_model_final))).copy()
from sklearn.metrics import accuracy_score
prediction = list(Predict_dict.keys())
print(testing_data)
print(prediction)
print(accuracy_score(testing_data[0:13][-1],prediction))
# state =sys.argv[1]
# district=sys.argv[2]
# season=sys.argv[3]


# testing_data = [[state,district,season]]



# for row in testing_data:
#     Predict_dict = (print_leaf(classify(row,dt_model_final))).copy()


# for key, value in Predict_dict.items() :
#     print (key)
#     print ("  ,  ")


