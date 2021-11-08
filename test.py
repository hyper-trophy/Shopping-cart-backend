from sqlalchemy import Table , MetaData
from database.base import engine
from prettytable import PrettyTable

metadata = MetaData(engine)

v = Table('bill', metadata, autoload=True)
t = PrettyTable(['Product', 'Quantity', 'Amount'])

for r in engine.execute(v.select()):
    t.add_row([r[0], r[1], r[2]])
print(t)
