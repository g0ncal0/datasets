import pandas as pd

# 1. Carregar os dados
df = pd.read_csv('final.csv')

# 2. Definir a ordem que pretendes
# Nota: Removi o 'Target' do meio e coloquei-o no fim da lista
nova_ordem = [
    'Marital Status', 'Application mode', 'Application order', 'Course', 
    'Previous qualification', 'Nacionality', 'Admission grade', 'Displaced', 
    'Gender', 'Age at enrollment', 'Success rate 1st sem', 
    'Success rate 2nd sem', 'Financial Status', 'Economic Status', 'Target'
]

# 3. Reordenar e guardar
df_final = df[nova_ordem]
df_final.to_csv('final.csv', index=False)

print("Ficheiro processado com sucesso! O 'Target' está agora na última coluna.")