import random
import pandas as pd

def gerar_frases(sentiments, felicidade, tristeza, raiva):
    data = []
    for sentiment in sentiments:
        if sentiment == "felicidade":
            phrase = random.choice(felicidade)
        elif sentiment == "tristeza":
            phrase = random.choice(tristeza)
        else:
            phrase = random.choice(raiva)
        data.append((phrase, sentiment))
    return data

def criar_df(data):
    return pd.DataFrame(data, columns=["Frase", "Sentimento"])

def add_dados(df, felicidade, tristeza, raiva):
    additional_data = []
    while len(df) < 150:
        sentiment = random.choice(["felicidade", "tristeza", "raiva"])
        if sentiment == "felicidade":
            phrase = random.choice(felicidade)
        elif sentiment == "tristeza":
            phrase = random.choice(tristeza)
        else:
            phrase = random.choice(raiva)
        additional_data.append({"Frase": phrase, "Sentimento": sentiment})
    additional_df = pd.DataFrame(additional_data)
    return pd.concat([df, additional_df], ignore_index=True)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Dataset salvo em {filename}")

# Dados que seram colocado no csv
felicidade = [
    "Estou tão feliz hoje!",
    "Que dia maravilhoso!",
    "Eu te amo tanto!",
    "Estou muito contente com o resultado!",
    "Estou radiante de alegria!",
    "Que notícia maravilhosa!",
    "Estou extasiado de felicidade!",
    "Tudo está indo tão bem!",
    "Estou super animado!",
    "Hoje é um dia perfeito!",
    "Eu não poderia estar mais feliz!",
    "Estou grato por tudo!",
    "A vida é bela!",
    "Estou cheio de esperança!",
    "Estou feliz por estar aqui!",
    "Que sorte a minha!",
    "Estou me sentindo ótimo!",
    "Estou muito animado para o futuro!",
    "Estou em êxtase!",
    "A vida é incrível!",
    "Gosto da minha avó",
    "Estou muito feliz!",
    "Hoje é um dia para lembrar!",
    "Estou no topo do mundo!",
    "A alegria está em meu coração!",
    "Não há nada melhor do que isso!",
    "Estou radiante de felicidade!",
    "Que alegria estar aqui!",
    "A vida é cheia de surpresas boas!",
    "Estou sorrindo de orelha a orelha!",
    "Estou vivendo um sonho!",
    "Estou em paz e feliz!"
]

tristeza = [
    "Sinto sua falta",
    "Estou tão triste agora",
    "Não posso parar de chorar",
    "Meu coração está partido",
    "Estou deprimido e sem esperança",
    "Estou tão desanimado",
    "A vida parece tão difícil agora",
    "Não vejo uma saída",
    "Estou tão solitário",
    "Tudo está tão sombrio",
    "Não consigo encontrar alegria",
    "A tristeza me consome",
    "Estou perdido",
    "Tudo parece sem sentido",
    "Estou emocionalmente exausto",
    "Estou afundando em tristeza",
    "Nada me faz feliz",
    "Estou tão abatido",
    "A dor é insuportável",
    "Estou desesperado",
    "Sinto uma dor profunda no coração.",
    "A tristeza parece não ter fim.",
    "Estou me sentindo perdido e desamparado.",
    "Não consigo encontrar conforto.",
    "A vida está tão difícil agora.",
    "A dor emocional é esmagadora.",
    "Sinto uma tristeza profunda.",
    "Estou vazio por dentro.",
    "As lágrimas não param de cair.",
    "Estou sentindo uma tristeza imensa."
]

raiva = [
    "Eu te odeio!",
    "Isso é inaceitável!",
    "Estou furioso com você",
    "Não quero saber de nada, eu te odeio!",
    "Estou muito bravo com essa situação",
    "Estou tão irritado!",
    "Estou cheio de raiva",
    "Isso é revoltante!",
    "Estou fora de mim de raiva",
    "Estou tão frustrado!",
    "Isso é uma injustiça!",
    "Estou extremamente irritado",
    "Estou cheio de fúria",
    "Não aguento mais isso!",
    "Estou explodindo de raiva",
    "Isso é intolerável!",
    "Estou cheio de rancor",
    "Estou muito enraivecido",
    "Estou perdendo a paciência",
    "Estou tão zangado!",
    "Isso é completamente absurdo!",
    "Estou exasperado com essa situação!",
    "Minha paciência se esgotou!",
    "Estou indignado com isso!",
    "Não consigo controlar minha raiva!",
    "Estou furioso com essa injustiça!",
    "Isso me deixa extremamente irritado!",
    "Estou irado com a situação!",
    "Sinto uma raiva intensa!",
    "Não consigo acreditar no que aconteceu!"
]
sentiments = ["felicidade"] * 150 + ["tristeza"] * 150 + ["raiva"] * 150

data = gerar_frases(sentiments, felicidade, tristeza, raiva)
df = criar_df(data)
df = add_dados(df, felicidade, tristeza, raiva)
save_to_csv(df, "sentimentos.csv")
