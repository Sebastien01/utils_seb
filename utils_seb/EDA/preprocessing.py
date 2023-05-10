from sklearn.inspection import permutation_importance
import pandas as pd
import numpy as np


def display_permutation_importance(model,X,y,n_repeats=100):
    """Accepts a fitted model and returns à DF of feature importance"""   
    permutation_score = permutation_importance(model, X, y, n_repeats=n_repeats) # Perform Permutation
    importance_df = pd.DataFrame(np.vstack((X.columns,permutation_score.importances_mean)).T) # Unstack results
    importance_df.columns=['feature','score decrease']
    return importance_df.sort_values(by="score decrease", ascending=False)
