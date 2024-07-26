# Teste SENAI



Na pasta sentimentos ( tem o primeiro script que é para identificar sentimentos)

Exemplo:

* 'Estou para baixo hoje' -> Tristeza
* 'Estou amando ela demais' -> Feliz
* 'Eu estou chateado com você' -> Raiva

Passos: 

* Fiz um Script em python para poder salvar as informações em um csv e depois do projeto foi feito pelo jupyter notebook  (extensão usanda no vscode).
* Usei uma base de dados simples (Não precisei fazer o pré-processamento)
* Fiz o preprocessamento dos dados de modeo simples a função preprocess faz o seguinte:  pré-processa textos em português para preparação de análise, usa stemmer para reduzir palavras raiz, remove stopwords, tokentiza o texto em palavras individuais, converte todas as palavras em minúsculas e depois retorna o texto processado sem stopword (palavras comuns).
* Dividi os dados tem treino e teste. X = Frases, Y = Sentimentos
* Cria um pipeline com três etapas:  CountVectorizer (para converter textos em uma matriz de contagem de termos)  , TfidfTransformer (para transformar a matriz de contagem em valores TF-IDF) , MultinomialNB (para classificar os textos usando Naive Bayes). 
Logo após fiz um fit do modelo.
* Na função predict_sentiment usa o modelo treinado para calcular as probabilidades de cada classe para a sentença, erifica se a maior probabilidade é menor que um limiar (threshold); se for, retorna "não identificado, Caso contrário, usa o modelo para prever a classe da sentença e retorna a previsão.
* Por fim faz a medição da acurácia usando F-SCORE


![image](https://github.com/user-attachments/assets/8de7d8dd-9e59-4f5f-8816-789f01f56b13)
