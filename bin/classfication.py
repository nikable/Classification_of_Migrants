from sklearn.svm import SVC
from feature_extraction import tf_idf_vect_feature_vector
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from IPython.display import Image
import pydotplus
from sklearn.externals.six import StringIO
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

def decision_tree_classification():
    df_test,df_train,df = tf_idf_vect_feature_vector()
    tree = DecisionTreeClassifier()
    tree.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    print(tree)
    y_pred = tree.predict(df_test['tweets_vec'].tolist())
    accuracy = accuracy_score(df_test['tag'].tolist(), y_pred) * 100
    print("Accuracy score is :",accuracy)
    
    # Calculate metrics globally by counting the total true positives, 
    # false negatives and false positives.
    # Accuracy = TP + TN / (TP + TN + FP + FN)
    # Precision = TP / (TP + FP)
    # Recall = TP / (TP + FN)  Also known as sensitivity, or True Positive Rate
    # F1 = 2 * Precision * Recall / (Precision + Recall)
    
    # print('Accuracy:', accuracy_score(df_test['tag'].tolist(), y_pred)
    
    print('Recall:', recall_score(df_test['tag'].tolist(), y_pred))
    print('Precision:', precision_score(df_test['tag'].tolist(), y_pred))

    f1 = f1_score(df_test['tag'].tolist(), y_pred, average='micro')
    print('f1_score is', f1)

    #dotfile = open("dtree2.dot", 'w')
    # dotfile = StringIO()
    # export_graphviz(tree, out_file=dotfile,filled=True, rounded=True,special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dotfile.getvalue())
    # graph.write_png('plot.png')
    #predict =tree.predict(df_test['tweets_vec'].tolist(),df_test.tag.tolist())
    #print(predict)
    return tree

def svm_classification():
    df_test, df_train, df = tf_idf_vect_feature_vector()
    clf = SVC()
    clf.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    # Plot Decision Region using mlxtend's awesome plotting function
   # print(clf.score())
    plot_decision_regions(X=df_train['tweets_vec'].tolist(),y=df_train['tag'].tolist(),clf=clf,legend=2)
    # Update plot object with X/Y axis labels and Figure Title
    #plt.xlabel(X.columns[0], size=14)
    #plt.ylabel(X.columns[1], size=14)
    plt.title('SVM Decision Region Boundary', size=16)
    plt.show()

    #predict = clf.predict(df_test['tweets_vec'].tolist(), df_test.tag.tolist())
    predict = clf.predict(df_test['tweets_vec'].tolist(), df_test['tag'].tolist())
    print(predict)

    print('Recall:', recall_score(df_test['tag'].tolist(), predict))
    print('Precision:', precision_score(df_test['tag'].tolist(), predict))

    f1 = f1_score(df_test['tag'].tolist(), predict, average='micro')
    print("f1_score is :", f1)

    return predict



