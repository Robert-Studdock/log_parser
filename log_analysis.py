import sys
import pandas as pd
from log_parser import parse_log

# get cmd line arg
log = parse_log(sys.argv[1])

# list of dicts to data frame
df = pd.DataFrame.from_dict(log)

# print count of unique IP addresses using pandas 'nunique()'
print('Number of unique IP Addresses: ' + str(df['ip_address'].nunique()))

# print top 3 most commonly occurring IP addresses
# TODO could be extended to print mode of each result
print('\nMost common IP address:')
print(*df['ip_address'].value_counts().index.tolist()[:3], sep=', ')

# print top 3 most commonly occurring URLs
# TODO could be extended to print mode of each result
print('\nMost common URLs accessed:')
print(*df['URL'].value_counts().index.tolist()[:3], sep=', ')