# Porsline SDK

A lightweight, Pythonic SDK for integrating with the [Porsline](https://www.porsline.ir) survey API.  
Ideal for ETL pipelines, analytics, and survey automation.

## 📦 Features

- Fetch survey settings, variables, and responses
- Incremental sync via index or timestamp
- Manage folders and survey questions
- Built-in validation using `pydantic`
- SOLID-compliant structure for extensibility

---

## 🚀 Installation

```bash
pip install porsline-sdk
```
_Has not pushed yet!_ 

## 🔧 Usage
```python
from porsline.client import PorslineClient
from porsline.services import (
    SurveyService, VariableService, ResponseService,
    FolderService, QuestionService
)
from porsline.models import Question

API_KEY = "your_api_key_here"
SURVEY_ID = 123456

client = PorslineClient(API_KEY)

# Survey
survey_service = SurveyService(client)
settings = survey_service.get_settings(SURVEY_ID)
print(settings)

# Variables
variable_service = VariableService(client)
variables = variable_service.get_variables(SURVEY_ID)
print(variables)

# Responses
response_service = ResponseService(client)
all_responses = response_service.get_all_responses(SURVEY_ID)
new_responses = response_service.get_responses_after(SURVEY_ID, last_index=100)
recent_responses = response_service.get_responses_since(SURVEY_ID, "2025-01-01T00:00:00+03:30")

# Folders
folder_service = FolderService(client)
folders = folder_service.list_folders()
print(folders)

# Questions
question_service = QuestionService(client)
new_question = Question(title="How likely are you to recommend us?", type=6)
created_question = question_service.add_question(SURVEY_ID, new_question)
print(created_question)

```

## ✅ Requirements
- `Python >= 3.7`
- `requests`
- `pydantic`

## 📄 License
This project is licensed under the MIT License.

## ✨ Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your proposal.
