import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('preprocessed2.csv')
data.head()
data['Season'] = data['Season'].str.rstrip()
del data['Unnamed: 0']

training_data = list(np.array(data))
testing_data = training_data[100:120]
header = ['State_Name', 'District_Name', 'Season', 'Crop']

def unique_vals(Data,col):
    return set([row[col] for row in Data])

def class_counts(Data):
    counts= {}
    for row in Data:
        label =row[-1]
        if label not in counts:
             counts[label] = 0
        counts[label] += 1
    return counts

print(class_counts(training_data))

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
Question(0,'Bihar')


def partition(Data,question):
    true_rows,false_rows = [],[]
    for row in Data:
        if(question.match(row)):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows,false_rows
            
def gini(Data):
    counts = class_counts(Data)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl]/float(len(Data))
        impurity-=prob_of_lbl**2
    return impurity


def info_gain(left,right,current_uncertainity):
    p = float(len(left))/(len(left)+len(right))
    return current_uncertainity - p*gini(left) - (1-p)*gini(right)

def find_best_split(Data):
    best_gain = 0
    best_question = None
    current_uncertainity = gini(Data)
    n_features = len(Data[0]) - 1
    for col in range(n_features):
        values = unique_vals(Data,col)
        for val in values:
            question = Question(col,val)
            true_rows,false_rows = partition(Data,question)
            if(len(true_rows) == 0 or len(false_rows) == 0 ):
                continue
            gain = info_gain(true_rows,false_rows,current_uncertainity)
            if gain>best_gain:
                best_gain ,best_question =gain,question
    return best_gain,best_question

class Leaf:
    def __init__(self,Data):
        self.predictions = class_counts(Data)


class Decision_Node:
    def __init__(self,question,true_branch,false_branch):
        self.question=question
        self.true_branch = true_branch
        self.false_branch = false_branch

def build_tree(Data,i=0):
    gain, question = find_best_split(Data)
    if gain == 0 :
        return Leaf(Data)
    true_rows,false_rows =partition(Data,question)
    true_branch = build_tree(true_rows,i)
    false_branch = build_tree(false_rows,i)
    return Decision_Node(question,true_branch,false_branch)

my_tree = build_tree(training_data)
print(my_tree)


def print_tree(node,spacing=""):
    if isinstance(node,Leaf):
        print(spacing + "Predict",node.predictions)
        return
    print(spacing+str(node.question))
    print(spacing + "--> True:")
    print_tree(node.true_branch,spacing + " ")

    print(spacing + "--> False:")
    print_tree(node.false_branch,spacing + " ")

print_tree(my_tree)

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


from sklearn.externals import joblib 

joblib.dump(my_tree, 'filetest2.pkl') 