# resume parsing and scoring

def parse_resume(text:str)->dict:
    """Parses raw resume text and extracts key profile attributes.

    Note:
        This is a placeholder/dummy parser. Replace with a real NLP-based parser.

    Args:
        text (str): Raw resume text.

    Returns:
        dict: Extracted profile information including skills, experience,
            and a summary.
    """  
    return {
        "skills":["python","fastapi","docker"],
        "years_of_experience":4,
        "summary":"software engineer with backend experience",
    }

def score_against_id(jd:str,profile:dict)-> dict:
    """Scores a parsed candidate profile against a job description.

    Note:
        This is a simplified dummy scoring mechanism. Replace with real
        model-based scoring logic.

    Args:
        jd (str): The job description text.
        profile (dict): Parsed candidate profile containing skills, experience, etc.

    Returns:
        dict: Scoring details including numeric score, decision, and reasons.
 """  
    score=0.8 #pretending  computed
    reasons="Good match on skills and experience"
    decision="shortlist" if score>0.7 else "reject"
    return {
       
        "score":score,
        "decision":decision,
        "reasons":reasons
    }
#-------------------------------------------------------
## scheduling tools
#--------------------------------------------------------
PANEL_SLOTS={
    "backend_engineer":[
        "2025-12-13T10:00:00Z",
        "2025-12-13T11:00:00Z",
        "2025-12-13T15:00:00Z",
        "2025-12-13T16:00:00Z",
    ]
}

BOOKED: list[str]=[]

def get_panel_availability(role: str) -> list[str]:
    """
    Returns the list of available interview panel slots for a given role.

    This function checks all predefined panel slots for the specified role
    and filters out any slots that have already been booked.

    Args:
        role (str): The job role for which panel availability is requested.

    Returns:
        list[str]: A list of available (unbooked) time slots for the role.
    """
    return [s for s in PANEL_SLOTS.get(role, []) if s not in BOOKED]


def book_slot(candidate_id: str, slot: str) -> dict:
    """
    Attempts to book an interview slot for a candidate.

    If the slot is already booked, the function returns a failure response.
    Otherwise, it books the slot and returns a confirmation.

    Args:
        candidate_id (str): Unique identifier of the candidate requesting the slot.
        slot (str): The interview time slot to be booked.

    Returns:
        dict: A dictionary containing:
            - "status" (str): "confirmed" or "failed"
            - "slot" (str): The booked slot or reason for failure
    """
    if slot in BOOKED:
        return {"status": "failed", "slot": "already booked"}
    BOOKED.append(slot)
    return {"status": "confirmed", "slot": slot}
#-----------------------------------------------------
### Feedback + decision tools
#-----------------------------------------------------
def simulate_feedback(round_no: int) -> str:
    """
    Generates simulated interview feedback for a given round.

    This function returns predefined feedback text based on the interview
    round number. Round 1 focuses on Python and basic design skills, while
    later rounds emphasize system design and communication.

    Args:
        round_no (int): The interview round number.

    Returns:
        str: A feedback string describing the candidate's performance.
    """
    if round_no == 1:
        return "Round 1 feedback: strong python and basic design skills"
    else:
        return f"Round 2 feedback: strong system design and communication skills"


def decide_next_step(feedback: str, round_no: int) -> str:
    """
    Determines the next step in the interview process based on feedback.

    The decision logic is:
    - If feedback contains "weak": reject.
    - If feedback contains "strong" and round_no >= 2: offer.
    - If feedback contains "strong" and round_no == 1: move to next round.
    - Otherwise: reject.

    Args:
        feedback (str): The feedback text from the interviewer.
        round_no (int): The current interview round number.

    Returns:
        str: One of "reject", "next_round", or "offer".
    """
    feedback_parsed = feedback.lower()
    if "weak" in feedback_parsed:
        return "reject"
    if "strong" in feedback_parsed and round_no >= 2:
        return "offer"
    if "strong" in feedback_parsed and round_no == 1:
        return "next_round"
    return "reject"