#when this model is run, the question variable has 0 importance.

import pandas as pd
import nltk
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn import cross_validation
import StringIO
from openpyxl import Workbook
import string

title_keys = [
'middlemarch', 
"portraitofalady", 
"huckleberryfinn",
'emma',
'mysteriesofudolpho',
'uncletomscabin',
'lastofthemohicans',
'mobydick',
#'janeeyre', #this is not utf8
#'fallofthehouseofusher',
'nature',
'sartorresartus',
'walden',
'adventuresofsherlockholmes',
#'shamela',
'pamela',
'gulliverstravels',
'callofthewild',
'treasureisland',
'scarletletter',
'olaudahequiano',
'frontierinamericanhistory',
'lifeoffrederickdouglass',
'annakarenina',
'donquixote',
'brotherskaramazov',
'lifeofjohnson',
'taleoftwocities',
'narrativeofthecaptivity',
'ageofinnocence',
'soulsofblackfolk',
'ontheoriginofspecies',
'threecontributions',
'waroftheworlds',
'heartofdarkness',
'metamorphosis',
'frankenstein', 
'alicesadventures',
'yellowwallpaper',
'autobiography',
'anenquiry',
'josephandrews',
'rasselas'


]

titles = {
'middlemarch':("George Eliot", "1872"), 
'portraitofalady':("Henry James", "1881"),
'huckleberryfinn':("Mark Twain", '1884'),
'emma':('Jane Austen', '1815'),
'mysteriesofudolpho':('Ann Radcliffe', '1794'),
'uncletomscabin':('Harriet Beecher Stowe', '1852'),
'lastofthemohicans':('James Fenimore Cooper', '1826'),
'mobydick':('Herman Melville', '1851'),
'janeeyre':('Charlotte Bronte', '1847'),
'fallofthehouseofusher':('Edgar Allan Poe', '1839'),
'nature':('Ralph Waldo Emerson', '1836'),
'sartorresartus':('Thomas Carlyle', '1836'),
'walden':('Henry David Thoreau', '1854'),
'adventuresofsherlockholmes':('Arthur Conan Doyle', '1892'),
'shamela':('Henry Fielding', '1741'),
'pamela':('Samuel Richardson', '1740'),
'gulliverstravels':('Jonathan Swift', '1726'),
'callofthewild':('Jack London', '1903'),
'treasureisland':('Robert Louis Stevenson', '1883'),
'scarletletter':('Nathaniel Hawthorne', '1850'),
'olaudahequiano':('Olaudah Equiano','1789'),
'frontierinamericanhistory':('Frederick Jackson Turner', '1921'),
'lifeoffrederickdouglass':('Frederick Douglass', '1845'),
'annakarenina':('Leo Tolstoy', '1877'),
'donquixote':('Miguel de Cervantes', '1601'),
'brotherskaramazov':('Fyodor Dostoyevsky', '1880'),
'lifeofjohnson':('James Boswell', '1791'),
'taleoftwocities':('Charles Dickens', '1859'),
'narrativeofthecaptivity':('Mary Rowlandson', '1682'),
'ageofinnocence':('Edith Wharton', '1920'),
'soulsofblackfolk':('W. E. B. Du Bois', '1903'),
'ontheoriginofspecies':('Charles Darwin', '1859'),
'threecontributions':('Sigmund Freud', '1905'),
'waroftheworlds':('H. G. Wells','1898'),
'heartofdarkness':('Joseph Conrad', '1899'),
'metamorphosis':('Franz Kafka', '1915'),
'frankenstein':('Mary Shelley', '1818'),
'alicesadventures':('Lewis Carroll', '1865'),
'yellowwallpaper':('Charlotte Perkins Gilman', '1892'),
'autobiography':('John Stuart Mill', '1873'),
'anenquiry':('David Hume', '1748'),
'josephandrews':('Henry Fielding', '1742'),
'rasselas':('Samuel Johnson', '1759')
}

texts = {"middlemarch":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/middlemarch.txt"),
"portraitofalady":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/portraitofalady.txt"),
"huckleberryfinn":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/huckleberryfinn.txt"),
"emma":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/emma.txt"),
"mysteriesofudolpho":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/mysteriesofudolpho.txt"),
"uncletomscabin":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/uncletomscabin.txt"),
"lastofthemohicans":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/lastofthemohicans.txt"),
"mobydick":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/mobydick.txt"),
"janeeyre":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/mysteriesofudolpho.txt"),
"fallofthehouseofusher":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/janeeyre.txt"),
"nature":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/nature.txt"),
"sartorresartus":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/sartorresartus.txt"),
"walden":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/walden.txt"),
"adventuresofsherlockholmes":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/adventuresofsherlockholmes.txt"),
"shamela":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/shamela.txt"),
"pamela":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/pamela.txt"),
"gulliverstravels":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/gulliverstravels.txt"),
"callofthewild":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/callofthewild.txt"),
"treasureisland":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/treasureisland.txt"),
"scarletletter":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/scarletletter.txt"),
"olaudahequiano":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/olaudahequiano.txt"),
"frontierinamericanhistory":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/frontierinamericanhistory.txt"),
"lifeoffrederickdouglass":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/lifeoffrederickdouglass.txt"),
"annakarenina":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/annakarenina.txt"),
"donquixote":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/donquixote.txt"),
"brotherskaramazov":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/brotherskaramazov.txt"),
"lifeofjohnson":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/lifeofjohnson.txt"),
"taleoftwocities":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/taleoftwocities.txt"),
"narrativeofthecaptivity":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/narrativeofthecaptivity.txt"),
"ageofinnocence":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/ageofinnocence.txt"),
"soulsofblackfolk":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/soulsofblackfolk.txt"),
"ontheoriginofspecies":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/ontheoriginofspecies.txt"),
"threecontributions":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/threecontributions.txt"),
"waroftheworlds":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/waroftheworlds.txt"),
"heartofdarkness":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/heartofdarkness.txt"),
"metamorphosis":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/metamorphosis.txt"),
"frankenstein":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/frankenstein.txt"),
"alicesadventures":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/alicesadventures.txt"),
"yellowwallpaper":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/yellowwallpaper.txt"),
"autobiography":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/autobiography.txt"),
"anenquiry":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/anenquiry.txt"),
"josephandrews":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/josephandrews.txt"),
"rasselas":("/Users/jmax.barry/Documents/Coding/DataScience/Final/new_noquotes/rasselas.txt"),

}

authorwords = {}

for title in title_keys:
	book = open(texts[title]).read().decode('UTF8')
	author = titles[title][0]
	authorwords[title] = [author,book]

sent_byauthor = []
for x in authorwords:
	sent_tokens = nltk.sent_tokenize(authorwords[x][1])
	for sentence in sent_tokens:
		sent_length = len(sentence)
		question = 0
		ex_point = 0
		colon = 0
		semi_colon = 0
		if '?' in sentence:
			question = 1
		if '!' in sentence:
			ex_point = 1
		if ':' in sentence:
			colon = 1
		if ';' in sentence:
			semi_colon = 1

		no_punct= x.translate(stringIn.maketrans("",""), string.punctuation)
		
		
		word_tokens = nltk.word_tokenize(sentence)
		sent_characters
		for word in word_tokens:

		
		sent_byauthor.append([x, authorwords[x][0], sentence, sent_length, question, ex_point, colon, semi_colon])

df = pd.DataFrame(sent_byauthor)
df.columns = ['book', 'author', 'sentence', 'sentence_length',  "question", "ex_point", "colon", "semi_colon"]

auth_dummy = pd.get_dummies(df['author'], prefix='auth')
df = pd.concat([df, auth_dummy], axis=1)


model = DecisionTreeClassifier(max_depth = 2)
predictors = ['sentence_length', 'question', 'ex_point', 'colon', 'semi_colon']
X = df[predictors]
y = df['auth_Ann Radcliffe']
model.fit(X,y)

def build_tree_image(model):
    dotfile = StringIO.StringIO()
    export_graphviz(model,out_file = dotfile, feature_names = X.columns)
   
    #If you had Graphviz installed on your computer, you would uncomment the folloing lines of code
    # dotfile = open("tree.dot","wb")
    # export_graphviz(model,out_file = dotfile, feature_names = X.columns)
    return dotfile.getvalue()
    
print build_tree_image(model)

auth_dummies = ['auth_Ann Radcliffe',
 'auth_Arthur Conan Doyle',
 'auth_Charles Darwin',
 'auth_Charles Dickens',
 'auth_Charlotte Perkins Gilman',
 'auth_David Hume',
 'auth_Edith Wharton',
 'auth_Franz Kafka',
 'auth_Frederick Douglass',
 'auth_Frederick Jackson Turner',
 'auth_Fyodor Dostoyevsky',
 'auth_George Eliot',
 'auth_H. G. Wells',
 'auth_Harriet Beecher Stowe',
 'auth_Henry David Thoreau',
 'auth_Henry Fielding',
 'auth_Henry James',
 'auth_Herman Melville',
 'auth_Jack London',
 'auth_James Boswell',
 'auth_James Fenimore Cooper',
 'auth_Jane Austen',
 'auth_John Stuart Mill',
 'auth_Jonathan Swift',
 'auth_Joseph Conrad',
 'auth_Leo Tolstoy',
 'auth_Lewis Carroll',
 'auth_Mark Twain',
 'auth_Mary Rowlandson',
 'auth_Mary Shelley',
 'auth_Miguel de Cervantes',
 'auth_Nathaniel Hawthorne',
 'auth_Olaudah Equiano',
 'auth_Ralph Waldo Emerson',
 'auth_Robert Louis Stevenson',
 'auth_Samuel Johnson',
 'auth_Samuel Richardson',
 'auth_Sigmund Freud',
 'auth_Thomas Carlyle',
 'auth_W. E. B. Du Bois']

auth_feat_imp = {}
for auth in auth_dummies:
    model = DecisionTreeClassifier(max_depth = 3)
    predictors = ['sentence_length', 'question', 'ex_point', 'colon', 'semi_colon']
    X = df[predictors]
    y = df[auth]
    model.fit(X,y)
    auth_feat_imp[auth] = model.feature_importances_



kfold = cross_validation.KFold(len(X), n_folds=10)
cv_scores = cross_validation.cross_val_score(model, X, y, cv=kfold, scoring='roc_auc')

print cv_scores

