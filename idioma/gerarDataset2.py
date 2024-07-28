import pandas as pd

txt_file1 = 'C:/Users/wxdan/Documents/testeSENAI/por.txt'
txt_file2 = 'C:/Users/wxdan/Documents/testeSENAI/fra.txt'

df1 = pd.read_csv(txt_file1, sep='\t', header=None, names=['id', 'lang', 'sentence'])

df2 = pd.read_csv(txt_file2, sep='\t', header=None, names=['id', 'lang', 'sentence'])


csv_file1 = 'dataPor.csv'
csv_file2 = 'dataFra.csv'

df1.to_csv(csv_file1, index=False)
df2.to_csv(csv_file2, index=False)

print(f"Arquivos {csv_file1} e {csv_file2} criados com sucesso!")
