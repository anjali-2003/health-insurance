import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# reading the data.
df = pd.read_csv(r'C:\Users\ANIRUDDHA\OneDrive\Desktop\anju\insurance\health.csv')

X = df.drop('PremiumPrice', axis=1)
Y = df['PremiumPrice']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=1)

# Import the Algorithm 

#from sklearn.tree import DecisionTreeRegressor

# created the model
model = LinearRegression()
#dtr = DecisionTreeRegressor()

# training of the model
model.fit(X_train, y_train)
#dtr.fit(X_train, y_train)

pickle_out = open(r"C:\Users\ANIRUDDHA\OneDrive\Desktop\anju\insurance\model.pkl", "wb")
pickle.dump(model, pickle_out)
pickle_out.close()
