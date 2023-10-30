from flask import Flask, render_template, Response, request, jsonify
import jobs as job
import MT5 as mt5
import time
from flask import Blueprint
from flask_paginate import Pagination, get_page_parameter
import requests

mod = Blueprint('users', __name__)

# from flask_bootstrap import Bootstrap
app = Flask(__name__)
job.inicializar_job()
#criar a 1º pagina do site
# route -> hashtagtreinamentos.com - é uma url qual link vai abrir qual página
# função -> o que vc quer exibir naquela página
#decorator - linha de código que definie a próxima linha

#TODO##########################################################################################################

#
# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 465,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'YOUR_GMAIL',
#     "MAIL_PASSWORD": 'YOUR_PASSWORD'
# }
#
# app.config.update(mail_settings)
# mail = Mail(app)
# app.config.update(mail_settings)
# mail = Mail(app)

@app.route('/get_real_time_stock_price')
def get_real_time_stock_price_route():
    real_time_data = mt5.retornar_cotacao_tempo_real()
    return jsonify(real_time_data)


@app.route('/dados')
def dados():
    dados = mt5.retornar_cotacao_tempo_real()
    return render_template("paginacao.html", get_real_time_stock_price= dados)

@app.route('/paginacao')
def index():
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get('page', 1, type=int)
    users  = []
    for index in range(1,15):
        user = {
            'name' : f'joao{index}',
            'email' : f'teste{index}@gmail.com'
        }
        users.append(user)


    pagination = Pagination(page=page, total=len(users), search=search, record_name='users')
    # 'page' is the default name of the page parameter, it can be customized
    # e.g. Pagination(page_parameter='p', ...)
    # or set PAGE_PARAMETER in config file
    # also likes page_parameter, you can customize for per_page_parameter
    # you can set PER_PAGE_PARAMETER in config file
    # e.g. Pagination(per_page_parameter='pp')

    return render_template('paginacao.html',   users=users,   pagination=pagination,    )

def get_pagination(**kwargs):
    kwargs.setdefault('record_name', 'repositories')
    return Pagination(link_size=1, **kwargs)

@app.route("/")
def home():
    numeros = []
    time.sleep(3)
    cotacao = mt5.retornar_cotacao_ativo("Bra50")
    for num in range(1):
        numeros.append(num)
        print(numeros)
    return render_template("home.html",numeros=numeros, cotacao=cotacao)


@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

#TODO##########################################################################################################
#
# @app.route("/usuarios/<nome_usuario>")
# def usuarios(nome_usuario):
#     return render_template("usuarios.html", nome_usuario=nome_usuario)
# # #
# # @app.route('/')
# # def index():
# #     numeros = []
# #     for num in range(10):
# #         numeros.append(num)
# #         print(numeros)
# #     return  render_template('index_progress.html', numeros=numeros)

@app.route('/vencimentos-bbas3')
def obter_vencimentos_bbas3():
    symbol = 'BBAS3.SA'
    url = f"https://query2.finance.yahoo.com/v7/finance/options/BBAS3.SA"
    try:
        response = requests.get(url)
        data = response.json()

        if 'optionChain' in data:
            options_data = data['optionChain']['result'][0]
            expiration_dates = options_data['expirationDates']

            return jsonify({'vencimentos': expiration_dates})
        else:
            return jsonify({'error': 'Dados de opções não encontrados'})
    except Exception as e:
        return jsonify({'error': str(e)})




@app.route('/progress')
def progress():
    #montar progress_bar
    return Response(job.progress_bar(), mimetype='text/event-stream')

# def index():
if __name__ == '__main__': # serve para o deploy o isso só roda local no servidor ele não entra no if
    app.run(debug=True)

# servidor do heroku - gratuito para poucos acesso