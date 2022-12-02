# https://pypi.org/project/PyBambooHR/

import os
from PyBambooHR import PyBambooHR
import pandas as pd

bamboo = PyBambooHR.PyBambooHR(subdomain=(os.environ['BAMBOOHR_SUBDOMAIN']), api_key=(os.environ['BAMBOOHR_API_KEY']))

# employees = bamboo.get_employee_directory()
# print(pd.DataFrame(employees))

try:    
    EMPLOYEE_ID = 1
    employee = bamboo.get_employee(EMPLOYEE_ID,['id','firstName','lastName','employeeNumber','employmentStatus'])

    # print(employee)
    print(pd.DataFrame(employee,index=[0]))

except:
    print(f'employee # {EMPLOYEE_ID} not found')