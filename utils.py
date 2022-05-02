from random import randint
from typing import Tuple

class Utils():
    def generate_position(self, min: int, max: int) -> Tuple[int, int]:
        return randint(min, max)

