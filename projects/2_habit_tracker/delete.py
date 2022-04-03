import requests
from decouple import config

headers = {
    "X-USER-TOKEN": config('GENERATED_TOKEN')
}

# Delete a User.
user_delete_endpoint = f"{config('PIXEL_ENDPOINT')}/{config('USERNAME')}"

delete_user_request = requests.delete(user_delete_endpoint, headers=headers)
print("Deleted User!")

# Delete a Graph.
delete_graph_endpoint = f"{config('PIXEL_ENDPOINT')}/{config('USERNAME')}/graphs/{config('GRAPH_ID')}"

delete_graph_request = requests.delete(delete_graph_endpoint, headers=headers)
print("Deleted Graph!")