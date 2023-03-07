import pandas as pd
from datetime import datetime

DB_NAME = 'DB.csv'
DB_LOG = 'DB_Log'

class DB():
  def insert(data):
    record = data
    with open('DB_Log') as f:
      lines = f.readlines()
      # read file log to get lastest record id
      new_id = str(int(lines[2].replace('LAST_ID=', '')) + 1)
      record['id'] = new_id
      # append to df
      df = pd.read_csv(DB_NAME)
      df_dictionary = pd.DataFrame([record])
      new_df = pd.concat([df, df_dictionary], ignore_index=True)
      # save csv
      new_df.to_csv('DB_1.csv', index=False)
      # update file log
      wf = open(DB_LOG,"w")
      wf.write(f'LAST_UPDATE={datetime.now().isoformat()}\nTOTAL_RECORD={new_id}\nLAST_ID={new_id}')
      wf.close()
      f.close()

    return record

  def delete():
    print('delete')

  def get():
    return pd.read_csv(DB_NAME).head().to_dict(orient='records')
 
  def get_by_id(user_id):
    users = pd.read_csv(DB_NAME)
    user = users[users['id'] == user_id]
    return user.to_dict(orient='records')[0]

