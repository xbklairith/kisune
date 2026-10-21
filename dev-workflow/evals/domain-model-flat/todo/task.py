from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    project_id: int
    due: date | None = None
    done: bool = False

    def complete(self) -> None:
        self.done = True
