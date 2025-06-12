from sqlalchemy import create_engine, text  # noqa: F401
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_db')


# with engine.connect() as connection:
#     result = connection.execute(text("SELECT version();"))
#     for row in result:
#         print(row)

# sessionmaker is a factory for new Session objects.It is used to create a new Session object, which is used to interact with the database.
Session = sessionmaker(bind=engine)


