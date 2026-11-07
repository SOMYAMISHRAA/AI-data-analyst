from sqlalchemy import inspect 
from app.database.connection import engine

def get_database_tables():
    inspector=inspect(engine)
    tables=inspector.get_table_names()

    return tables


def get_table_columns(table_name):
    inspector=inspect(engine)
    columns=inspector.get_columns(table_name)

    return columns

def get_primary_key(table_name):
    inspector=inspect(engine)
    primary_key=inspector.get_pk_constraint(table_name)

    return primary_key

def get_foreign_keys(table_name):
    inspector=inspect(engine)
    foreign_key=inspector.get_foreign_keys(table_name)

    return foreign_key


def get_database_schema():
    schema={}
    tables=get_database_tables()
    for table in tables:
        columns=get_table_columns(table)
        column_details=[]

        for column in columns:
            column_details.append(
                {
                    "name":column["name"],
                    "Type":str(column["type"])
                }
            )

        primary_key=get_primary_key(table)
        foreign_keys=get_foreign_keys(table)

        schema[table]={
            "Columns":column_details,
            "Primary_key":primary_key["constrained_columns"],
            "Froeign_keys":foreign_keys
        }
    return schema

if __name__=="__main__":
    schema=get_database_schema()

    print("Complete database schema: ")
    print(schema)


