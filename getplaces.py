from yelpapi import YelpAPI
from random import randint
consumer_key = ''
consumer_secret = ''
token = ''
token_secret = ''
google_api_key = ''

yelp_api = YelpAPI(consumer_key,consumer_secret, token, token_secret)

def placeSearch(loc):
	all_places = []
	response = yelp_api.search_query(term='bars', location=loc, sort=1, limit=20)
	random = randint(0,len(response["businesses"]))
	for business in response["businesses"]:
		all_places += [business]
	address = all_places[random]["location"]["display_address"]
	place = all_places[random]["id"]
	place_array = place.split("-")
	place_final = ""
	for val in place_array:
		place_final += val + " "

	street = address[0]
	rest = address[len(address) - 1]
	final_add = street + " " + rest
	return place_final, address