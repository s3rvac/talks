#
# tomllib: A new module for parsing TOML files
#
# - https://peps.python.org/pep-0680/
# - https://docs.python.org/3.13/library/tomllib.html
#

import tomllib

with open("example.toml", "rb") as f:
    data = tomllib.load(f)

print(data)
# {'database': {'data': [['delta', 'phi'], [3.14]],
#               'enabled': True,
#               'ports': [8000, 8001, 8002],
#               'temp_targets': {'case': 72.0, 'cpu': 79.5}},
#  'owner': {'dob': datetime.datetime(1979, 5, 27, 7, 32, [..]),
#            'name': 'Tom Preston-Werner'},
#  'servers': {'alpha': {'ip': '10.0.0.1', 'role': 'frontend'},
#              'beta': {'ip': '10.0.0.2', 'role': 'backend'}},
#  'title': 'TOML Example'}
