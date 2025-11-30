from typing import Iterable
from .types import Episode

def perseverance_reward(episodes: Iterable[Episode]) -> float:
    episodes_list = list(episodes)
    if not episodes_list:
        return 0.0
    return float(len(episodes_list))

