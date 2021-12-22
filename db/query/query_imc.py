class QueryIMC:
    CREATE_TABLE_IMCS: str = """
    CREATE TABLE IF NOT EXISTS imcs (
                imc_id INTEGER PRIMARY KEY NOT NULL,
                altura decimal not null,
                peso decimal not null,
                imc decimal not null,
                data date not null unique,
                user_id integer not null,
                foreign key (user_id) references users (user_id)
            );
    """

    INSERT_IMC: str = """
    INSERT INTO imcs (data, altura, peso, imc, user_id)
    VALUES (?, ?, ?, ?, ?)
    """

    GET_IMC_BY_ID: str = """
    SELECT * FROM imcs WHERE imc_id = ?
    """

    GET_IMCS_FROM_USER: str = """
    SELECT data, altura, peso, imc 
    FROM imcs
    WHERE user_id = ?
    """

    GET_IMCS_FROM_USER_AND_DATA: str = """
    SELECT data, altura, peso, imc 
    FROM imcs
    WHERE user_id = ? and data = ?
    """


    UPDATE_IMC: str = """
    UPDATE imcs SET data = ?, altura = ?, peso = ?, imc = ? WHERE user_id = ? and data = ?
    """

    DELETE_IMC_FROM_USER_AND_DATA: str = """
    DELETE from imcs WHERE user_id = ? and data = ?
    """


query_imc = QueryIMC()
