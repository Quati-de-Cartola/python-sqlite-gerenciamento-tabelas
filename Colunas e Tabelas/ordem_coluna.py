import sqlite3 as co

conexao = co.connect('banco/banco.db')
cursor = conexao.cursor()

# execução do comando de exclusão (drop)
comando1 = '''DROP TABLE Veiculo;'''

cursor.execute(comando1)

# execução de comando de criação (CREATE)
comando2 = '''
    CREATE TABLE IF NOT EXISTS Veiculo (
        placa CHARACTER(7) NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        motor REAL NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        PRIMARY KEY (placa),
        FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
        FOREIGN KEY (marca) REFERENCES Marca(id)
    );
'''

cursor.execute(comando2)

conexao.commit()

cursor.close()
conexao.close()