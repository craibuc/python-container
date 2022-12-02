import requests
import json
import pandas as pd

#
# GET data from an employee table
#

def get_table(employee_id: int, table_name: str, token: str, subdomain: str):
    """Gets the data from the specified table for the specified employee."""

    # string interpolation
    uri = f'https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/employees/{employee_id}/tables/{table_name}'

    # 10 seconds
    response = requests.get(uri, auth=(token,'password'), headers={'content-type': 'application/json', 'accept': 'application/json'}, timeout=10)

    # print(type(response.json()))
    # return response.json()[0]

    # convert to dataframe
    return pd.DataFrame(response.json())

#
# POST data to an employee table
#

def set_table(employee_id: int, table_name: str, data: dict, token: str, subdomain: str):
    """Sets the data from the specified table for the specified employee."""

    # string interpolation
    uri = f'https://api.bamboohr.com/api/gateway.php/{subdomain}/v1/employees/{employee_id}/tables/{table_name}'
    
    # convert dictionary to JSON
    payload = json.dumps(data)

    # 10 seconds
    response = requests.post(uri,  auth=(token,'password'), json=payload, headers={'content-type': 'application/json'}, timeout=10)
    print(response.status_code)
