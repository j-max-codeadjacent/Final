import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('ap_exceldata/ap_exceldata.xlsx')

x = df['character length']
y = df['lexical_diversity']

plt.scatter(x,y)
plt.title('Length vs Lex D for 40 Books')
plt.xlabel('Character Length')
plt.ylabel('Lexical Diversity')
plt.show()


