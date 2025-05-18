from porsline.models import Question

class QuestionService:
    def __init__(self, client):
        self.client = client

    def add_question(self, survey_id: int, question: Question) -> Question:
        payload = question.dict(exclude_unset=True)
        data = self.client.request("POST", f"/api/v2/surveys/{survey_id}/questions/", json=payload)
        return Question(**data)