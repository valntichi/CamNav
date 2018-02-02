import json

with open('data/users-tracer.json') as data_file:
    json_data = json.load(data_file)
    print json_data
    print json_data[0]['username']