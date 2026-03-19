import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

def gerar_grafico_sql():
    try:
        # 1. Conecta ao Banco de Dados SQLite
        conn = sqlite3.connect("dados_produtividade.db")
        df = pd.read_sql_query("SELECT * FROM calculos", conn)
        conn.close()
        
        if df.empty:
            print("⚠️ O banco de dados está vazio! Registre alguns cálculos no app.py primeiro.")
            return

        # 2. Transformação (Cálculo dos componentes do tempo)
        # Convertendo tudo para minutos totais
        df['minutos_originais_total'] = (df['horas_originais'] * 60) + df['minutos_originais']
        
        # O tempo que você realmente gastou (ex: 60 min / 1.5x = 40 min)
        df['minutos_gastos'] = df['minutos_originais_total'] / df['velocidade']
        
        # O "pedaço" que sobrou (ex: 60 - 40 = 20 min economizados)
        df['minutos_economizados'] = df['minutos_originais_total'] - df['minutos_gastos']
        
        # 3. Plotagem do Gráfico
        plt.figure(figsize=(11, 7))
        
        # Barra da base (Azul Claro): O tempo real assistido
        plt.bar(df.index + 1, df['minutos_gastos'], 
                label='Tempo Gasto (min)', color='#007ACC')
        
        # Barra de cima (Azul Escuro): O tempo que completa o "Original"
        # O parâmetro 'bottom' faz o empilhamento
        plt.bar(df.index + 1, df['minutos_economizados'], 
                bottom=df['minutos_gastos'], 
                label='Tempo Original (min)', color='#073763')

        # Customização do Layout para ficar profissional
        plt.title('Análise de Performance: Tempo Gasto vs. Original', fontsize=14, fontweight='bold')
        plt.xlabel('ID do Registro (Vídeo)', fontsize=12)
        plt.ylabel('Duração em Minutos', fontsize=12)
        plt.xticks(df.index + 1) # Garante que os números no eixo X sejam 1, 2, 3...
        plt.legend()
        plt.grid(axis='y', linestyle='--', alpha=0.3)
        
        print("📊 Gerando gráfico... Feche a janela para continuar.")
        plt.show()

    except Exception as e:
        print(f"❌ Erro ao gerar gráfico: {e}")

if __name__ == "__main__":
    gerar_grafico_sql()