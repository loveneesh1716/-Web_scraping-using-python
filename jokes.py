


import requests
import json

jokes_dict = {}

number_of_jokes= int(input(' Enter number of jokes you want to Scrape '))

#scrapping all the jokes and adding to the dictionary with their index
for i in range(1, number_of_jokes):
    jokes_url = f"http://api.icndb.com/jokes/{i}"
    if json.loads(requests.get(jokes_url).content)['type'] == 'success':
        jokes_dict[i] = (json.loads(requests.get(jokes_url).content)['value']['joke'])
        print(jokes_dict[i])
        
joke_number = int(input("Enter the joke Number"))

print(jokes_dict[joke_number])




