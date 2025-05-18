import requests
import time
from porsline.models import APIError

class PorslineAPIException(Exception):
    def __init__(self, status_code, message):
        super().__init__(f"Porsline API Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message

class PorslineClient:
    BASE_URL = "https://survey.porsline.ir"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def request(self, method: str, endpoint: str, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"API-Key {self.api_key}"
        headers["Content-Type"] = "application/json"

        for attempt in range(5):
            response = requests.request(method, f"{self.BASE_URL}{endpoint}", headers=headers, **kwargs)
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", "60"))
                print(f"Rate limited. Retrying in {retry_after} seconds...")
                time.sleep(retry_after)
                continue
            try:
                response.raise_for_status()
            except requests.HTTPError:
                raise PorslineAPIException(response.status_code, response.text)
            return response.json()

        raise PorslineAPIException(429, "Too many retries due to rate limiting.")