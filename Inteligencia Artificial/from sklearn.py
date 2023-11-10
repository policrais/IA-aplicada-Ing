from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Cargar el conjunto de datos de iris
iris = load_iris()
X = iris.data
y = iris.target

# Seleccionar dos características (para simplificar la visualización)
features = [2, 3]  # Índices de las características (petal length y petal width)
X_subset = X[:, features]

# Crear un clasificador de árbol de decisión
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_subset, y)

# Mostrar la estructura básica del árbol de decisión
tree_rules = export_text(clf, feature_names=[iris.feature_names[i] for i in features])
print("Estructura del árbol:\n", tree_rules)
