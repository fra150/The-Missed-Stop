from typing import Any, Dict, List
from .memory import MissedStopMemory
from .types import Episode, State, Plan, ErrorInfo

class MissedStop:
    def __init__(self, memory: MissedStopMemory, think_steps: int = 1) -> None:
        self.memory = memory
        self.think_steps = think_steps

    def reflect_and_recover(
        self,
        state: State,
        plan: Plan,
        error: ErrorInfo,
    ) -> Dict[str, Any]:
        past: List[Episode] = list(self.memory.retrieve_similar(state))

        recovery_strategy: Dict[str, Any] = {
            "action": "try_alternative_path",
            "comment": "Do not give up: use chaos to find a different path.",
            "used_past_episodes": len(past),
            "think_steps": self.think_steps,
        }

        episode = Episode(
            state=state,
            plan=plan,
            error=error,
            recovery_strategy=recovery_strategy,
        )
        self.memory.add_episode(episode)

        return recovery_strategy

