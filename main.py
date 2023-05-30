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

def valid_IP_Address(sample_str):
    result = True
    match_obj = re.search( r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", sample_str)
    if  match_obj is None:
        result = False
    else:
        for value in match_obj.groups():
            if int(value) > 255:
                result = False
                break
    return result


if (input == True) :
    details = handler.getDetails(input)
else:
    ipOfDomain = socket.gethostbyname_ex(input)
    details = handler.getDetails(ipOfDomain[2][0])


for key, value in details.all.items():
    print(f"{key}: {value}")
