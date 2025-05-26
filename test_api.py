import requests

url = "http://127.0.0.1:5000/validate"
data = {
    "hsn_codes": ["01", "0101", "9954", "123"]
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response JSON:", response.json())
except Exception as e:
    print("Error during request:", e)
