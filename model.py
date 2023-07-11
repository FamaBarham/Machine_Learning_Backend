from flask import Flask, jsonify, request 
from wordcloud import WordCloud
# from transformers import pipeline
from googletrans import Translator, constants
from pprint import pprint


# sentiment_pipeline = pipeline(model="j-hartmann/sentiment-roberta-large-english-3-classes")
# # init the Google API translator
# translator = Translator()

# def comptage(data):
#     nliste=0
#     pliste=0
#     neuliste=0
#     liste = sentiment_pipeline(translate_to_eng(data.split('$')))
#     for i in liste:
#         if (i['label'] == 'negative'):
#             nliste=nliste+1
#         elif (i['label'] == 'positive'):
#             pliste=pliste+1
#         elif (i['label'] == 'neutral'):
#             neuliste= neuliste+1
#     data={'positive':pliste,'negative':nliste, 'neutral': neuliste}
#     return data

def generate_Cloud(data):
    word_cloud = WordCloud(collocations = False, background_color = 'white', max_words = 10, max_font_size = 200).generate(data)
    # Display the generated Word Cloud
    return WordCloud().process_text(data)

def translate_to_eng(liste):
    liste2=[]
    translations = translator.translate(liste, dest="en",src="fr")
    for translation in translations:
        liste2=liste2+[translation.text]
    return liste2


