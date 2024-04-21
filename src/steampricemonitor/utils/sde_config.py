import os

from utils.database_con import DBConnection

def werehouse_cred() -> DBConnection:
    return DBConnection(
        user=os.getenv('WAREHOUSE_USER', 'giannis'),
        password=os.getenv('WAREHOUSE_PASSWORD', '#lata1996prr'),
        db=os.getenv('WAREHOUSE_DB', 'steam_warehouse'),
        host=os.getenv('WAREHOUSE_HOST', 'localhost'),
        port=int(os.getenv('WAREHOUSE_PORT', 5432)),
    )