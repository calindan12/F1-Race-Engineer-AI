import requests

response = requests.get(
    "https://api.openf1.org/v1/drivers?driver_number=1"
)

print(response.status_code)
print(response.json())