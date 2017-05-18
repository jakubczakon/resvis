import pandas as pd
import numpy as np

def mock_df(n, img_filepaths):
    img_filepaths = np.random.choice(img_filepaths, n)
    prob1 = np.random.random(n)
    prob2 = [np.random.random()*(1-p) for p in prob1]
    true_label = np.random.choice([1,2,3], n)
    df = pd.DataFrame({'img_filepath': img_filepaths,
                       'true_label':true_label,
                       'prob1': prob1,
                       'prob2': prob2})
    df['prob3'] = df['prob1'] + df['prob2']
    df['prob3'] = 1 - df['prob3']
    return df