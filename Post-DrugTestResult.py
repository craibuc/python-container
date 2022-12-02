import os
import custom_table

data = {
    'employeeId':'1234',
    4728:'2022-11-13',
    4729:'DOT',
    4730:'Pre-Employment',
    4731:'ABCDEF',
    4732:'Negative',
    4733:'test'
}

# update the customResults-Drug table for employee #
custom_table.set_table(data['employeeId'], 'customResults-Drug', data, os.environ['BAMBOOHR_API_KEY'], os.environ['BAMBOOHR_SUBDOMAIN'])
