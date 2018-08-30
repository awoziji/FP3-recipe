import sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.ensemble.partial_dependence import plot_partial_dependence

#important links -- read each link and try to apply method.  Look to generalize to any df for other projects:
######Metric evaluation
###http://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html#sphx-glr-auto-examples-model-selection-plot-multi-metric-evaluation-py
###http://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics
###http://scikit-learn.org/stable/model_selection.html
######Model evaluation
###http://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation
###http://scikit-learn.org/stable/modules/metrics.html#metrics
######Ensamble Methods
###http://scikit-learn.org/stable/modules/ensemble.html#forest
######SVM
###http://scikit-learn.org/stable/modules/svm.html#svm
######Persistance
###http://scikit-learn.org/stable/modules/model_persistence.html

file_num = 50
test_df = pd.read_csv('recipe_cuisine_recipe_info' + str(file_num) + '.csv')

{}


def randomForestClassifier(_X, _y, args = None):
    RFC_ = RandomForestClassifier()
    RFC_cross_validate = cross_val_score(RFC_, _X, _y)

def adaBoostClassifier(_X, _y, args = None):
    ABC_ = AdaBoostClassifier()
    ABC_cross_validate = cross_val_score(ABC_, _X, _y)

def gradientBoostingClassifier(_X, _y, args = None):
    GBC_ = GradientBoostingClassifier()
    GBC_cross_validate = cross_val_score(GBC_, _X, _y)

def VotingClassifier(estimators, args = None):
    VC_ = VotingClassifier(estimators = list(enumerate(estimators)))
