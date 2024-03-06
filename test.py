import requests

headers = {
    "Authorization": "Bearer b1705e235b0b06ae9ee013996ef18801"
}

# Make a GET request with custom headers
response = requests.get("https://neocities.org/api/list", headers=headers)

# Print the response
print(response.text)