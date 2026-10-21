import secrets
from dataclasses import dataclass, field
from datetime import datetime, timedelta

from auth.account import Account


@dataclass
class Session:
    account: Account
    token: str = field(default_factory=lambda: secrets.token_urlsafe(32))
    expires_at: datetime = field(
        default_factory=lambda: datetime.now() + timedelta(hours=12)
    )
