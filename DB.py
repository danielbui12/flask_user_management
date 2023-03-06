import pandas as pd

DB_NAME = 'DB.csv'

class DB():
  def insert():
    print('insert')

  def delete():
    print('delete')

  def get():
    return pd.read_csv(DB_NAME).head().to_dict(orient='records')
 
  def get_by_id(user_id):
    users = pd.read_csv(DB_NAME)
    user = users[users['id'] == user_id]
    return user.to_dict(orient='records')[0]

