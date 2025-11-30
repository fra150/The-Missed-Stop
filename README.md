# Plan Disruption – The Missed Stop

This module implements the idea of "The Missed Stop" in code: a network that doesn't give up when the plan fails, uses thinking time to review the past, and writes lessons for the future.

## Architecture

- Main Planner (`src/upheaval/planner.py`)
- Monitor / Sentinel (`src/upheaval/monitor.py`)
- MissedStop (`src/upheaval/missed_stop.py`)
- Missed Stop Memory (`src/upheaval/memory.py`)
- Orchestrator Model (`src/upheaval/core.py`)

## Usage Example

```python
from upheaval import (
    PlanDisruptionModel,
    MissedStop,
    MissedStopMemory,
    SimplePlanner,
)

memory = MissedStopMemory()
missed_stop = MissedStop(memory, think_steps=2)
planner = SimplePlanner()

model = PlanDisruptionModel(
    planner=planner,
    missed_stop=missed_stop,
)

state = {"pos": "home"}
goal = {"pos": "school"}

action, info = model.step(state, goal)

print(action)
print(info)
```

Here `info["status"]` will be `"recovered"` because the default sentinel always simulates a missed stop, to demonstrate the dynamics.
