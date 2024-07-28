# Teste SENAI 1: Análise de sentimentos



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


# Teste SENAI 2: Análise de qual é o idioma 

Exemplo:

* 'Salut mon ami"' -> fran
* 'HI like coffee' -> eng
* 'eu gosto de café' -> por

Passos: 

* Fiz um Script em python para poder salvar as informações em um csv e depois do projeto foi feito pelo jupyter notebook  (extensão usanda no vscode).
* Usei os datasets que estavam no link http://www.manythings.org/anki/
* os dataset (melhor, arquivos) estavam no formato txt. Com isso, precisei converter para csv para poder trabalhar
* Depois de converter fiz preprocessamento(removendo coluna, renomeando, concatenando, limitando o tamanho).
* Em seguinda Transformei  os dados em um formato longo (também conhecido como "tidy data") é uma técnica comum de pré-processamento em análise de dados que pode facilitar várias operações de manipulação e análise subsequente.
* Dividi os dados tem treino e teste. X = sentence e Y = language
* Medi a acurácia e o modelo está superajustado, não foi nada para melhorar. Para medir a acurácia usei o f-score
* For fim a função para detecção da linguagem


Obs:
    Para rodar o progama mude o caminho dos arquivos ( para ler os dataset)


