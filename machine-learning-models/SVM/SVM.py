try:
    import numpy as np
    import pandas as pd
    from sklearn import svm
    from sklearn.metrics import confusion_matrix
    from sklearn.model_selection import train_test_split
    from nltk import classify
    from nltk.classify.scikitlearn import SklearnClassifier
    from joblib import load, dump
except Exception as e:
    print(e)

class SVM:
    """
    
    Classe para a criação e manipulação do SVM com as bibliotecas sklearn e nltk.
    
    """
    def __init__(self, model="rbf", path="SVM/Models/"):
        """
        
        Args:
            model [string] : modelo a ser utilizado.
                   Valores disponíveis: linear, linearsvc, rbf, nurbf, poly, nupoly, sigmoid, nusigmoid.
            path [string] : localização dos modelos, caso já exista modelos treinados. 

        """
        self.data = None
        try:
            self.clf = load(r'{}{}.hdf5'.format(path, model.lower()))
        except:
            self.clf = None
        self.acc = None

    def classify(self, value):
        """
        
        Classifica os dados desejados a partir do modelo definido.

        Args:
            value [string/list] : Dados a serem classificados.

        Return [string/list] :
            Resultado da classificação.

        Raises:
            Erro do tipo Exception caso não seja encontrado um modelo treinado.
        """

        if self.clf == None:
            raise Exception("Impossible to classify. Untrained SVM.")
        if type(value) == str:
            return self.clf.classify(self.prepareData(value,op=2))
        else:
            return self.clf.classify_many(self.prepareData(value, op=1))   

    def prepareData(self, names, genders=0, op=0):
        """
        Pré-processamento dos dados para ser feita a classificação ou treinamento.

        Args:
            names [string/list] : nome(s) a ser classificados.
            genders [int/list] : gênero referente ao nome (utilizado para o treinamento).
                            padrão: 0
                            valores possíveis: 0, 1
            op [int] : Opção para utilização da função.
                        0 - Treinamento do svm.
                        1 - Lista de nomes para classificação.
                        2 - Único nome para classificação.

        Return [dict/list]:
            Dicionario ou lista de dicionarios para a classificação.
        """

        if type(genders) == int:
            genders = [0]*len(names)
        dataSet = list()
        for name, gender in zip(names, genders):
            name = name.lower()
            dictName = {'name':name,
                        'firstChar':name[0],
                        'lastChar':name[-1],
                        'lastTwoChar':name[-2:],
                        'lastThreeChar':name[-3:],
                        'length':len(name)
                        }
            if op == 0:
                dataSet.append((dictName, gender))
            if op == 1:
                dataSet.append(dictName)
            if op == 2:
                return dictName

        return dataSet

    def training(self, typeSVM="linearsvc", test_size=0.2, random_state=28, database="SVM/grupos.csv"):
        """
        Treinamento do SVM.

        Args:
            typeSVM [string] : tipo de modelo a ser utilizado.
                        Valores disponíveis: linear, linearsvc, rbf, nurbf, poly, nupoly, sigmoid, nusigmoid.
                        padrão: linearsvc.
            test_size [float] : relação de divisão dos dados de teste e treinamento. Exemplo: 20% da base de dados para teste reflete em test_size=0.2.
                        padrão: 0.2
            random_state [int] : randomização dos dados.
                        padrão: 28
            database [string] : local do arquivo com os dados para o treinamento.
                        padrão: "SVM/grupos.csv"
        
        Raises:
            Erro do tipo Exception caso não seja encontrada a base de dados.
            Erro do tipo Exception caso não seja definido uma opção valida para o tido de modelo.
        
        """

        try:
            dfData = pd.read_csv(r""+database)
        except:
            raise Exception("Impossible to do training. Database not found.")
        
        names = dfData["name"].apply(lambda x: x.lower())
        classification = dfData['classification']

        self.data = self.prepareData(names, classification)

        treino, teste = train_test_split(self.data, test_size=test_size, random_state=random_state)

        if typeSVM.lower() == "linear":
            self.clf = SklearnClassifier(svm.SVC(kernel="linear", C=10.0))
            dump(self.clf,r"SVM/Models/linear.hdf5")
        elif typeSVM.lower() == "linearsvc":
            self.clf = SklearnClassifier(svm.LinearSVC(C=1.0, max_iter=1000000))
            dump(self.clf,r"SVM/Models/linearsvc.hdf5")
        elif typeSVM.lower() == "rbf":
            self.clf = SklearnClassifier(svm.SVC(kernel="rbf", gamma=0.01, C=100.0))
            dump(self.clf,r"SVM/Models/rbf.hdf5")
        elif typeSVM.lower() == "nurbf":
            self.clf = SklearnClassifier(svm.NuSVC(kernel="rbf", gamma=0.01, nu=0.1))
            dump(self.clf,r"SVM/Models/nurbf.hdf5")
        elif typeSVM.lower() == "poly":
            self.clf = SklearnClassifier(svm.SVC(kernel='poly', gamma='auto', degree=1, C=100.0))
            dump(self.clf,r"SVM/Models/poly.hdf5")
        elif typeSVM.lower() == "nupoly":
            self.clf = SklearnClassifier(svm.NuSVC(kernel='poly', gamma='auto', degree=1, nu=0.3))
            dump(self.clf,r"SVM/Models/nupoly.hdf5")
        elif typeSVM.lower() == "sigmoid":
            self.clf = SklearnClassifier(svm.SVC(kernel='sigmoid', gamma=0.01, C=0.01))
            dump(self.clf,r"SVM/Models/sigmoid.hdf5")
        elif typeSVM.lower() == "nusigmoid":
            self.clf = SklearnClassifier(svm.NuSVC(kernel='sigmoid', gamma=0.01, nu=0.9))
            dump(self.clf,r"SVM/Models/sigmoid.hdf5")
        else:
            raise Exception("SVM model not available.")

        self.clf = self.clf.train(treino)
        self.acc = classify.accuracy(self.clf, teste)

if __name__ == "__main__":
    svc = SVM()
    svc.training(typeSVM = "linearsvc")
    print(svc.acc)
    print(svc.classify(["Gabriel", "Milena", "Walkir"]))