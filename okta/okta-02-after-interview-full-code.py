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
import datetime

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
last_3_days = datetime.datetime.now() - datetime.timedelta(days=3)
last_3_days = last_3_days.strftime("%Y-%m-%d")

# _url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-03-14&end_date=2025-03-16&api_key=DEMO_KEY"
_url = "https://api.nasa.gov/neo/rest/v1/feed"
params = {
    "start_date": last_3_days,
    "end_date": current_date,
    "api_key": "DEMO_KEY"
}
# get the data from API
resp = requests.get(_url,params=params)
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

#2. Find all the IDs and Names of all asteroids that are potentially hazardous i.e "is_potentially_hazardous_asteroid": true
    _per_date = _near_e[date] 
    for ast in _per_date:
        if ast["is_potentially_hazardous_asteroid"]:
            print(f"ID: {ast['id']} Name: {ast['name']} is potentially hazardous")

#3. Find the IDs/Names of all asteroids that are larger than 0.5 miles in diameter ( maximum )
        if ast["estimated_diameter"]["miles"]["estimated_diameter_max"] > 0.5:
            print(f"ID: {ast['id']} Name: {ast['name']} is larger than 0.5 miles in diameter")
    print("*"*50)
    print("\n")

"""
**************************************************
Count of Asteroids on - 2025-03-14 is 17
**************************************************
ID: 3114018 Name: (2002 CS11) is larger than 0.5 miles in diameter
ID: 3365954 Name: (2007 AF2) is larger than 0.5 miles in diameter
ID: 3758927 Name: (2016 RN1) is potentially hazardous
ID: 3758927 Name: (2016 RN1) is larger than 0.5 miles in diameter
ID: 54291148 Name: (2022 OC1) is larger than 0.5 miles in diameter
**************************************************


**************************************************
Count of Asteroids on - 2025-03-15 is 14
**************************************************
ID: 54522922 Name: (2025 EV2) is larger than 0.5 miles in diameter
**************************************************


**************************************************
Count of Asteroids on - 2025-03-16 is 11
**************************************************
ID: 2325102 Name: 325102 (2008 EY5) is larger than 0.5 miles in diameter
ID: 3758247 Name: (2016 QE44) is larger than 0.5 miles in diameter
ID: 3802451 Name: (2018 GJ2) is larger than 0.5 miles in diameter
ID: 54075550 Name: (2020 UF2) is potentially hazardous
ID: 54075550 Name: (2020 UF2) is larger than 0.5 miles in diameter
ID: 54298762 Name: (2022 QF7) is larger than 0.5 miles in diameter
**************************************************


**************************************************
Count of Asteroids on - 2025-03-17 is 7
**************************************************
**************************************************
"""
