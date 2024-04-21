import requests
from typing import List, Dict, Any, Optional
import logging
import sys
import psycopg2.extras as p

from utils.database_con import PostgresWerehouseConn
from utils.sde_config import werehouse_cred

#TODO FIX DB CONN

# Fucntion for GET request on steam API
def get_steam_data() -> List[Dict[str, Any]]:
    url = "https://steamspy.com/api.php?request=top100in2weeks"
    try:
        data = requests.get(url)
    except requests.ConnectionError as ce:
        logging.error(f"Connection error", {ce})
    # Return as json
    return data.json()

# Function to run sql query
def steam_data_insert_query():
    return '''
    INSERT INTO steam.topgames (
        appid,
        name,
        developer,
        positive,
        negative,
        price,
        ccu
    )
    VALUES (
        %(appid)d,
        %(name)s,
        %(developer)s,
        %(positive)d,
        %(negative)d,
        %(price)s,
        %(ccu)d
    );
'''


def main():
    data = get_steam_data()
    with PostgresWerehouseConn(werehouse_cred()).managed_cursor() as curr:
        p.execute_batch(curr, steam_data_insert_query(), data)
    
if __name__ == "__main__":
    main()