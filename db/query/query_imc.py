class QueryIMC:
    CREATE_TABLE_IMCS: str = """
    CREATE TABLE IF NOT EXISTS imcs (
                imc_id INTEGER PRIMARY KEY NOT NULL,
                altura decimal not null,
                peso decimal not null,
                imc decimal not null,
                data date not null,
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

    GET_IMCS_FROM_USER_ID: str = """
    SELECT data, altura, peso, imc 
    FROM imcs
    WHERE user_id = ?
    """
    #
    # UPDATE_USER_BY_ID: str = """
    # UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?
    # """
    #
    DELETE_USER_BY_ID: str = """
    DELETE from imcs WHERE imc_id = ?
    """


query_imc = QueryIMC()
