from dataclasses import dataclass
from typing import Any, Dict, Protocol, Optional

State = Any
Plan = Any
Action = Any

@dataclass
class ErrorInfo:
    reason: str
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class Episode:
    state: State
    plan: Plan
    error: ErrorInfo
    recovery_strategy: Dict[str, Any]

class Planner(Protocol):
    def make_plan(self, state: State, goal: Any) -> Plan:
        ...
    def act(self, state: State, plan: Plan) -> Action:
        ...

