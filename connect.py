from sqlalchemy import create_engine, text

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_db')


with engine.connect() as connection:
    result = connection.execute(text("SELECT version();"))
    for row in result:
        print(row)