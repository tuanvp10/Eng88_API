# Let's use python to make an API call using package called requests
# Dependencies are Pip

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
