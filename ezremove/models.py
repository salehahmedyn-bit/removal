from dataclasses import dataclass
from typing import Optional

@dataclass
class JobResult:
    job_id: str
    image_url: Optional[str] = None
    status: str = "pending"
    error_message: Optional[str] = None

