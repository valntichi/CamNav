import requests

url = "https://api.instagram.com/v1/users/{user-id}/follows?access_token=ACCESS-TOKEN"
client_id = "a30036007ba14662ac3deb3fd902691b"
redirect_uri = "http://my.host.co.za"

url = "url = https://api.instagram.com/oauth/authorize/?client_id=%s&redirect_uri=%s&response_type=code"%(
    client_id, redirect_uri
)
print url

#  authorise
response = requests.get(url)
print response.text

"""
Client ID 	a30036007ba14662ac3deb3fd902691b
Client Status 	Sandbox Mode 


1- https://api.instagram.com/oauth/authorize/?client_id=CLIENT-ID&redirect_uri=REDIRECT-URI&response_type=code
2- my.host.co.za?code=CODE
3-
curl -F 'client_id=a30036007ba14662ac3deb3fd902691b' \
    -F 'client_secret=65f12c6c280f420a9db8f72c2da16325' \
    -F 'grant_type=authorization_code' \
    -F 'redirect_uri=my.host.co.za' \
    -F 'code=035c660f9fcc47e589494358e0258a58' \
    https://api.instagram.com/oauth/access_token
    
"""
