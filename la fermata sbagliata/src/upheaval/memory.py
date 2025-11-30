from typing import List, Iterable
from .types import Episode, State


class MissedStopMemory:
    def __init__(self) -> None:
        self._episodes: List[Episode] = []

    @property
    def episodes(self) -> Iterable[Episode]:
        return tuple(self._episodes)

    def add_episode(self, episode: Episode) -> None:
        self._episodes.append(episode)

    def retrieve_similar(self, state: State, k: int = 3) -> List[Episode]:
        return self._episodes[-k:]

