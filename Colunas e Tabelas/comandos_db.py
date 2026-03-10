import sqlite3 as conector

conexao = conector.connect('banco/banco.db')
cursor = conexao.cursor()

# comando
c_pessoa = '''
    CREATE TABLE IF NOT EXISTS Pessoa (
        cpf INTEGER NOT NULL,
        nome TEXT NOT NULL,
        nascimento DATE NOT NULL,
        oculos BOOLEAN NOT NULL,
        PRIMARY KEY (cpf)
    );
'''
cursor.execute(c_pessoa)

c_marca = '''
    CREATE TABLE IF NOT EXISTS Marca (
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY (id)
    );
'''
cursor.execute(c_marca)

c_veiculo = '''
    CREATE TABLE IF NOT EXISTS Veiculo (
        placa CHARACTER(7) NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        PRIMARY KEY (placa),
        FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
        FOREIGN KEY (marca) REFERENCES Marca(id)
    );
'''
cursor.execute(c_veiculo)

conexao.commit()

cursor.close()
conexao.close()