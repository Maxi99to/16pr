from dataclasses import dataclass
from .catalog import PRODUCTS

@dataclass
class OrderResult:
    user: str
    product: str
    qty: int
    amount: int
    reserve_id: str

def parse_order(raw: str):
    parts = raw.split(",")
    user = parts[0].strip()
    product = parts[1].strip()
    qty = int(parts[2].strip())
    return user, product, qty

def calculate_amount(product: str, qty: int) -> int:
    price = PRODUCTS[product]
    return price * qty

def process_order(raw: str, storage, logger) -> OrderResult:
    stage = "start"
    user = "unknown"

    stage = "parse_order"
    user, product, qty = parse_order(raw)

    stage = "calculate_amount"
    amount = calculate_amount(product, qty)

    stage = "reserve"
    reserve_id = storage.reserve(user, product, qty)

    logger.info(f"OK user={user} product={product} qty={qty} amount={amount} reserve={reserve_id}")

    return OrderResult(user=user, product=product, qty=qty, amount=amount, reserve_id=reserve_id)
