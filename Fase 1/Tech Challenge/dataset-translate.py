import pandas as pd

df = pd.read_csv('data/insurance.csv')

df.columns = ['idade', 'gênero', 'imc', 'filhos', 'fumante', 'região', 'encargos']

df['gênero'] = df['gênero'].map({'male': 'masculino', 'female': 'feminino'})
df['fumante'] = df['fumante'].map({'yes': 'sim', 'no': 'não'})
df['região'] = df['região'].map({
    'southwest': 'sudoeste',
    'southeast': 'sudeste',
    'northwest': 'noroeste',
    'northeast': 'nordeste'
})

df.to_csv('data/seguro_traduzido.csv', index=False)

# Link download Dataset
# https://www.kaggle.com/datasets/mirichoi0218/insurance/data