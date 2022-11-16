import socket
import requests
#import requests.packages.urllib3.util.connection as urllib3_cn
    
   
def allowed_gai_family():
    return socket.AF_INET

#urllib3_cn.allowed_gai_family = allowed_gai_family
url = 'https://www.npr.org/sections/business/archive?date=7-1-2022'
data = requests.get(url).text
print(data)