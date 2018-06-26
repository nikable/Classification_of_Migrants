
from sklearn.svm import SVC
from feature_extraction import tf_idf_vect_feature_vector
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from IPython.display import Image
import pydotplus
from sklearn.externals.six import StringIO
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt

def decision_tree_classification():
    df_test,df_train,df = tf_idf_vect_feature_vector()
    tree = DecisionTreeClassifier()
    tree = tree.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    print(tree)
    #dotfile = open("dtree2.dot", 'w')
    dotfile = StringIO()
    export_graphviz(tree, out_file=dotfile,filled=True, rounded=True,special_characters=True)
    graph = pydotplus.graph_from_dot_data(dotfile.getvalue())
    Image(graph.create_png())
    #predict =tree.predict(df_test['tweets_vec'].tolist(),df_test.tag.tolist())
    #print(predict)
    return tree

def svm_classification():
    df_test, df_train, df = tf_idf_vect_feature_vector()
    clf = SVC()
    clf.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    # Plot Decision Region using mlxtend's awesome plotting function
    print(clf.score())
    plot_decision_regions(X=df_train['tweets_vec'].tolist(),y=df_train['tag'].tolist(),clf=clf,legend=2)

    # Update plot object with X/Y axis labels and Figure Title
    #plt.xlabel(X.columns[0], size=14)
    #plt.ylabel(X.columns[1], size=14)
    plt.title('SVM Decision Region Boundary', size=16)
    plt.plot
    plt.show()

    predict = clf.predict(df_test['tweets_vec'].tolist(), df_test.tag.tolist())
    print(predict)
    return predict



