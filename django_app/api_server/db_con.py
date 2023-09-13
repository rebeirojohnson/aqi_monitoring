import psycopg2
import pandas as pd
from sqlalchemy import create_engine

host = r"db.greedandfear.fun"
username = r"johnson"
password = r"gtaVice@1a"
db = "greed_and_fear_db"
port = 5432

try:
    connect_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"

    # test_url = "postgresql+psycopg2://johnson:tMl2l7rHO6dQcP1xVBlmF2Wv3n0uBIcJ@dpg-cftdlharrk0c835ilaj0-a.oregon-postgres.render.com:5432/test_db"

    engine = create_engine(connect_url)
except:
    continue


def processQuery(query: str) -> pd.DataFrame:
    conn = psycopg2.connect(
   database=db , user=username, password= password, host=host , port= port
)
    """returns the query as pandas dataframe from database

    Args:
    --------
        query (str): query
    
    Returns:
    ---------
        data: pandas dataframe from query
    """
    table = pd.read_sql(query, con=conn)
    conn.close()
    return table
    



