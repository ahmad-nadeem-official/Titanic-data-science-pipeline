'''
here we have the main training loop for the model
we will use the RandomForestClassifier from sklearn
we will also use the LogisticRegression from sklearn
'''

x = data.iloc[::-1]
y = data['Survived']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

'''
logistic regression
'''

lr = LogisticRegression()
lr.fit(x_train, y_train)
lr.score(x_train, y_train)


'''
random forest classifier
'''

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(x_train, y_train)
rfc.score(x_train, y_train)


'''
Save the model
'''

joblib.dump(lr, 'LogisticRegression_trained_model.pkl')
print("model saved")

joblib.dump(rfc, 'RandomForestClassifier_trained_model.pkl')
print("model saved")