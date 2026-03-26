import logging

def setup_logger():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,
        format="%(levelname)s - %(message)s"
    )
    return logging.getLogger("maintenance_lab")
