from typing import Any
from .types import Planner, State, Plan, Action

class SimplePlanner:
    def make_plan(self, state: State, goal: Any) -> Plan:
        return {"goal": goal, "steps": ["go_straight"]}
    def act(self, state: State, plan: Plan) -> Action:
        return {"do": "follow_plan", "plan": plan}
__all__ = ["Planner", "SimplePlanner"]

