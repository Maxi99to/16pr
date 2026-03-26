from src.version import __version__
from src.logger import setup_logger
from src.storage import Storage
from src.service import process_order

def main():
    logger = setup_logger()
    storage = Storage()
    print(f"Maintenance Lab v{__version__}")

    orders = [
        "alice, coffee, 2",
        "bob, tea, 0",
        "kate, pizza, 1",
        "john, coffee, two",
        "eva, tea, 3",
    ]

    for raw in orders:
        result = process_order(raw, storage, logger)
        print("OK", result)

if __name__ == "__main__":
    main()
#