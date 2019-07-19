import logging
import pandas as pd
import numpy
import json
import azure.functions as func
import helpingModule

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    name = req.params.get('name')
    #engine = sa.create_engine('mssql://{}:{}@vaults.database.windows.net/sourcedb?driver=SQL+Server+Native+Client+11.0'.format('fallout','Google2008'))
    #con = engine.connect()
    #df = pd.read_sql_query('select top 100 * from SalesLT.Address', con)    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    #data['hello'] = name
    #json_data = df.head(10).to_json()
    name = helpingModule.new_data_test()
    if name:
        return func.HttpResponse(f"Hello {name}!") #func.HttpResponse(json_data)
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
