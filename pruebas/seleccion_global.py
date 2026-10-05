from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
X,y=load_iris(return_X_y=True)
cv=StratifiedKFold(n_splits=10,shuffle=True,random_state=42)
busqueda=GridSearchCV(Pipeline([('escala',StandardScaler()),('knn',KNeighborsClassifier())]),{'knn__n_neighbors':[3,5,7]},cv=5)
busqueda.fit(X,y)
scores=cross_val_score(busqueda.best_estimator_,X,y,cv=cv)
