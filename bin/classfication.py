from sklearn import svm
from feature_extraction import tf_idf_vect_feature_vector
from sklearn.tree import DecisionTreeClassifier
import numpy as np

def decision_tree_classification():
    df_test,df_train,df = tf_idf_vect_feature_vector()
    tree = DecisionTreeClassifier()
    tree.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    tree.predict(df_test['tweets_vec'].tolist(),df_test.tag.tolist())

def svm_classification():
    df_test, df_train, train_vect, df = tf_idf_vect_feature_vector()
    tree = DecisionTreeClassifier()
    tree.fit(train_vect, df_train['tag'].tolist())
    tree.predict(df_test.Tweets.tolist(), df_test.tag.tolist())



