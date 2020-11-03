import seaborn as sns
import sklearn
import joblib 
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split


#récupère un dataset déjà enregistré dans seaborn
#Je choisis iris parce que c'est un dataset facila a utilser et qui me permet de rattrapper les cours que j'ai manqué 
iris = sns.load_dataset('iris')

Y = iris['species'].astype('category').cat.codes
X = iris.drop('species', axis='columns')



clf = KNN(n_neighbors=3)
clf.fit(X,Y)


joblib.dump(clf, 'irisclassifier.joblib')