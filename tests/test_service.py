import pytest
from src.storage import Storage
from src.logger import setup_logger
from src.service import process_order

class DummyStorage(Storage):
    def reserve(self, user: str, product: str, qty: int) -> str:
        return "RES-0000"

def test_process_ok():
    logger = setup_logger()
    storage = DummyStorage()
    result = process_order("alice, coffee, 2", storage, logger)
    assert result.amount == 360

def test_unknown_product_raises():
    logger = setup_logger()
    storage = DummyStorage()
    with pytest.raises(KeyError):
        process_order("kate, pizza, 1", storage, logger)
