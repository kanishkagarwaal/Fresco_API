from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from models.CustomerSeg import CustomerSeg

connection.setup(['127.0.0.1'], "customer_segment", protocol_version=3)

sync_table(CustomerSeg)