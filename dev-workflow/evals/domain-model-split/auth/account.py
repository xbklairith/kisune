import hashlib
import hmac
from dataclasses import dataclass
from datetime import datetime


def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


@dataclass
class Account:
    email: str
    password_hash: str
    last_login: datetime | None = None

    def verify_password(self, password: str) -> bool:
        return hmac.compare_digest(self.password_hash, _hash(password))
