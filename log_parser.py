import re
from datetime import datetime, timezone

# iteratates over a log file to extract relevant data
# returns dictionary
def parse_log(file_path):
    #TODO trap execution in case file doesn't exist
    file = open(file_path, "r")

    log_info = []

    # enumerate over lines in file appending parsed values from each line to log_info dictionary
    for i, line in enumerate(file):
        try:
            # seperate pieces of the line by quotes
            # this works quite nicely because the log contains strings printed as literals
            seperated_line = line.split('"')    # even a single unexpected double quote added to a log could break this

            # extract IP address
            # match from the start of the line until the last number before a hyphen
            # uses a look ahead to stop searching for numbers at the first hyphen
            # there is improved regex for IP matching but overkill for this scenario where it's position is predictable
            ipAddress = re.search(r'.*[0-9](?=.+-)',seperated_line[0])[0] 
            
            # extract URL
            # split string by space and return index 1
            URL = seperated_line[1].split()[1]

            # extract and parse datetime and convert timezone to UTC
            dtString = re.search(r'\[.*\]',seperated_line[0])[0].strip("[]") # timestamp
            dtLocal = datetime.strptime(dtString,'%d/%b/%Y:%H:%M:%S %z').timestamp()
            dtUTC = datetime.fromtimestamp(dtLocal, tz = timezone.utc)

        except Exception as e:
            print("Error separating header and message on line %d: %s "%(i,e))

        # append parsed log line values to dict
        log_info.append({'ip_address':ipAddress, 'timestamp':dtUTC, 'URL':URL})

    #print(log_info)
    return log_info

parse_log('example-data.log')

        ## ORIGINAL APPROACH
        # try:
        #     messageSearch = re.search(r'\".*\"',line)
        #     logHeader = line[0:messageSearch.span()[0]]
        #     logMessage = messageSearch[0]
        # except Exception as e:
        #     print("Error Separating header and message on line %d: %s "%(i,e))

        # # parse log header contents
        # try:
        #     # match match from the start of the line till the last number before a hyphen
        #     # uses a look ahead to stop searching for numbers at the first hyphen
        #     # there is improved regex for IP matching but overkill for this scenario where it's position is predictable
        #     ipAddress = re.search(r'.*[0-9](?=.+-)',logHeader)[0] 

        #     # parse datetime and convert to UTC
        #     dtString = re.search(r'\[.*\]',logHeader)[0].strip("[]") # timestamp
        #     dtLocal = datetime.strptime(dtString,'%d/%b/%Y:%H:%M:%S %z').timestamp()
        #     dtUTC = datetime.fromtimestamp(dtLocal, tz = timezone.utc)

        #     # parse user - not required
        #     # search for user between hyphen and open square bracket, remove spaces.
        #     # user = re.search(r'(?<=-).*?(?=\[)',logHeader)[0].strip()
        #     # TODO replace empty matches with null
        #     # print(user)

        #     log_info.append({'ip_address':ipAddress, 'timestamp':dtUTC})

        # except Exception as e:
        #     print("Error Parsing Log Message on line %d: %s "%(i,e))