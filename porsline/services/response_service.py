from porsline.models import ResponseEntry

class ResponseService:
    def __init__(self, client):
        self.client = client

    def generate_hashed_links(self, survey_id: int, values: list):
        return self.client.request("POST", f"/api/surveys/{survey_id}/variables/hashes/", json={"values": values})

    def get_all_responses(self, survey_id: int):
        page = 1
        page_size = 100
        all_data = []

        while True:
            res = self.client.request("GET", f"/api/v2/surveys/{survey_id}/responses/results-table/?page={page}&page_size={page_size}")
            results = res.get("results", [])
            all_data.extend([ResponseEntry(**r) for r in results])
            if not res.get("next"):
                break
            page += 1

        return all_data

    def get_responses_after(self, survey_id: int, last_index: int):
        page = 1
        page_size = 100
        collected = []
        total_seen = 0

        while True:
            res = self.client.request("GET", f"/api/v2/surveys/{survey_id}/responses/results-table/?page={page}&page_size={page_size}")
            results = res.get("results", [])

            if total_seen + len(results) <= last_index:
                total_seen += len(results)
                page += 1
                continue

            new_start = last_index - total_seen if total_seen < last_index else 0
            collected.extend([ResponseEntry(**r) for r in results[new_start:]])

            if not res.get("next"):
                break

            total_seen += len(results)
            page += 1

        return collected

    def get_responses_since(self, survey_id: int, since_timestamp: str):
        page = 1
        page_size = 100
        collected = []

        while True:
            url = f"/api/v2/surveys/{survey_id}/responses/results-table/?since={since_timestamp}&page={page}&page_size={page_size}"
            res = self.client.request("GET", url)
            results = res.get("results", [])
            collected.extend([ResponseEntry(**r) for r in results])

            if not res.get("next"):
                break

            page += 1

        return collected