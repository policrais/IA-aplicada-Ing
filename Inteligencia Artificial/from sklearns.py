from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data
y = iris.target

# Crear y entrenar el clasificador de árbol de decisión con profundidad máxima de 2
clf = DecisionTreeClassifier(max_depth=2, random_state=42)
clf.fit(X, y)

# Visualizar el árbol de decisión
plt.figure(figsize=(8, 5))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
