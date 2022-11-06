from django.shortcuts import render

def home(request):

    return render(request,'home.html')

def predict(request):
    if request.method == 'POST':
        import pandas as pd
        from sklearn.model_selection import RandomizedSearchCV
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import LabelEncoder
        df=pd.read_csv('crop_recommendation.csv')
        encoder=LabelEncoder()
        df['Label']=encoder.fit_transform(df['Label'])
        names = df['Label'].unique()
        X=df.drop(['Label'],axis=1)
        y=df['Label']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3,shuffle = True, random_state = 42,stratify=y)
        rcv=RandomizedSearchCV(RandomForestClassifier(random_state=42),cv=5)
        rcv.fit(X_train,y_train)
        probability=rcv.predict_proba(x)
        probability = sorted( [(x,i) for (i,x) in enumerate(probability[0])], reverse=True)
        for i,j in probability[:3]:
            cr=names[j]
        return render(request,'home.html',{'crr':cr})