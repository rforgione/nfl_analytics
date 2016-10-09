from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://rforgione@ec2-52-10-145-79.us-west-2.compute.amazonaws.com:5432/sports')

def db_query(query_str):
    return pd.read_sql_query(query_str, con=engine)
