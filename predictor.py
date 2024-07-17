from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score  
from sklearn.pipeline import Pipeline


model = RandomForestClassifier(n_estimators=300)

# my_pipeline = column