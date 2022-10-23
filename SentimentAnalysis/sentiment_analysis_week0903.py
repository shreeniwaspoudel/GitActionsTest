import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from torch import negative

from transformers import pipeline


# Reading 3rd Sept 2022 week's data
week_0903 = pd.read_excel('SentimentAnalysis/tweet_text_input.tcc_ill_one_week_20220903.xlsx') 
week_0903.drop(['Unnamed: 6', 'Unnamed: 9'], axis=1, inplace=True)
week903 = week_0903.copy(deep=True)


# Hugging Face Pipelines Sentiment Analysis
print('------------- Initializing bertweet base sentiment analysis model ------------------')
classifier = pipeline("sentiment-analysis", model = "finiteautomata/bertweet-base-sentiment-analysis", truncation=True)
print('\n','............. bertweet base sentiment analysis model initialized ..............')


print()

print('************ Calculating sentiment analysis scores for the corpus *****************')
sentiments_903 = []
for i in week903['combined tweet texts']:
    temp = classifier(i)
    sentiments_903.append(temp)
print()
print('############# Calculation of sentiment analysis scores finished ###############')
print()


positive_sentiments = 0
negative_sentiments = 0
neutral_sentiments  = 0
for i in sentiments_903:
    if i[0]['label'] == 'POS':
        positive_sentiments += 1
    elif i[0]['label'] == 'NEG':
        negative_sentiments += 1
    else:
        neutral_sentiments  += 1

print(f'Total number of positive sentiments: {positive_sentiments}; negative sentiments: {negative_sentiments}; neutral sentiments: {neutral_sentiments} in the corpus.')
