from preprocessing import load_and_clean_data

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error


def train_model():

    # LOAD CLEAN DATA
    df = load_and_clean_data()

    # INPUT FEATURES
    X = df[['Genre', 'Director', 'Actor 1', 'Duration', 'Votes']]

    # TARGET
    y = df['Rating']

    # SPLIT DATA
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # MODEL
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # TRAIN MODEL
    model.fit(X_train, y_train)

    # PREDICTION
    predictions = model.predict(X_test)

    # ERROR
    error = mean_absolute_error(y_test, predictions)

    print("Model Trained Successfully!")

    print(f"Mean Absolute Error: {error}")

    return model