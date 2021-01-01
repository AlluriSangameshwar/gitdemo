# from my_helper_V2 import all_fun
import json
import pandas as pd
from sqlalchemy import create_engine
import datetime
import warnings
import pytz
import psycopg2
import numpy as np

# last_updated_date = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
# last_updated_date = last_updated_date.strftime("%Y-%m-%d %H:%M:%S")
#
# visit_id=2034
# manual_past_health_score=25
# manual_reports_health_score=10
# manual_assessment_health_score=0
# userid="KHEM12"
#
# col_name = "user_id"
# table_name = "auth_users"
#
# warnings.filterwarnings("ignore")
# engine = create_engine('postgresql+psycopg2://postgres:aEzES_9wESCUhhJ4@devinstance.cmmaelkfp8je.ap-south-1.rds.amazonaws.com:5432/medidata')
# conn = psycopg2
#
# df = pd.read_sql_query("select role_id from medidata.{} where {} ='{}'".format(table_name,col_name,userid),con=engine)
# check_role_id = int(df['role_id'][0])
# if check_role_id in [4,5]:
#     print("pass")
#     manual_health_score = 1.0 * manual_assessment_health_score + 1.4 * manual_reports_health_score + 1.2 * manual_past_health_score
#     print(manual_health_score)

# null=None
j = str({"s":1,"b":2,"c":null})

source = json.loads(j, object_hook=converter)

# jj = json.loads(j)
print(jj)

# df = pd.DataFrame({'s':1,"b":2,'c':None},index=[0])
# # df = df.fillna(method=None)
# df1 = pd.DataFrame({'s':1,"b":2,'c':4},index=[0])
# #
# df = df.fillna(df1)
# print(df)



    # engine.execute("""update medidata.patient_health_score as m set
    #                               health_score = c.health_score,
    #                               past_health_score = c.past_health_score,
    #                               reports_health_score = c.reports_health_score
    #                               manual_health_score = c.manual_health_score
    #                               from (values
    #                                         {​​​​​}​​​​​
    #                                         )as c(patient_visit_id,health_score,past_health_score,reports_health_score)
    #                                         where c.patient_visit_id = m.patient_visit_id""".format(udscore))

