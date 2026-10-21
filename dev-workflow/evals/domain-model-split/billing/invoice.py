from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal


@dataclass
class Invoice:
    account_name: str
    amount: Decimal
    issued_on: date = field(default_factory=date.today)
    paid: bool = False
