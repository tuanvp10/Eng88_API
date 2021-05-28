# What is an API?
## API with Python
#### API =  Application Programming Interface
- An API (Application Programming Interface) is a set of functions that allows applications to access data and interact with external software components, operating systems, or microservices. 
- To simplify, an API delivers a user response to a system and sends the system's response back to a user.

## Let's use python to make an API call using package called requests
## Dependencies are Pip
- installing pip is essential when dealing with APIs.
```python
import requests

# response_bbc = requests.get("https://www.bbc.co.uk/")
#
# # print(response_bbc)
# # print(response_bbc.status_code)
#
# print(response_bbc.headers)
# data_headers = response_bbc.headers
# for date_in in data_headers.keys():
#     print(date_in)

# print(data_headers)
# print(type(response_bbc.headers))
# print(type(response_bbc.content))
#
# json_data = response_bbc.json()
# print(type(json_data))
user_postcode = input("Please can you enter your postcode: ""\n")
post_api_response = requests.get("https://api.postcodes.io/postcodes/sw81af")
user_postcode_received = user_postcode
if post_api_response.status_code == 200:
    print("Thanks for the request " + str(post_api_response.status_code))
else:
    print("Sorry the postcode is incorrect, please enter the correct postcode.")

```

## Postcode task

```python
# Tasks
# Create a program that request a post code
# check if the postcode is valid
# then uses an API call to fetch more data from post code
# display the data in user friendly format

import requests

def postcode_check():
    postcode_api = "https://api.postcodes.io/postcodes/"
    postcode = input("Please enter your postcode, without any spaces please: ""\n").lower()
    user_postcode = (f"https://api.postcodes.io/postcodes/{postcode}")
    post_api_response = requests.get(user_postcode)
    if post_api_response.status_code == 200:
        print("That is a valid postcode, thank you! ")
    else:
        print("Sorry the postcode you entered is incorrect, please enter the correct postcode! ")

postcode_check()
```

