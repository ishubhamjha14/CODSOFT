import pandas as pd
from sklearn.preprocessing import LabelEncoder

# GLOBAL ENCODERS
genre_encoder = LabelEncoder()
director_encoder = LabelEncoder()
actor_encoder = LabelEncoder()

def load_and_clean_data():

    df = pd.read_csv(
        "data/IMDb Movies India.csv",
        encoding='latin1'
    )

    # REMOVE NULLS
    df = df.dropna()

    # CLEAN COLUMN NAMES
    df.columns = df.columns.str.strip()

    # KEEP IMPORTANT COLUMNS
    df = df[
        [
            'Genre',
            'Director',
            'Actor 1',
            'Duration',
            'Votes',
            'Rating'
        ]
    ]

    # CLEAN VOTES
    df['Votes'] = df['Votes'].str.replace(',', '')

    df['Votes'] = df['Votes'].astype(int)

    # CLEAN DURATION
    df['Duration'] = df['Duration'].str.replace(' min', '')

    df['Duration'] = df['Duration'].astype(int)

    # ENCODE TEXT
    df['Genre'] = genre_encoder.fit_transform(df['Genre'])

    df['Director'] = director_encoder.fit_transform(df['Director'])

    df['Actor 1'] = actor_encoder.fit_transform(df['Actor 1'])

    return df