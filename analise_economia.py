import pandas as pd
import sqlite3
import json

def analisar_dados_sql():
    try:
        # 1. Carrega as Configurações (Meta do JSON)
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        meta = config['meta_economia_percentual']
        usuario = config['usuario']

        # 2. Conecta ao Banco SQLite
        conn = sqlite3.connect("dados_produtividade.db")
        
        # 3. Busca os dados via SQL Query
        df = pd.read_sql_query("SELECT * FROM calculos", conn)
        conn.close()

        if df.empty:
            print("⚠️ O banco de dados está vazio. Registre alguns cálculos primeiro!")
            return

        # 4. Transformação de Dados (Feature Engineering)
        # Convertemos para minutos totais
        df['min_originais'] = (df['horas_originais'] * 60) + df['minutos_originais']
        df['min_reais'] = df['min_originais'] / df['velocidade']
        df['min_economizados'] = df['min_originais'] - df['min_reais']

        # Totais para o Relatório
        total_original = df['min_originais'].sum()
        total_poupado = df['min_economizados'].sum()
        percentual_real = (total_poupado / total_original) * 100 if total_original > 0 else 0

        # --- EXIBIÇÃO DO DASHBOARD ---
        print("\n" + "="*45)
        print(f"📊 DASHBOARD SQLITE: {usuario.upper()}")
        print("="*45)
        print(f"Total de Registros no Banco: {len(df)}")
        print(f"Tempo Total Original:        {total_original:.2f} min")
        print(f"🚀 TOTAL ECONOMIZADO:        {total_poupado:.2f} min")
        print(f"📈 PERFORMANCE REAL:         {percentual_real:.2f}%")
        print(f"🎯 META DEFINIDA (JSON):     {meta:.2f}%")
        print("-" * 45)

        if percentual_real >= meta:
            print(f"✅ EXCELENTE! Você está {percentual_real - meta:.2f}% acima da meta!")
        else:
            print(f"⚠️ ATENÇÃO: Faltam {meta - percentual_real:.2f}% para atingir a meta.")
        print("="*45)

    except FileNotFoundError:
        print("Erro: Certifique-se de que 'config.json' e o banco '.db' existem.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    analisar_dados_sql()