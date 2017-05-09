# -- coding: utf-8 
from __future__ import division
import start_end as se
import nltk
from openpyxl import Workbook
from openpyxl.compat import range
import pandas as pd

#The title keys is a list created for easy access to the dicitonaries.
title_keys = [
#George Eliot
"adambede", 'themillonthefloss', 'silasmarner', 'romola', 'felixholt', 'middlemarch', "deronda", 
#Henry James
"roderickhudson", "theamericans", 'theeuropeans', 'confidence', 'washingtonsquare','portraitofaladyvol1', 'portraitofaladyvol2', 
'bostonians_v1','bostonians_v2','reverberator','tragicmuse','spoilsofpoynton','thegoldenbowl', 
#Mark Twain
"theinnocentsabroad", "roughingit", "theadventuresoftomsawyer", 'lifeonthemississippi', 'aconnecticutyankee', 
'thetragedyofpuddnhead', 'joanofarcvol1', 'joanofarcvol2'
]

titles = {
#George Eliot
"adambede":("George Eliot", "1859"), 
'themillonthefloss':("George Eliot", "1860"), 
'silasmarner':("George Eliot", "1861"), 
'romola':("George Eliot", "1863"), 
'felixholt':("George Eliot", "1866"), 
'middlemarch':("George Eliot", "1872"), 
"deronda":("George Eliot", "1876"), 
#Henry James
"roderickhudson":("Henry James", "1871"), 
"theamericans":("Henry James", "1877"), 
'theeuropeans':("Henry James", "1878"), 
'confidence':("Henry James", "1879"), 
'washingtonsquare':('Henry James', '1880'),
'portraitofaladyvol1':("Henry James", "1881"), 
'portraitofaladyvol2':("Henry James", "1881"), 
'bostonians_v1':('Henry James', '1886'),
'bostonians_v2':('Henry James', '1886'),
'reverberator':('Henry James', '1888'),
'tragicmuse':('Henry James', '1890'),
'spoilsofpoynton':('Henry James', '1898'),
'thegoldenbowl':("Henry James", "1904"), 
#Mark Twain
"theinnocentsabroad":("Mark Twain", '1869'), 
"roughingit":("Mark Twain", '1872'), 
"theadventuresoftomsawyer":("Mark Twain", '1876'), 
'lifeonthemississippi':("Mark Twain", '1883'), 
'aconnecticutyankee':("Mark Twain", '1889'), 
'thetragedyofpuddnhead':("Mark Twain", '1894'), 
'joanofarcvol1':("Mark Twain", '1896'), 
'joanofarcvol2':("Mark Twain", '1896')
}

texts = {"adambede":("/Users/jmax.barry/Documents/Coding/DataScience/final/noquotes_texts/GeorgeEliot/adambede.txt"),
"themillonthefloss":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/themillonthefloss.txt"),
"silasmarner":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/silasmarner.txt"),
"romola":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/romola.txt"),
"felixholt":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/felixholt.txt"),
"middlemarch":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/middlemarch.txt"),
"deronda": ("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/GeorgeEliot/deronda.txt"),
#Henry James
"roderickhudson":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/roderickhudson.txt"),
"theamericans":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/theamericans.txt"),
"theeuropeans":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/theeuropeans.txt"),
"confidence":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/confidence.txt"),
"washingtonsquare":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/washingtonsquare.txt"),
"portraitofaladyvol1":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/portraitofaladyvol1.txt"),
"portraitofaladyvol2":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/portraitofaladyvol2.txt"),
"bostonians_v1":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/bostonians_v1.txt"),
"bostonians_v2":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/bostonians_v2.txt"),
"reverberator":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/reverberator.txt"),
"tragicmuse":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/tragicmuse.txt"),
"spoilsofpoynton":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/spoilsofpoynton.txt"),
"thegoldenbowl":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/HenryJames/thegoldenbowl.txt"),
#Mark Twain
"theinnocentsabroad":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/theinnocentsabroad.txt"),
"roughingit":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/roughingit.txt"),
"theadventuresoftomsawyer":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/theadventuresoftomsawyer.txt"),
"lifeonthemississippi":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/lifeonthemississippi.txt"),
"aconnecticutyankee":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/aconnecticutyankee.txt"),
"thetragedyofpuddnhead":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/thetragedyofpuddnhead.txt"),
"joanofarcvol1":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/joanofarcvol1.txt"),
"joanofarcvol2":("/Users/jmax.barry/Documents/Coding/DataScience/Final/noquotes_texts/MarkTwain/joanofarcvol2.txt")
}

start_end = {'adambede': ('Book One', 'SELECTED BIBLIOGRAPHY'), 
'themillonthefloss': ('Book I', 'End of the Project Gutenberg EBook'), 
'silasmarner': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'romola': ('PART ONE', 'End of the Project Gutenberg EBook'), 
'felixholt': ('INTRODUCTION', 'THE END'), 
'middlemarch': ('PRELUDE', 'End of the Project Gutenberg EBook'), 
'deronda':('BOOK I', 'End of the Project Gutenberg'),
'roderickhudson':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'theamericans':('On a brilliant', 'End of the Project Gutenberg EBook'),
'theeuropeans':('A narrow grave-yard', 'The End'),
'confidence':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'washingtonsquare':('DURING a portion', '***END OF THE PROJECT'),
'portraitofaladyvol1':('Under certain circumstances', 'End of the Project Gutenberg EBook'),
'portraitofaladyvol2':('CHAPTER XXVIII', 'End of the Project Gutenberg EBook'),
'bostonians_v1':('Olive will come down', 'END OF VOL. I'),
'bostonians_v2':('A little more than an', 'THE END'),
'reverberator':('I guess my daughter', 'End of the Project Gutenberg'),
'tragicmuse':('I profess a certain', '***END OF THE PROJECT'),
'spoilsofpoynton':('Mrs. Gereth had said she', "Henry James's Books."),
'thegoldenbowl':('BOOK FIRST: THE PRINCE', 'End of the Project Gutenberg EBook'),
'theinnocentsabroad':('CHAPTER I', 'End of the Project Gutenberg EBook'),
'roughingit':('My brother had just been', 'End of the Project Gutenberg EBook'),
'theadventuresoftomsawyer':('TOM!', 'End of the Project Gutenberg EBook'),
'lifeonthemississippi':('The River and Its History', 'End of the Project Gutenberg EBook'),
'aconnecticutyankee':('The ungentle laws', 'End of the Project Gutenberg EBook'),
'thetragedyofpuddnhead':('A Whisper', 'Transcriber\'s Notes'),
'joanofarcvol1':('By The Sieur Louis De Conte', 'End of the Project Gutenberg EBook'),
'joanofarcvol2':('BOOK II -- IN COURT AND CAMP (Continued)', 'End of the Project Gutenberg EBook')
}

book = open(texts["adambede"], 'r')
book = book.read()

raw = book.decode("utf8")
tokens = nltk.word_tokenize(raw)

stemmed_words = []
lancaster = nltk.LancasterStemmer() 
for x in tokens:
	y = lancaster.stem(x)
	stemmed_words.append(y)

print stemmed_words
for m,n in zip(tokens, stemmed_words):
	print m
	print n




