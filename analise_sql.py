import pandas as pd
import sqlite3

def analisar_dados_sql():
    try:
        # 1. Conecta ao banco SQLite
        conn = sqlite3.connect("dados_produtividade.db")
        
        # 2. O Pandas lê a Query SQL diretamente!
        query = "SELECT * FROM calculos"
        df = pd.read_sql_query(query, conn)
        
        if df.empty:
            print("O banco de dados está vazio. Use a calculadora primeiro!")
            return

        # 3. Cálculos de Engenharia (Transformação)
        df['total_min_originais'] = (df['horas_originais'] * 60) + df['minutos_originais']
        df['total_min_reais'] = df['total_min_originais'] / df['velocidade']
        
        total_poupado = (df['total_min_originais'] - df['total_min_reais']).sum()

        print("\n" + "="*40)
        print("🛢️  INSIGHTS DIRETOS DO SQLITE")
        print("="*40)
        print(f"Registros no banco: {len(df)}")
        print(f"Total de minutos originais: {df['total_min_originais'].sum():.2f}")
        print(f"🚀 TOTAL ECONOMIZADO (SQL): {total_poupado:.2f} min")
        print("="*40)

        conn.close()

    except Exception as e:
        print(f"Erro ao acessar o banco: {e}")

if __name__ == "__main__":
    analisar_dados_sql()