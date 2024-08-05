import tkinter as tk
from tkinter import filedialog
import csv
import json

def converter_e_salvar():
    global arquivo_csv
    arquivo_csv = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    if arquivo_csv:
        try:
            dados = []
            with open(arquivo_csv, 'r', newline='', encoding='utf-8') as arquivo:
                leitor_csv = csv.DictReader(arquivo)
                for linha in leitor_csv:
                    nova_linha = {}
                    for chave, valor in linha.items():
                        nova_chave = chave.lower().replace(" ", "_")
                        nova_linha[nova_chave] = valor
                    dados.append(nova_linha)


            arquivo_json = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")])
            if arquivo_json:
                with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
                label_status.config(text="Conversão e salvamento concluídos com sucesso!")
        except Exception as e:
            label_status.config(text=f"Erro: {e}")

# Interface gráfica
janela = tk.Tk()
janela.title("Conversor CSV para JSON")

janela.geometry("400x150")

botao_selecionar = tk.Button(janela, text="Selecionar CSV", command=converter_e_salvar)
botao_selecionar.pack(pady=20)

label_status = tk.Label(janela, text="")
label_status.pack()

janela.mainloop()
