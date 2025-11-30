import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from upheaval.memory import MissedStopMemory
from upheaval.types import Episode, ErrorInfo

def test_memory_add_and_retrieve():
    mem = MissedStopMemory()
    for i in range(5):
        ep = Episode(
            state={"s": i},
            plan={"p": i},
            error=ErrorInfo(reason="e"),
            recovery_strategy={"action": "a"},
        )
        mem.add_episode(ep)

    last_three = mem.retrieve_similar(state={"s": 99}, k=3)
    assert len(last_three) == 3
    assert last_three[-1].state == {"s": 4}

