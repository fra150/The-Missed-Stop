import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from upheaval import (
    PlanDisruptionModel,
    MissedStop,
    MissedStopMemory,
    SimplePlanner,
)


def main():
    memory = MissedStopMemory()
    missed_stop = MissedStop(memory, think_steps=2)
    planner = SimplePlanner()
    model = PlanDisruptionModel(planner=planner, missed_stop=missed_stop)
    action, info = model.step({"pos": "home"}, {"pos": "school"})
    print(action)
    print(info)


if __name__ == "__main__":
    main()

