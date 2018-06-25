
from text_processing import text_processed
from feature_extraction import tf_idf_vect_feature_vector


#array = text_processed()
#print(array)
vec = tf_idf_vect_feature_vector()

#print(test_token_array)
print(vec.toarray())
