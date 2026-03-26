import random
import time

class Storage:
    def reserve(self, user: str, product: str, qty: int) -> str:
        time.sleep(random.uniform(0.01, 0.05))
        if random.random() < 0.15:
            raise TimeoutError("DB timeout")
        return f"RES-{random.randint(1000, 9999)}"
