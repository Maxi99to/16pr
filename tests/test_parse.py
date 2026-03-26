import pytest
from src.service import parse_order

def test_parse_ok():
    user, product, qty = parse_order("alice, coffee, 2")
    assert user == "alice"
    assert product == "coffee"
    assert qty == 2

def test_parse_invalid_qty():
    with pytest.raises(ValueError):
        parse_order("john, coffee, two")
