import requests

BACKEND_URL = 'http://localhost:8000/health'

def check_backend():
    r = requests.get(BACKEND_URL)
    print(f"Backend status: {r.json()['status']}")

if __name__ == "__main__":
    check_backend()
