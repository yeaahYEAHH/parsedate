import requests
import xml.etree.ElementTree as ET
from const import *

token = 'V1NOUEs6V1NOUEs='

optinons = {
	'Content-type' : 'text/xml;  charset=utf-8',
	'Authorization' : 'Basic ' + token
}

res = requests.post(url, data = soap, headers = optinons)

root =  ET.fromstring(res.text)
print(res.text)

