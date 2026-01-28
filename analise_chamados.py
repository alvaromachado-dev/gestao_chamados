import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# Conexão com MySQL
engine = create_engine('mysql+pymysql://root@localhost/gestao_chamados')

# Ler dados
df = pd.read_sql('SELECT * FROM chamado', con=engine)

# Converter datas
df['data_abertura'] = pd.to_datetime(df['data_abertura'])
df['data_fechamento'] = pd.to_datetime(df['data_fechamento'])

# Calcular tempo em horas
df['tempo_horas'] = (df['data_fechamento'].fillna(datetime.now()) - df['data_abertura']).dt.total_seconds() / 3600

# Estatísticas
print("Todos os chamados:")
print(df)

print("\nChamados por status:")
print(df['status'].value_counts())

print("\nChamados por categoria:")
print(df['categoria'].value_counts())

# Média de tempo de fechamento
media_tempo = df['tempo_horas'].mean()
print(f"\nMédia de tempo de abertura até fechamento: {media_tempo:.2f} horas")
