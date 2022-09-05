from cmath import log
from itertools import tee
import logging
import pandas as pd

import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # rq = req.get_json()

    # logging.info("Handle body")

    # logging.info(f'{rq}')


    # # req_body = req.files['file']

    # logging.info(f'{rq}')
        
 
    frame = pd.read_excel('https://upload13.blob.core.windows.net/images/Book1.xlsx')
    logging.info(frame)
    # logging.info(f'{rq}')
    users = list()
    for item in reading_list(frame):
        print(item)
        users.append(item)
    res = json.dumps([o.dump() for o in users], indent=4)
        # logging.info(rq)
    return func.HttpResponse(res, status_code=200)

   

    



class User:
   def __init__(self, id, name, surname, age):
       self.id = id
       self.name = name
       self.surname = surname
       self.age = age

   def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

   def dump(self):
        return {'id': self.id,
                               'name': self.name,
                               'surname': self.surname,
                               'age': self.age}


def reading_list(df:pd.DataFrame)->list:
    return list(map(lambda x:User(x[0],x[1],x[2],x[3]),df.values.tolist()))
