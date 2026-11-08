"""Order statuses and the moves allowed between them."""
from enum import Enum


class Status(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    PACKED = "packed"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    RETURN_REQUESTED = "return_requested"
    REFUNDED = "refunded"


# status -> {event: next status}
TRANSITIONS = {
    Status.PENDING: {"pay": Status.PAID, "cancel": Status.CANCELLED},
    Status.PAID: {"pack": Status.PACKED, "cancel": Status.REFUNDED},
    Status.PACKED: {"ship": Status.SHIPPED, "cancel": Status.REFUNDED},
    Status.SHIPPED: {"deliver": Status.DELIVERED, "lose": Status.REFUNDED},
    Status.DELIVERED: {"request_return": Status.RETURN_REQUESTED},
    Status.RETURN_REQUESTED: {"approve_return": Status.REFUNDED, "reject_return": Status.DELIVERED},
}

FINAL = {Status.CANCELLED, Status.REFUNDED}

RETURN_WINDOW_DAYS = 30


class InvalidTransition(Exception):
    pass


def next_status(current, event, days_since_delivery=0):
    if current in FINAL:
        raise InvalidTransition(f"{current.value} is final")
    if event == "request_return" and days_since_delivery > RETURN_WINDOW_DAYS:
        raise InvalidTransition("return window closed")
    try:
        return TRANSITIONS[current][event]
    except KeyError:
        raise InvalidTransition(f"cannot {event} from {current.value}") from None
