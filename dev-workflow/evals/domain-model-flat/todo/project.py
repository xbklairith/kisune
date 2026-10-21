from dataclasses import dataclass, field

from todo.task import Task


@dataclass
class Project:
    id: int
    name: str
    tasks: list[Task] = field(default_factory=list)
    archived: bool = False

    def open_tasks(self) -> list[Task]:
        return [t for t in self.tasks if not t.done]
