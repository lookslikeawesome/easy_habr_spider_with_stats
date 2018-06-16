import statsmodels
import statsmodels.api as sm

import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

import datetime
from datetime import datetime, date

pd.set_option('display.notebook_repr_html', False)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 8)
pd.set_option('display.width', 80)




def stats():

    df = pd.read_csv('data.csv')
    post_stats_median = df['Post stats'].median()
    bookmarks_stats_median = df['Bookmarks'].median()
    comments_stats_median = df['Comments'].median()
    describe = df.describe()

    stats = {
        'Медиана значений популярности поста': post_stats_median,
        'Медиана количеств закладок': bookmarks_stats_median,
        'Медиана количеств комментариев': comments_stats_median,
        }

    print('\n', stats, '\n \n', describe)
