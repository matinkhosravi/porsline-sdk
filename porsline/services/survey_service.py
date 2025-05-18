from porsline.models import SurveySetting

class SurveyService:
    def __init__(self, client):
        self.client = client

    def get_settings(self, survey_id: int) -> SurveySetting:
        data = self.client.request("GET", f"/api/surveys/{survey_id}/settings/")
        return SurveySetting(**data["survey"])

    def update_settings(self, survey_id: int, settings: dict):
        return self.client.request("PATCH", f"/api/surveys/{survey_id}/settings/", json=settings)
