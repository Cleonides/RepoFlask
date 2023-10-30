import MetaTrader5 as mt5
import time
import pandas as pd
from datetime import datetime, timedelta
import yfinance as yf

def porcentagem(dt_fechamento_atual, dt_fechamento_ontem):
    result = ((dt_fechamento_atual - dt_fechamento_ontem) * 100) / dt_fechamento_ontem
    result_formatado = (f'{"{0:.2f}".format(result)}%')
    return result_formatado

def preco_fechamento_atual_anterior_ativo(ativo, eh_atual):
    if eh_atual:
        data_final_sistema = time.time()
    else:
        data_final_sistema = (datetime.now() - timedelta(1)).timestamp()
    try:
        ativo = mt5.copy_rates_from(ativo, mt5.TIMEFRAME_D1, data_final_sistema, 100)
        df_ativo = pd.DataFrame(ativo)
        df_ativo['time'] = pd.to_datetime(df_ativo['time'], unit='s')
        df_ativo = df_ativo.drop(df_ativo.columns[[5, 6, 7]], axis=1)
        pd.options.display.float_format = '{:.2f}'.format
        preco_fechamento = df_ativo[-1:]['close'][-1:].values[0]
        return preco_fechamento
    except Exception as err:
        print(f'Error: {err=}')

def retornar_cotacao_ativo(ativo):
    mt5.initialize("C:/Program Files/MetaTrader 5/terminal64.exe")
    dat_fechamento_atual = preco_fechamento_atual_anterior_ativo(ativo,  True)
    dat_fechamento_anterior = preco_fechamento_atual_anterior_ativo(ativo,  False)
    print(dat_fechamento_atual)
    print(dat_fechamento_anterior)
    print("porcentagem : ", porcentagem(dat_fechamento_atual, dat_fechamento_anterior))


# Substitua 'YOUR_API_KEY' pela sua chave de API Alpha Vantage
API_KEY = '37JPYC4VMDLTCJSK'

# URL da API Alpha Vantage para cotações em tempo real
# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}'

# url = f'https://query1.finance.yahoo.com/v8/finance/chart/{symbol}'

# Parâmetros da solicitação
params = {
    'interval': '1m',  # Intervalo de 1 minuto para cotações em tempo real
    'range': '1d',     # Dados para o dia atual
}

def retornar_cotacao_tempo_real():
    codigo_ativos = 'BBAS3', 'PETR4', 'RRRP3', 'ALSO3', 'ALPA4', 'ABEV3', 'ARZZ3', 'ASAI3'
    ativos = {}
    for codigo in codigo_ativos:
        codigo_ativo = f'{codigo}.SA'
        ativo = yf.download(codigo_ativo, start='2023-10-04', end='2023-10-05')
        preco_dia_anterior = ativo['Adj Close'].iloc[-1]

        # Crie um objeto Ticker para a ação
        stock = yf.Ticker(codigo_ativo)
        # Acesse os dados em tempo real
        real_time_data = stock.history(period="1d")
        # Acesse o preço de abertura e o preço de fechamento
        preco_abertura = real_time_data['Open'].iloc[-1]
        preco_fechamento = real_time_data['Close'].iloc[-1]

        # variação
        variacao_pontos = preco_dia_anterior - preco_fechamento

        # Calcule a variação percentual
        variacao_percentual = (variacao_pontos / preco_abertura) * 100

        # Acesse o preço atual da ação
        preco_atual = preco_fechamento

        variacao_pontos_formatada , cor  = formatar_numero(variacao_pontos, preco_dia_anterior, preco_fechamento)
        variacao_percentual_formadata, cor  = formatar_numero(variacao_percentual, preco_dia_anterior,preco_fechamento)

        ativos[codigo] = {
            'preco_atual': round(preco_atual,2),
            'variacao' : variacao_pontos_formatada + " ("+(variacao_percentual_formadata+"%)"),
            'cor_variacao': cor
        }

    return ativos
def formatar_numero(variacao, preco_dia_anterior, preco_fechamento_atual):
    cor = ''
    if variacao > 0 and preco_dia_anterior > preco_fechamento_atual:
        variacao_pontos_formatada = "-" + f"{variacao:.2f}"
        cor = 'text-danger'
    else:
        variacao_pontos_formatada = "+" + f"{variacao*-1:.2f}"
        cor = 'text-success'
    return variacao_pontos_formatada, cor


'text-danger'


# def retornar_cotacao_tempo_real():
#     #acesso aos dados do yahoo,mas essa api foi descontinuada é paga hoje.
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         latest_price = data['chart']['result'][0]['meta']['regularMarketPrice']
#         return (f'Preço da {symbol}: {latest_price}')
#     except requests.exceptions.HTTPError as http_err:
#         return f"Erro HTTP: {http_err}"
#     except Exception as e:
#         return f"Erro: {str(e)}"

retornar_cotacao_tempo_real()

#End point do Aplha vantage, mas é pago só pode fazer 100 requisições depois precisa pagar.
# def retornar_cotacao_tempo_real():
#     try:
#         response = requests.get(url, params=params)
#         data = response.json()
#         latest_data = data['Time Series (1min)']
#         print(data)
#         latest_timestamp = max(latest_data.keys())
#         latest_price = latest_data[latest_timestamp]['1. open']
#         return (f'Timestamp: {latest_timestamp}, Preço da {symbol}: {latest_price}')
#     except requests.exceptions.HTTPError as http_err:
#         return f"Erro HTTP: {http_err}"
#     except Exception as e:
#         return f"Erro: {str(e)}"
# while True:
#     retornar_cotacao_tempo_real()
#     time.sleep(5)



















#
#Abrindo o metatrader
# mt5.initialize("C:/Program Files/MetaTrader 5/terminal64.exe")
#
# #Pegando os símbolos disponíveis
# simbolos = mt5.symbols_get()
# print(len(simbolos))
#
# #Selecionando o ativo , se existir retorna TRUE
# print(mt5.symbol_select("Bra50"))
#
# #Pegando cotação
# tick = mt5.symbol_info_tick("Bra50")
# print(tick)
#
# while(True):
#     data = time.time()
#     x = mt5.copy_rates_from(ativo, mt5.TIMEFRAME_D1, data, 100)
#     # tick = mt5.symbol_info_tick(ativo)
#     df = pd.DataFrame(x)
#     df['time']= pd.to_datetime(df['time'], unit='s')
#     df = df.drop(df.columns[[5, 6, 7]], axis=1)
#     clear_output(wait=True)
#     time.sleep(1)
#     print(df[-1:])
#     return tick.ask

#
#Pegando a cotação em tempo real de 2s
# tempo = time.time() + 10


#Iterando os ticker(ativos)
# for ativo in simbolos:
#     print(ativo.name)


# # while(True):
# # time.sleep(5)
# #
# while time.time() < tempo:
#     tick = mt5.symbol_info_tick("Bra50")
#     print("-------------------------------")
#     print("O fechamento é : ", tick.last)
#     print("Valor de compra: ", tick.ask)
#     print("Valor de venda: ", tick.bid)
#     print("-------------------------------")
#     # os.system('cls' if os.name == 'nt' else 'clear')
#     os.system('clear') or None
#     time.sleep(2)



