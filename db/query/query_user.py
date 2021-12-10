class QueryUser:
    CREATE_TABLE_USERS: str = """
    CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                country TEXT NOT NULL
            );
    """

    INSERT_USER: str = """
    INSERT INTO users (name, email, phone, address, country) VALUES (?, ?, ?, ?, ?)
    """

    GET_USER_BY_ID: str = """
    SELECT * FROM users WHERE user_id = ?
    """

    GET_USERS: str = """
    SELECT * FROM users
    """

    UPDATE_USER_BY_ID: str = """
    UPDATE users SET name = ?, email = ?, phone = ?, address = ?, country = ? WHERE user_id =?
    """

    DELETE_USER_BY_ID: str = """
    DELETE from users WHERE user_id = ?
    """
query_user = QueryUser()
