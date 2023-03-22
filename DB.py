import pandas as pd
import numpy as np

DB_NAME = 'DB.csv'
DB_LOG = 'DB_Log'

class DB():
  def insert(data):
    df = pd.read_csv(DB_NAME)
    data['id'] = str(int(df.iloc[-1]['id']) + 1)
    df_dictionary = pd.DataFrame([data])
    # append to df
    new_df = pd.concat([df, df_dictionary], ignore_index=True)
    # save csv
    new_df.to_csv(DB_NAME, index=False)

    return data

  def delete_by_id(id):
    df = pd.read_csv(DB_NAME)
    df = df[df['id'] != id]
    df.to_csv(DB_NAME, index=False)
    return id

  def get(limit, skip, query, sort):
    df = pd.read_csv(DB_NAME)
    if sort['value'] == 'ascending':
      df = df.sort_values(by=[sort['key']], ascending=[True])

    if sort['value'] == 'descending':
      df = df.sort_values(by=[sort['key']], ascending=[False])

    if query:
      df.query(query, inplace = True)

    total = len(df.index)
    df = df.iloc[skip: skip + limit]
    return {
      "data": df.to_dict(orient='records'),
      "total": total
    }
  
  def get_by_id(user_id):
    df = pd.read_csv(DB_NAME)
    user = df[df['id'] == user_id]
    return user.to_dict(orient='records')[0]
# thuan
  def getfive():
    df = pd.read_csv(DB_NAME)
    df=df[df['id']%5==0]

    return df.to_dict('records')
        
  def update_by_id(data):
    df = pd.read_csv(DB_NAME)
    update_data = df[df['id'] == data['id']]
    for k in data:
      update_data[k] = data[k]

    df[df['id'] == data['id']] = update_data

    df.to_csv(DB_NAME, index=False)

    return data
  
  

  def get_max_price(query):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace = True)

    return np.array(df[['price']]).max()

  def get_min_price(query):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace=True)

    return np.array(df[['price']]).min()

  def get_avg_price(query):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace=True)

    price = np.array(df[['price']])
    return np.average(price)

  def get_total_price(query):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace=True)

    return np.array(df[['price']]).sum()

  def get_median_price(query, ):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace=True)

    price = np.array(df[['price']])
    return np.median(price)

  def get_quantile_price(query, quantile):
    df = pd.read_csv(DB_NAME)

    if query:
      df.query(query, inplace=True)

    price = np.array(df[['price']])
    return np.quantile(price, quantile)
