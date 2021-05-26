# Tasks
# Create a program that request a post code
# check if the postcode is valid
# then uses an API call to fetch more data from post code
# display the data in user friendly format

import requests
postcode_api = "https://api.postcodes.io/postcodes/"
postcode = input("Please enter your postcode: ")
user_postcode = postcode_api + postcode
post_api_response = requests.get(user_postcode)
if post_api_response == 200:
    print("That is a valid postcode, thank you! ")
else:
    print("Sorry the postcode you entered is incorrect, please enter the correct postcode! ")