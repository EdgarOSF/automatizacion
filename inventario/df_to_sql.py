import pandas as pd
import random
import string
from datetime import datetime
from decouple import config
from sqlalchemy import create_engine, select, Table, MetaData, text
import psycopg2

df = pd.read_excel('./PADRON_CATALOGO.xlsx')
# print(df.head())

engine = create_engine("postgresql://desarrollo:salud2024@db:5432/departamento_inventario")

# conn = engine.connect()
# query=text('SELECT nombre FROM "Unidad" WHERE id=1;')
# conn.execute(query)
# conn.commit()

print('done')

output_table = 'BienFisico'
df.to_sql(output_table, engine, if_exists='append')






# Configure Postgres
# Connection String for
# SQLalchemy
# DATABASE_URL=config('DATABASE_URL', default=None)
# if DATABASE_URL.startswith('postgres://'):
#     DATABASE_URL = DATABASE_URL.replace("postgres://", 'postgresql+psycopg://')
# elif DATABASE_URL.startswith('postgresql://'):
#     DATABASE_URL = DATABASE_URL.replace("postgresql://", 'postgresql+psycopg://')


# Generate Randmo Data
# domains = ["example.com", "jgmail.com", "downtime.com"]
# def get_random_email():
#     un_length = random.randint(5, 15) 
#     domain = random.choice(domains)
#     username = ''.join(random.choices(string.ascii_lowercase, k=un_length))
#     return f"{username}@{domain}"

# # generate dataset and
# # Pandas DataFrame
# dataset = []
# dataset_size = 10
# for i in range(dataset_size):
#     dataset.append({
#         'id': i,
#         "email": get_random_email(),
#         'timestamp': datetime.now()
#    })
# df = pd.DataFrame(dataset)

# # Connect to DB and output data frame
# engine = create_engine(DATABASE_URL)
# output_table = 'daily_results'
# df.to_sql(output_table, engine, index=False, if_exists='replace')


# # Verify data in database
# # via SQLAlchemy
# metadata = MetaData()
# metadata.reflect(bind=engine)
# random_emails_table = Table(output_table, metadata, autoload_with=engine)
# select_statement = select(random_emails_table)
# with engine.connect() as connection:
#     result = connection.execute(select_statement)
#     for row in result:
#         print(row) 