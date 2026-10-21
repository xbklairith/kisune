from dataclasses import dataclass
from datetime import datetime

from todo.task import Task


@dataclass
class Reminder:
    task: Task
    fire_at: datetime
    sent: bool = False
