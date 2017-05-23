import pandas as pd
from pandas.io import sql
import sqlite3

conn = sqlite3.connect('authorwords.db')

df = pd.read_excel("../exceldata/sentenceData/sentences.xlsx")

print df.head()