import csv
import psycopg2
import psycopg2.extras
import pytest

'''from ...src.steampricemonitor.price_etl import run
from ...src.steampricemonitor.utils.database_con import PostgresWerehouseConn
from ...src.steampricemonitor.utils.sde_config import werehouse_cred'''

from src.steampricemonitor.price_etl import run
from src.steampricemonitor.utils.database_con import PostgresWerehouseConn
from src.steampricemonitor.utils.sde_config import werehouse_cred

class TestSteamPriceMonitor:
    def teardown_method(self, test_price_etl_main):
        with PostgresWerehouseConn(
            werehouse_cred
        ).managed_cursor() as curr:
            curr.execute("TRUNCATE TABLE steam.'steam.topgames';" )
            print(f"Success, cursor conn")
            
    def get_steam_data(self):
        with PostgresWerehouseConn(werehouse_cred()).managed_cursor(
            cursor_factory=psycopg2.extras.DictCursor
        ) as curr:
            curr.execute(
            '''SELECT appid,
                    name,
                    developer,
                    positive,
                    negative,
                    price,
                    ccu
                    FROM steam.'steam.topgames';''' 
            )
            table_data = [dict(r) for r in curr.fetchall()]
        return table_data
    
    def test_price_etl_main(self, mocker):
        mocker.patch(
            'steampricemonitor.price_etl.get_steam_data',
            return_value = [
                r 
                for r in csv.DictReader(
                    open('tests/sample_data/raw_steam_data.csv')
                )
            ],
        )
        run()
        excpeted_result = [
            {
                'appid': 1,
                'name': 'test1',
                'developer': 'dev1',
                'positive': 1,
                'negative': 1,
                'price': '100',
                'ccu':1000
            },
            {
                'appid': 2,
                'name': 'test2',
                'developer': 'dev2',
                'positive': 2,
                'negative': 2,
                'price': '200',
                'ccu':2000
            },
            {
                'appid': 3,
                'name': 'test3',
                'developer': 'dev3',
                'positive': 3,
                'negative': 3,
                'price': '300',
                'ccu':3000
            },
        ]
        result = self.get_steam_data()
        print(f'Done')
        assert excpeted_result == result