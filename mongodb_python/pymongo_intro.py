import pymongo
from pprint import pprint

# NOTE! Need to have MongoD (daemon) up and running to use pymongo
client = pymongo.MongoClient()
# default MongoDB port: 27017
db = client['starwars']

# now, syntax mostly the same as mongodb
# EXCEPT Python uses snake_case, NOT camelCase as in MongoDB
# also, need quotes around field names, because Python

luke = db.characters.find_one({"name": "Luke Skywalker"})
#print(type(luke))
pprint(luke)

# db.characters.find() produces a cursor object - MongoDB shell prints info in cursor with find()
# for pymongo, we need to use find_one instead
# db.characters.find_one() produces a standard Python dictionary!

# pprint default: keys sorted alphabetically - to disable:
# type 'pprint(luke, sort_dicts=False)'
print(luke[0])  # index in cursor
print(list(luke))  # can force into list

# cursor objects are ITERABLE -> use for loop
for char in luke:
#    print(char) #
    print(char["name"])

blue = db.characters.find({"eye_color": "blue"})
blue_names = map(lambda x: x["name"], blue)
print(list(blue_names))

# species names begin with capital letter!
droids = db.characters.find({"species.name": "Droid"})
droid_names = map(lambda x: x["name"], droids)
#print(list(droid_names))
# OR
for bot in droids:
    print(bot["name"])

# return height, name of Darth Vader
print(db.characters.find_one({"name": "Darth Vader"}, {"name": 1, "height": 1, "_id": 0}))
# less efficient, but still valid: assign query to variable, then do Python print
# for regex, example: find({"name": {"$regex": "Vader"}},{return-y stuff})

# return characters with yellow eyes, only return names
for i in db.characters.find(
        {"eye_color": "yellow"},
        {"name": 1, "_id": 0}):
    print(i)

# find male characters, limit results to show only first 3
print('male chars:')
male_chars = db.characters.find({"gender": "male"}, {"name": 1, "_id": 0}).limit(3)
# mongoDB .limit(n) method: limits result to length n
for guy in male_chars:  # instead of limit, could use male_chars[0:3]
    print(guy)

# find names of all humans whose homeworld in Alderaan
print('Alderaanian types')
ald_ones = db.characters.find({"homeworld.name": "Alderaan", "species.name": "Human"},
                              {"name": 1, "_id": 0}) # "homeworld.name": 1, "species.name": 1,
for person in ald_ones:
    print(person)

# average height of female characters
avg_f_height = db.chardemo.aggregate([{"$match": {"gender": "female", "height": {"$ne": float("nan")}}},
                                        {"$group": {"_id": "$gender", "av_f_height": {"$avg": "$height"}}}])
print(avg_f_height.next())

# which character is the tallest
max_height = db.chardemo.aggregate([{"$match": {"height": {"$ne": float("nan")}}},
                                    {"$group": {"_id": "null",
                                                "max_height": {"$max": "$height"}}}]).next()['max_height']
print(max_height)
for char_height in db.chardemo.find({"height": max_height}, {"name": 1, "height": 1, "_id": 0}):
    print(char_height)
