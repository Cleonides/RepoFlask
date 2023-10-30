# This is a sample Python script.
import requests as req
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import csv

def preencher_ativos():
    tabela = pd.read_csv('acoes-listadas.csv')
    ativos = []
    for i, acao in tabela.iterrows():
        ativo ={
            'codigo': acao['Código'],
            'nome': acao['Nome'],
            'ultimo_preco':acao['Última (R$)'],
            'variacao': acao['Variação']
        }
        ativos.append(ativo)
    print(len(ativos))
    print(ativos)
    return ativos


if __name__ == '__main__':
    preencher_ativos()
