import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import os

def obtener_ruta_datos():
    # obtiene la ruta al archivo de datos
    script_dir = os.path.dirname(__file__)
    project_dir = os.path.dirname(script_dir)
    return os.path.join(project_dir, 'data', 'spam.csv')

def entrenar_modelo():
    data_path = obtener_ruta_datos()
    data = pd.read_csv(data_path, encoding= 'latin-1')
    data = data [['v1', 'v2']]
    data.columns = ['label', 'text']

    X_train, X_test, y_train, y_test = train_test_split(
         data['text'], data ['label'], test_size=0.2, random_state= 42
    )

    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(X_train_vec, y_train)
    print("Modelo entrenado exitosamente")
    return model, vectorizer

def predecir_spam(texto, modelo, vectorizer):
    vec = vectorizer.transform([texto])
    pred = modelo.predict(vec)[0]

    if pred == "spam":
         return "spam"
    else:
         return "no spam"
def evaluar_modelo(modelo, vectorizer):
    data_path = obtener_ruta_datos()
    data = pd.read_csv (data_path, encoding='latin-1')
    data = data[['v1', 'v2']]
    data.columns = ['label', 'text']
    
    X_train, X_test, y_train, y_test = train_test_split(
        data['text'], data ['label'], test_size=0.2, random_state= 42
    )

    X_test_vec = vectorizer.transform( X_test)
    predictions = modelo.predict(X_test_vec)
    accuracy = accuracy_score(y_test, predictions)

    return accuracy
    


