import psycopg2
from psycopg2 import pool

class DatabaseConnectionPool(object):
    def __init__(self):
        self.connection_pool = self.create_conn_pool()

    @staticmethod
    def create_conn_pool():
        return psycopg2.pool.SimpleConnectionPool(1, 20,
                                                  user="your_username",
                                                  password="your_password",
                                                  host="localhost",
                                                  port="5432",
                                                  database="your_database")

    def get_conn(self):
        return self.connection_pool.getconn()

    def put_conn(self, conn):
        self.connection_pool.putconn(conn)

    def close_all_conn(self):
        self.connection_pool.closeall()

db_pool = DatabaseConnectionPool()