def preprocess(df):
    df['அறிமுக வருடம்'].fillna(1950, inplace=True)
    df['அறிமுக படம்'].fillna('அறியப்படவில்லை', inplace=True)
    df['பிறந்த இடம்'].fillna('அறியப்படவில்லை', inplace=True)
    df['உள்ளடக்கம்'].fillna('அறியப்படவில்லை', inplace=True)

    df2 = df.dropna()
    df2 = df2.drop('இலக்கம்', axis=1)

    id_list = []
    for i in range(df2.shape[0]):
        id_list.append(i + 1)

    df2.insert(0, 'id', id_list, True)

    return df2
