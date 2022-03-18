import requests

# ---------------to download an image with python--------
# r = requests.get('https://www.programming-hero.com/blog/assets/images/blog/python-developer-roadmap-follow-this-roadmap-and-become-a-python-hero.png')
# with open('py.png','wb') as f:
#     f.write(r.content)


# -----------------------get request-----------------
# r = requests.get('https://community-open-weather-map.p.rapidapi.com/weather')
# print(r.text)


#--------------- post request---------
# data = {
#     'username' : "asifmdasif",
#     'password': '123448'
# }
# r = requests.post('https://httpbin.org/post',data = data)
# # print(r.text)
# json_dict = r.json()
# print(json_dict['form'])


#---------basic authentication route--------------
# r = requests.get('https://httpbin.org/basic-auth/asif/testing',auth=('asif','testing'))
# print(r.text)


#------------my django rest framework api testing-----------------------
data = {
    "username" : "root",
    "password" : "root"

}

r = requests.post('http://127.0.0.1:8000/api/token/',data=data)
print(r.text)
