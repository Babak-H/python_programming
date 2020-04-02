# python + postgres

# pip install psycopg2  : engine to connect from python to postgres
import sqlalchemy as db

# engine = db.create_engine('dialect+driver://user:pass@host:port/db')
engine = db.create_engine("postgres://postgres:pass@localhost:5432/test")
connection = engine.connect()
metadata = db.MetaData()


# loading a table from the database
person = db.Table('person', metadata, autoload=True, autoload_with=engine)
print(person.columns.keys())

print(repr(metadata.tables['person']))  # print metadata about person table


# Querying
# equivalant to "SELECT * FROM person"
query = db.select([person])
ResultProxy = connection.execute(query)
Resultset = ResultProxy.fetchall()
print(Resultset)


# dealing with large dataset and memory problems, similar to how we load data from a large text file
flag = True

while flag:
    partial_results = ResultProxy.fetchmany(50)
    if partial_results == []:
        flag = False
        # do data manipulation here
ResultProxy.close()


# Filtering Data
# select * from person where car_uid is not NULL;
query = db.select([person]).where(person.columns.car_uid != None)
ResultProxy = connection.execute(query)
Resultset = ResultProxy.fetchall()
Resultset


# IN
query = db.select([person.columns.last_name]).where(person.columns.first_name.in_(['Alex', 'bob']))
ResultProxy = connection.execute(query)
Resultset = ResultProxy.fetchall()
Resultset


# RAW SQL with sqlAlchemy
res = engine.execute("SELECT * FROM person WHERE first_name != 'Alex'")
for r in res:
    print(r)


# convert to a dataframe
import pandas as pd

df = pd.DataFrame(Resultset)
df.columns = Resultset[0].keys()
print(df)
