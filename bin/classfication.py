from sklearn.svm import SVC
from feature_extraction import tf_idf_vect_feature_vector
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from IPython.display import Image
import pydotplus

def decision_tree_classification():
    df_test,df_train,df = tf_idf_vect_feature_vector()
    tree = DecisionTreeClassifier()
    tree = tree.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    dotfile = open("dtree2.dot", 'w')
    export_graphviz(tree, out_file=dotfile,filled=True, rounded=True,special_characters=True)
    graph = pydotplus.graph_from_dot_data(dotfile.getvalue())
    Image(graph.create_png())
    predict =tree.predict(df_test['tweets_vec'].tolist(),df_test.tag.tolist())
    print(predict)
    return predict

def svm_classification():
    df_test, df_train, df = tf_idf_vect_feature_vector()
    clf = SVC()
    clf.fit(df_train['tweets_vec'].tolist(), df_train['tag'].tolist())
    predict = clf.predict(df_test['tweets_vec'].tolist(), df_test.tag.tolist())
    print(predict)
    return predict



