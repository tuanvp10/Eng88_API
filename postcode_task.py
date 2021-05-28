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
