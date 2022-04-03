import requests
from decouple import config
from datetime import date, datetime

headers = {
    "X-USER-TOKEN": config('GENERATED_TOKEN')
}

pixel_param_user = {
    "token": config('GENERATED_TOKEN'),
    "username": config('USERNAME'),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create user API. 
create_user_request = requests.post(config('PIXEL_ENDPOINT'), json=pixel_param_user)
print(create_user_request.text)

graph_endpoint = f"{config('PIXEL_ENDPOINT')}/{config('USERNAME')}/graphs"

pixel_param_graph = {
    "id": config('GRAPH_ID'),
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai" 
}

# Create graph API.
create_graph_request = requests.post(graph_endpoint, headers=headers, json=pixel_param_graph)
print(create_graph_request.text)

# Get a Graph...... Check readme.md file.

# Post value to the Graph.
post_value_endpoint = f"{graph_endpoint}/{pixel_param_graph['id']}"

pixel_post_graph_param = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "5.5"
}

post_value_to_graph = requests.post(post_value_endpoint, headers=headers, json=pixel_post_graph_param)
print(post_value_to_graph.text)