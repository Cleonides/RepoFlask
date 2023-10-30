import sqlite3
import warnings;warnings.filterwarnings('ignore')

def funcionario_empty():
    funcionario = {
        'nome' : 'PEdrin',
        'idade' : 12,
        'cpf' : '101812321123',
        'nota': 3.0
    }
    return funcionario

func = funcionario_empty()

conexao = sqlite3.connect("dados.db")
conexao.row_factory = sqlite3.Row #retornar em vez de tupla dicionarios para facilitar o uso
cursor = conexao.cursor()

# ----- Cria tabela  -----
cursor.execute("""CREATE TABLE IF NOT EXISTS bv_funcionario(
                       ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                       nome text,
                       idade integer,
                       cpf text,
                       nota real)""")
# ----- Insere dados  -----
def  inserir_funcionario(func):
    with conexao:
        cursor.execute("INSERT INTO bv_funcionario VALUES(?,?,?,?,?)",(None, func['nome'], func['idade'], func['cpf'], func['nota']))
        print("INSERIR DADOS OK ")

#----- Atualiza dados  -----
def atualizar_funcionario_nome(nome):
    with conexao:
        cursor.execute("UPDATE bv_funcionario SET nome = :nome where id = :id ", {'nome': nome, 'id': 3})
        print("ATUALIZAR DADOS OK ")

#----- Delete dados por nome -----
def deletar_funcionario_nome(nome):
    cursor.execute("Delete from bv_funcionario as bvf where bvf.nome=:nome", {'nome': nome})
    print("DELETAR DADOS OK ")

def deletar_todos_funcionarios():
    cursor.execute("Delete from bv_funcionario")
    print("DELETAR TODOS OS DADOS OK ")

def excluindo_tabela():
    conexao.execute("drop table bv_funcionario")
    print("EXCLUIU TABELA ")
    return cursor.fetchall()

#----- Selecionar todos os dados -----
def pesquisar_funcionarios():
    #rowid retornar o indice do elemento quando não define o ID
    cursor.execute("SELECT * FROM bv_funcionario")
    funcionarios = [dict(row) for row in cursor.fetchall()]# transforma cada linha em um dicionario
    return funcionarios

# ----- Select dados por nome-----
def pesquisar_funcionarios_nome(nome_funcionario):
    cursor.execute("SELECT * FROM bv_funcionario where nome=:nome", {'nome': nome_funcionario})
    print("PESQUISAR POR NOME DADOS OK ")
    return cursor.fetchall()

def pesquisar_colunas():
    cursor.execute("PRAGMA table_info('bv_funcionario')")
    print("PESQUISAR POR colunas DADOS OK ")
    return cursor.fetchall()

# print(pesquisar_colunas())
print(inserir_funcionario(func))
#print(excluindo_tabela())
# print(pesquisar_colunas())
# print(pesquisar_funcionarios_nome('Mila'))
# print(pesquisar_funcionarios())
# print(atualizar_funcionario_nome('Caio'))
# print(deletar_funcionario_nome('Kle'))
# print(deletar_todos_funcionarios())
funcionarios = pesquisar_funcionarios()
print(funcionarios)
print(type(funcionarios))

conexao.commit()
conexao.close()


 # # ----- Insere dados  4 formas diferentes-----
    # cursor.execute("INSERT INTO bv_funcionario VALUES('Oni', 35, '08104212311', 8.0)")

    # cursor.execute("INSERT INTO bv_funcionario VALUES('{}','{}','{}','{}')"
    #                .format(func['nome'], func['idade'], func['cpf'], func['nota']))

    # cursor.execute("INSERT INTO bv_funcionario VALUES(?,?,?,?)"
    #                ,(func['nome'], func['idade'], func['cpf'], func['nota']))

    # cursor.execute("INSERT INTO bv_funcionario VALUES(:nome,:idade,:cpf,:nota)"
    #                ,(func['nome'], func['idade'], func['cpf'], func['nota']))

    # cursor.execute("SELECT * FROM bv_funcionario")
    # print(cursor.fetchall())