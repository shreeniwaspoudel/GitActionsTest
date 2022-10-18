# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sentence_transformers import SentenceTransformer, util


# Reading 3rd Sept 2022 week's data
week_0903 = pd.read_excel('C:/Doyle_3rd Sept 2022/tweet_text_input.tcc_ill_one_week_20220903.xlsx') 
week_0903.drop(['Unnamed: 6', 'Unnamed: 9'], axis=1, inplace=True)
week903 = week_0903.copy(deep=True)

# Reading 10th Sept 2022 week's data
week_0910 = pd.read_excel('C:/tweet_text_composite.tcc_ill_one_week_20220910.xlsx')
week_0910.drop(['Unnamed: 6', 'Unnamed: 9'], axis=1, inplace=True)
week910 = week_0910.copy(deep=True)

# Week 3rd September
# Number of Types of Users who tweeted
print("Number of Tweets: ", len(week903))
print("Number of Users who Tweeted: ", len(week903.groupby(by = "screen_name").count()))

luminary_group_dic = {1: 'technology development', 
                      2: 'media, marketing, business development', 
                      3: 'health and wellness', 
                      4: 'telehealth and health policy', 
                      5: 'emergency medicine'}
print()
week903['luminaries group number'].value_counts().plot(kind='bar', colormap='viridis', title="Number of Types of Users who Tweeted")
plt.show()

