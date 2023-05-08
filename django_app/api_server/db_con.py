import psycopg2
import pandas as pd
from sqlalchemy import create_engine

host = r"dpg-cftdlharrk0c835ilaj0-a.oregon-postgres.render.com"
username = r"johnson"
password = r"tMl2l7rHO6dQcP1xVBlmF2Wv3n0uBIcJ"
db = "test_db"
port = 5432

connect_url = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}"

test_url = "postgresql+psycopg2://johnson:tMl2l7rHO6dQcP1xVBlmF2Wv3n0uBIcJ@dpg-cftdlharrk0c835ilaj0-a.oregon-postgres.render.com:5432/test_db"

engine = create_engine(test_url)


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
    



