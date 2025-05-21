import requests

BACKEND_URL = 'http://localhost:8000/upload/'

def upload_file(path):
    with open(path, 'rb') as f:
        files = {'file': (path, f)}
        r = requests.post(BACKEND_URL, files=files)
        print(r.json())

if __name__ == "__main__":
    upload_file('test.txt')
