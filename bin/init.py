
from text_processing import text_processed
from feature_extraction import tf_idf_vect_feature_vector
from classfication import decision_tree_classification,svm_classification


#array = text_processed()
#print(array)
vec = decision_tree_classification()
#vec = svm_classification()

print(vec)
#print(vec.toarray())
