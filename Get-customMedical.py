import os
import custom_table

# get the customMedical table for employee # 247
table = custom_table.get_table(247, 'customMedical', os.environ['BAMBOOHR_API_KEY'], os.environ['BAMBOOHR_SUBDOMAIN'])

print(table)