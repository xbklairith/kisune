from dataclasses import dataclass, field
from decimal import Decimal

from billing.invoice import Invoice


@dataclass
class Account:
    company_name: str
    balance: Decimal = Decimal("0")
    credit_limit: Decimal = Decimal("5000")
    invoices: list[Invoice] = field(default_factory=list)
    member_emails: list[str] = field(default_factory=list)

    def charge(self, amount: Decimal) -> Invoice:
        if self.balance + amount > self.credit_limit:
            raise ValueError("over credit limit")
        self.balance += amount
        invoice = Invoice(account_name=self.company_name, amount=amount)
        self.invoices.append(invoice)
        return invoice
