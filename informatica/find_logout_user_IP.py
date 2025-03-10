# Problem list of input lines from text files
# find the user and IP if action is logout
# user regex to acheive this task.

audit_events = [
    "Timestamp: 2023-10-01T08:15:23Z, User: john_doe, IP: 192.168.1.101, Action: login",
    "Timestamp: 2023-10-01T08:20:45Z, User: jane_smith, IP: 192.168.1.102, Action: failed",
    "Timestamp: 2023-10-01T09:05:12Z, User: admin, IP: 192.168.1.105, Action: login",
    "Timestamp: 2023-10-01T10:30:56Z, User: john_doe, IP: 192.168.1.101, Action: logout",
    "Timestamp: 2023-10-01T11:15:34Z, User: guest, IP: 192.168.1.110, Action: failed",
    "Timestamp: 2023-10-01T12:45:22Z, User: jane_smith, IP: 192.168.1.102, Action: login",
    "Timestamp: 2023-10-01T13:20:11Z, User: admin, IP: 192.168.1.105, Action: logout",
    "Timestamp: 2023-10-01T14:50:09Z, User: john_doe, IP: 192.168.1.101, Action: failed",
    "Timestamp: 2023-10-01T15:30:47Z, User: guest, IP: 192.168.1.110, Action: login",
    "Timestamp: 2023-10-01T16:05:33Z, User: jane_smith, IP: 192.168.1.102, Action: logout"
]

# Solution
# FYI: I didn't solve this during the interview with regex instead I used split function with string comparison
import re
regex = ".*(User:\s)(?P<user>.*)(,\s)(IP:\s)(?P<IP>\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*(Action:\s)(?P<action>logout)"
r_c = re.compile(regex)

for line in audit_events:
    m = r_c.match(line)
    if m:
        print(m.group(2), m.group(5))

# Output
# john_doe 192.168.1.101
# admin 192.168.1.105
# jane_smith 192.168.1.102
