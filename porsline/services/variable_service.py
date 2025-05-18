from porsline.models import Variable
from typing import List

class VariableService:
    def __init__(self, client):
        self.client = client

    def get_variables(self, survey_id: int) -> List[Variable]:
        data = self.client.request("GET", f"/api/surveys/{survey_id}/variables/")
        if isinstance(data, dict) and "variables" in data:
            return [Variable(**item) for item in data["variables"]]
        raise ValueError("Unexpected variable response format")

    def create_variables(self, survey_id: int, variables: list):
        return self.client.request("POST", f"/api/surveys/{survey_id}/variables/", json=variables)