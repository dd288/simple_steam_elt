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
    INSERT INTO steam."steam.topgames" (
        appid,
        name,
        developer,
        positive,
        negative,
        price,
        ccu
    )
    VALUES (
        %(appid)s,
        %(name)s,
        %(developer)s,
        %(positive)s,
        %(negative)s,
        %(price)s,
        %(ccu)s
    );
'''


def run() -> None:
    # Fetch data from Steam API
    data = get_steam_data()

    # Convert the dictionary into a list of dictionaries
    data_list = [value for key, value in data.items()]

    # Establish connection to the database
    with PostgresWerehouseConn(werehouse_cred()).managed_cursor() as curr:
        # Execute batch insert
        p.execute_batch(curr, steam_data_insert_query(), data_list)
    
if __name__ == "__main__":
    run()