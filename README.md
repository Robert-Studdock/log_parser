## Overview
The Log Parser utility is intended to provide meaningful analysis of a very specific format of log file. Currently the utility will provide the number of unique IP addresses, 3 most commonly seen IP addresses and URLs accessed.

This utility only works for a very specific format of log file seen in the `example-data.log`; but could be extended to work for other formats, or provide other analysis.


## Installation
```sh
# Source the python environment
source ./bin/activate

# Install dependencies
pip install requirements.txt
```

## Usage
```sh
# Run log analysis with path to log file
python3 log_analysis.py ./example-data.log
```

# Known Improvements
- General better protected evaluation in specific areas of log parsing so that any descrepencies in log format can more easily be identified and accounted for
- Print counts of most commonly occurring IP addresses and URLs
- Parsing could be made much more robust using a log parsing library such as pylogparser