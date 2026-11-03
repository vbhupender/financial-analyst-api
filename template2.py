# assignment4.py

import sys
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, f1_score

def bayes_knn_classifier(x):
    """
    Train and evaluate a Bayes or KNN classifier based on the value of x.
    To be implemented by the student.
    """
    # TODO: Implement the logic based on x
    # Hint: Use conditional statements to handle different ranges of x
    # Use train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    # for every hold-out evaluation

    if x <= 0:
        X, y = load_wine(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        model = GaussianNB(var_smoothing=10**x)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        
    elif 0 < x < 1:
        X, y = load_digits(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        model = MultinomialNB(alpha=x)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        
    elif 1 <= x < 20:
        X, y = load_iris(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        k = int(np.floor(x))
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        
    elif 20 <= x < 50:
        X, y = load_wine(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        k = int(np.floor(x / 5))
        pipeline = make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=k, weights='distance')
        )
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        
    elif 50 <= x < 100:
        X, y = load_breast_cancer(return_X_y=True)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=42, stratify=y
        )
        k = int(np.floor(x)) - 49
        pipeline = make_pipeline(
            StandardScaler(),
            KNeighborsClassifier(n_neighbors=k, metric='manhattan')
        )
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)
        score = f1_score(y_test, y_pred)
        
    else:  # x >= 100
        X, y = load_digits(return_X_y=True)
        k = int(np.floor(np.sqrt(x)))
        model = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(model, X, y, cv=5)
        score = np.mean(scores)
        
    return round(score, 4)


def main():
    if len(sys.argv) != 2:
        print("Usage: python assignment4.py <number>")
        sys.exit(1)

    try:
        x = float(sys.argv[1])
    except ValueError:
        print("Please enter a valid number.")
        sys.exit(1)

    result = bayes_knn_classifier(x)
    print(f"Output: {result:.4f}\n")

if __name__ == "__main__":
    main()
