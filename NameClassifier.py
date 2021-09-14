import pandas as pd
import numpy as np 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


def prepared_names(i):
    df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/nomes.csv')
    le = preprocessing.LabelEncoder()
    y = le.fit_transform(df.classification)
    names = df['first_name'].apply(lambda x: x.lower())

    vocab = set(' '.join([str(i) for i in names]))            
    vocab.add('END')
    len_vocab = len(vocab)
    char_index = dict((c, i) for i, c in enumerate(vocab))
    if i == 0:
        return(names, y, char_index, len_vocab)
    else:
        return (y, names)


def set_flag(i, len_vocab):
    aux = np.zeros(len_vocab);
    aux[i] = 1
    return list(aux)

def prepare_encod_names(X):
    maxlen = 14
    i = 0
    names, y, char_index, len_vocab = prepared_names(i)
    vec_names = []
    trunc_name = [str(i)[0:maxlen] for i in X]  
    for i in trunc_name:
        tmp = [set_flag(char_index[j], len_vocab) for j in str(i)]
        for k in range(0,maxlen - len(str(i))):
            tmp.append(set_flag(char_index["END"], len_vocab))
        vec_names.append(tmp)
    return vec_names

def data_split(names, y):
    x = prepare_encod_names(names.values)
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    y_train = np.asarray(y_train)
    y_test = np.asarray(y_test)
    return(X_train, y_train)

def data2df(x, y):
    df_x = pd.DataFrame(data=x.reshape((x.shape[0],-1)))
    df_y = pd.DataFrame(data=y.reshape((y.shape[0],-1)))
    
    df = pd.concat([df_x, df_y], axis=1)
    columns = list(df.columns)
    columns[-1] = 'class'
    df.columns = columns
    df = df.astype('int8')
    return df

def treino(df_train, y_train):
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(df_train, y_train)


def main(nomes):
    i = 1
    Y, names = prepared_names(i)
    x, y = data_split(names, Y)
    data = data2df(x, y)
    datay = data['class']
    data.drop('class', axis=1, inplace=True)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(data, datay)
    vec_nomes = prepare_encod_names(nomes)
    vec_nomes = np.asarray(vec_nomes)
    df_x = pd.DataFrame(data=vec_nomes.reshape((vec_nomes.shape[0],-1)))
    pred = knn.predict(df_x)
    return pred

