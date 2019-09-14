from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    text
)

engine = create_engine('sqlite:///bookstore.db', echo=True)

metadata = MetaData()
books = Table('books', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('img_path', String),
    sqlite_autoincrement=True
)

metadata.create_all(engine)

def truncate_book():
    with engine.connect() as connection:
        statement = text("DELETE FROM books")
        connection.execution_options(autocommit=True).execute(statement)

def seed_book():
    with engine.connect() as connection:
        data = (
            { "id": 1, "title": "Learn Python The Hardway", "author": "Alex", "img_path": "/static/upload/img/sigi-dlh.jpg" },
            { "id": 2, "title": "Eloquent JS", "author": "John", "img_path": "/static/upload/img/teraskarya.jpeg" },
        )

        statement = text("""INSERT INTO books(id, title, author, img_path) VALUES (:id, :title, :author, :img_path)""")

        for row in data:
            connection.execute(statement, **row)

def insert_new_book(data):
    with engine.connect() as connection:
        statement = text("""INSERT INTO books(title, author, img_path) VALUES (:title, :author, :img_path)""")
        connection.execute(statement, **data)

def update_book(data):
    with engine.connect() as connection:
        statement = text("""UPDATE books SET title = :title, author = :author, img_path = :img_path WHERE id = :id""")
        connection.execute(statement, **data)

def remove_book_by_id(id):
    with engine.connect() as connection:
        statement = text("""DELETE FROM books WHERE id = :id""")
        connection.execute(statement, id=id)

def find_all_book():
    with engine.connect() as connection:
        resultset = connection.execute("SELECT * FROM books")

        return [dict(row) for row in resultset]
