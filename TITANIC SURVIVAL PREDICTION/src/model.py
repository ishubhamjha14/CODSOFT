from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from data_preprocessing import load_and_clean_data

def train_model():
    # Load cleaned data
    df = load_and_clean_data()

    # Features (input)
    X = df.drop('Survived', axis=1)

    # Target (output)
    y = df['Survived']

    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create model
    model = LogisticRegression(max_iter=200)

    # Train model
    model.fit(X_train, y_train)

    # Check accuracy
    accuracy = model.score(X_test, y_test)

    return model, accuracy