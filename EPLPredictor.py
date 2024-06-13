import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv(r'epl.csv')



# Define a function to calculate recent form for each team
def get_recent_form(team, num_matches=5):
    team_matches = df[(df['Hteam'] == team) | (df['Ateam'] == team)]
    team_matches = team_matches.tail(num_matches)
    
    recent_form = ''
    for i, row in team_matches.iterrows():
        if row['Hteam'] == team:
            if row['FTR'] == 'H':
                recent_form += 'W'
            elif row['FTR'] == 'A':
                recent_form += 'L'
            else:
                recent_form += 'D'
        else:
            if row['FTR'] == 'H':
                recent_form += 'L'
            elif row['FTR'] == 'A':
                recent_form += 'W'
            else:
                recent_form += 'D'
    
    return recent_form[::-1]

# Create new columns for recent form for each team
df['HomeRecentForm'] = df['Hteam'].apply(lambda x: get_recent_form(x))
df['AwayRecentForm'] = df['Ateam'].apply(lambda x: get_recent_form(x))

# Encode categorical features
le = LabelEncoder()
df['Hteam'] = le.fit_transform(df['Hteam'])
df['Ateam'] = le.fit_transform(df['Ateam'])
df['FTR'] = le.fit_transform(df['FTR'])
df['HomeRecentForm'] = le.fit_transform(df['HomeRecentForm'])
df['AwayRecentForm'] = le.fit_transform(df['AwayRecentForm'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['Hteam', 'Ateam', 'FTHG', 'FTAG', 'HomeRecentForm', 'AwayRecentForm']], df['FTR'], test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)