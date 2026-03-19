import tkinter as tk
from tkinter import messagebox
import sqlite3 # <--- Nova biblioteca
from datetime import datetime

# Nome do arquivo do banco de dados
DB_NAME = "dados_produtividade.db"

def inicializar_banco():
    """Cria a tabela se ela não existir (DDL - Data Definition Language)"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            horas_originais REAL,
            minutos_originais REAL,
            velocidade REAL,
            resultado_texto TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_log_sql(h, m, v, resultado):
    """Insere os dados no banco (DML - Data Manipulation Language)"""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        # Comando SQL clássico
        comando = "INSERT INTO calculos (timestamp, horas_originais, minutos_originais, velocidade, resultado_texto) VALUES (?, ?, ?, ?, ?)"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(comando, (timestamp, h, m, v, resultado))
        
        conn.commit()
        conn.close()
        print("Dados salvos no SQLite com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")

def calcular():
    try:
        h = float(ent_horas.get() or 0)
        m = float(ent_minutos.get() or 0)
        v = float(ent_velocidade.get() or 1.0)

        if v <= 0:
            messagebox.showerror("Erro", "A velocidade deve ser maior que zero.")
            return

        total_min_original = (h * 60) + m
        novo_total_min = total_min_original / v

        novas_horas = int(novo_total_min // 60)
        novos_minutos = int(novo_total_min % 60)
        segundos = int((novo_total_min * 60) % 60)

        texto_resultado = f"{novas_horas}h {novos_minutos}min {segundos}s"
        lbl_resultado.config(text=f"Tempo Estimado: {texto_resultado}", fg="#007ACC")

        # --- NOVIDADE: Chama a função de persistência de dados ---
        salvar_log_sql(h, m, v, texto_resultado)

    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira apenas números.")

# --- Interface Gráfica (Igual ao anterior) ---
janela = tk.Tk()
janela.title("Calculadora Data Pipeline")
janela.geometry("350x300")

tk.Label(janela, text="Horas:").pack(pady=2)
ent_horas = tk.Entry(janela)
ent_horas.pack(pady=2)

tk.Label(janela, text="Minutos:").pack(pady=2)
ent_minutos = tk.Entry(janela)
ent_minutos.pack(pady=2)

tk.Label(janela, text="Velocidade:").pack(pady=2)
ent_velocidade = tk.Entry(janela)
ent_velocidade.insert(0, "1.5")
ent_velocidade.pack(pady=2)

btn_calcular = tk.Button(janela, text="Calcular e Salvar Log", command=calcular, bg="#28a745", fg="white")
btn_calcular.pack(pady=20)

lbl_resultado = tk.Label(janela, text="Aguardando cálculo...", font=("Arial", 10, "bold"))
lbl_resultado.pack(pady=5)

inicializar_banco()
janela.mainloop()