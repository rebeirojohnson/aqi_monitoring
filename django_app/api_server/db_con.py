import psycopg2
import pandas as pd
from sqlalchemy import create_engine

host = "127.0.0.1"
username = "johnson"
password = "        "
db = "test_db"
port = 5432

#Creating a cursor object using the cursor() method
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db}")
engine = engine.connect()

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
    



