import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from upheaval import (
    PlanDisruptionModel,
    MissedStop,
    MissedStopMemory,
    SimplePlanner,
)

def test_step_recovers():
    memory = MissedStopMemory()
    missed_stop = MissedStop(memory, think_steps=2)
    planner = SimplePlanner()
    model = PlanDisruptionModel(planner=planner, missed_stop=missed_stop)
    action, info = model.step({"pos": "home"}, {"pos": "school"})
    assert info["status"] == "recovered"
    assert isinstance(action, dict)
    assert len(tuple(memory.episodes)) == 1

