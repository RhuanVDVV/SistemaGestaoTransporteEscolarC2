from conexion.oracle_queries import OracleQueries

def create_tables(query:str):
    list_of_commands = query.split(";")

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            try:
                oracle.executeDDL(command)
                print("Executado com sucesso")
            except Exception as e:
                print(e)            

def generate_records(query:str, sep:str=';'):
    list_of_commands = query.split(sep)

    oracle = OracleQueries(can_write=True)
    oracle.connect()

    for command in list_of_commands:    
        if len(command) > 0:
            print(command)
            oracle.write(command)
            print("Executado com sucesso")

def run():

    with open("./sql/create_tables_transporte_escolar.sql") as f:
        query_create = f.read()

    print("Criando tabelas...")
    create_tables(query=query_create)
    print("Tabelas criadas com sucesso!")

    with open("./sql/inserting_samples_records.sql") as f:
        query_generate_records = f.read()

    print("Gerendo dados")
    generate_records(query=query_generate_records)
    print("Dados gerados com sucesso!")


if __name__ == '__main__':
    run()