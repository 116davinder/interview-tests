"""
NASA runs the Near Earth Object Web Service, which is a RESTful web service for near earth Asteroid information.  A user can search for Asteroids based on their closest approach date to Earth,  look up a specific Asteroid with its NASA JPL small body id, as well as browse the overall data-set.

The full API docs are at https://api.nasa.gov/index.html 

Write a simple Python/Go (or any other language/tooling) client that queries the NEOWS API for the last 3 days.

Example URI: https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-09-07&end_date=2022-09-08&api_key=DEMO_KEY 
There is no need to use an API key for this question, the DEMO_KEY is sufficient for the duration of the interview

From here, please:

1. Count how many asteroids there were on each day

2. Find all the IDs and Names of all asteroids that are potentially hazardous i.e "is_potentially_hazardous_asteroid": true 

3. Find the IDs/Names of all asteroids that are larger than 0.5 miles in diameter ( maximum )
"""

# assume current and last 3 days
import requests
import json

_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-03-14&end_date=2025-03-16&api_key=DEMO_KEY"

# get the data from API
resp = requests.get(_url)
if resp.status_code == 200:
    json_re = resp.json()
    # print(json_re)
else:
    print("error", resp.status_code)

# print(json_re["links"])
# print(json_re["element_count"])

_near_e = json_re["near_earth_objects"]
for date in _near_e:
    print("*"*50)
    print(f"Count of Asteroids on - {date} is {len(_near_e[date])}")
    print("*"*50)

    _per_date = _near_e[date] 
    for ast in _per_date:
        print(ast)
# parse the data for different conditions

# print the data


