from porsline.models import Folder
from typing import List

class FolderService:
    def __init__(self, client):
        self.client = client

    def list_folders(self) -> List[Folder]:
        data = self.client.request("GET", "/api/folders/")
        return [Folder(**item) for item in data]

    def get_folder(self, folder_id: int) -> Folder:
        data = self.client.request("GET", f"/api/folders/{folder_id}/")
        return Folder(**data)

    def create_folder(self, name: str, order: int = None):
        data = {"name": name}
        if order is not None:
            data["order"] = order
        return self.client.request("POST", "/api/folders/", json=data)

    def update_folder(self, folder_id: int, name: str, order: int = None):
        data = {"name": name}
        if order is not None:
            data["order"] = order
        return self.client.request("PUT", f"/api/folders/{folder_id}/", json=data)

    def delete_folder(self, folder_id: int):
        return self.client.request("DELETE", f"/api/folders/{folder_id}/")