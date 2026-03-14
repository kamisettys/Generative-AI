## project set up
* Create a project structure
```bash
mkdir resumescreening
uv sync --package .
uv sync
```

* Installing dependencies
```bash
uv add langgraph python-dotenv
```

* Models:
    * we will start with gemini models from GCP
    * we will use open ai gpt
    * we will use bed rock from AWS
    * we will use Azure AI Foundry/Azure Open AI
    * We will be using local models hosted on ollama

## PART1- Defining the state

* Interviewround
```python
class InterviewRound(TypedDisct):
    round_number: int
    slot: str
    feedback: str|None
    decision: Literal["next_round","reject","offer"]
class CandidateInterview(TypedDict):
    candidate_id:str
    status:str
    current_round:int
    history:List[InterviewRound]

class State(TypedDict):
    job_id:str
    job_description:str
    resumes: list[str]
    screening_result: list[dict]    
    interviews: List[CandidateInterview]
    hr_report:str
```    
