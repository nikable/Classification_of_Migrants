import numpy as np
import pandas as pd
from gensim import models
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances, cosine_distances, manhattan_distances
from text_processing import text_processed, split_string_2_data_array
from sklearn.model_selection import train_test_split


pd.set_option("display.max_columns", 100)
np.set_printoptions(threshold=np.inf)


def count_vectorizer_feature_vector():
    token_array = text_processed()
    training_token_array, test_token_array = split_string_2_data_array(token_array, 0.8)

    vectorizer = CountVectorizer(encoding='utf-8', analyzer='word', stop_words='english', binary='false',
                                 min_df=0.01)
    # tokenize and build vocab
    vec = vectorizer.fit(training_token_array)
    vec_matrix = vectorizer.fit_transform(training_token_array)
    # print(vectorizer.get_feature_names())
    f_vector = vectorizer.transform(training_token_array)
    # print(f_vector.shape)
    # print(f_vector.toarray())
    return (test_token_array, vec, vec_matrix)


def tf_idf_vect_feature_vector():
    df = text_processed()


    vectorizer = TfidfVectorizer()

    vec_train = vectorizer.fit_transform(df.Tweets)
    df['tweets_vec']  = list(vec_train.toarray())
    #df.to_csv('tfidf_vector.csv')
    train, test = train_test_split(df, test_size=0.2)


    print(vectorizer.get_feature_names())

    print(df)
    return test,train,df


def tf_idf_trans_feature_vector():
    token_array = text_processed()
    training_token_array, test_token_array = split_string_2_data_array(token_array, 0.8)
    print(token_array)
    vectorizer = TfidfTransformer(stop_words='english', analyzer="word")
    # tokenize and build vocab
    X = vectorizer.fit_transform(token_array)
    analyze = vectorizer.build_analyzer()
    print(analyze("subject is not the case"))
    # summarize
    print(vectorizer.get_feature_names())
    # summarize encoded vector
    print(X.toarray())
    return X


def word2vec_feature_vector():
    token_array = text_processed()
    print(token_array)
    model = models.Word2Vec(token_array, min_count=1)
    print(model)
    return


def cluster_indices(cluster_assignments):
    n = cluster_assignments.max()
    indices = []
    for cluster_number in range(1, n + 1):
        indices.append(np.where(cluster_assignments == cluster_number)[0])
    return indices


def compute_dissimalrity_matrix():
    token_array = text_processed()
    vectorizer = TfidfVectorizer(stop_words='english', analyzer="word")

    td_if = vectorizer.fit_transform(token_array)
    x = td_if.toarray()
    y = vectorizer.get_feature_names()
    print(x)
    print(y)
    matrix = euclidean_distances(td_if)

    # print(matrix)
    return matrix


def compute_similarity_matrix(model_matrix, pred_matrix):
    similarity_matrix = cosine_similarity(model_matrix, pred_matrix)
    return similarity_matrix


def compute_distance_matrix(model_matrix, pred_matrix, distance_matrix_type):
    distance_matrix = []
    if (distance_matrix_type == 'euclidean'):
        distance_matrix = euclidean_distances(model_matrix, pred_matrix)
    elif (distance_matrix_type == 'cosine'):
        distance_matrix = cosine_distances(model_matrix, pred_matrix)
    elif (distance_matrix_type == 'manhatten'):
        distance_matrix = manhattan_distances(model_matrix, pred_matrix)

    return distance_matrix
