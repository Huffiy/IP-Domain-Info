import ipinfo
import sys
import socket

try:
    input = sys.argv[1]
except IndexError:
    input = None
# access token for ipinfo.io (https://ipinfo.io/account/token)
access_token = 'YOUR_TOKEN_HERE'

handler = ipinfo.getHandler(access_token)

if (input == None):
    details = handler.getDetails()
else:
    if (input == True) :
        details = handler.getDetails(input)
    else:
        ipOfDomain = socket.gethostbyname_ex(input)
        details = handler.getDetails(ipOfDomain[2][0])

for key, value in details.all.items():
    print(f"{key}: {value}")
