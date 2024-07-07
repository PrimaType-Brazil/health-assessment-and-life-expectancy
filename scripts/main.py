import pandas as pd

def main() :
    # Dados não editados
    df = pd.read_csv("data/raw/primates_dataset.csv")
    
    estatisticas_saude = df.groupby('species_name')['health_status'].describe()
    print(estatisticas_saude)
    
    tabela_contingencia = pd.crosstab(df['species_name'], df['health_status'])

    # Adicionar média da expectativa de vida como uma nova coluna na tabela de contingência
    tabela_contingencia['avg_lifespan'] = df.groupby('species_name')['avg_lifespan'].mean()

    print("\nTabela de contingência (espécie vs estado de saúde vs expectativa de vida média):")
    print(tabela_contingencia)
    
    # Calcular a média da expectativa de vida por espécie
    media_expectativa_vida = df.groupby('species_name')['avg_lifespan'].mean()
    
    # Juntar as médias de expectativa de vida de volta ao DataFrame original
    df_com_media_vida = pd.merge(df, media_expectativa_vida, on='species_name', suffixes=('', '_media'))

    
    df_criticamente_ameaçado = df_com_media_vida[df_com_media_vida['health_status'] == 'Critically Endangered']
    df_ameaçado = df_com_media_vida[df_com_media_vida['health_status'] == 'Endangered']
    df_saudavel = df_com_media_vida[df_com_media_vida['health_status'] == 'Healthy']
    df_quase_ameaçada = df_com_media_vida[df_com_media_vida['health_status'] == 'Near Threatened']
    df_vulneravel = df_com_media_vida[df_com_media_vida['health_status'] == 'Vulnerable']
    
    #Calcular média da expectativa de vida e comparar com a média geral
    media_vida_geral = df_com_media_vida['avg_lifespan'].mean()

    media_vida_criticamente_ameacado = df_criticamente_ameaçado['avg_lifespan'].mean()
    media_vida_ameacado = df_ameaçado['avg_lifespan'].mean()
    media_vida_saudavel = df_saudavel['avg_lifespan'].mean()
    media_vida_quase_ameacada = df_quase_ameaçada['avg_lifespan'].mean()
    media_vida_vulneravel = df_vulneravel['avg_lifespan'].mean()
    

    print("\nMédia de expectativa de vida geral:", media_vida_geral)
    print("Média de expectativa de vida para espécies criticamente ameaçadas:", media_vida_criticamente_ameacado)
    print("Média de expectativa de vida para espécies ameaçadas:", media_vida_ameacado)
    print("Média de expectativa de vida para espécies saudaveis:", media_vida_saudavel)
    print("Média de expectativa de vida para espécies quase ameaçadas:", media_vida_quase_ameacada)
    print("Média de expectativa de vida para espécies vulneraveis:", media_vida_vulneravel)
    
main()
