from dataclasses import dataclass
from typing import Any, Protocol, Optional
from .types import State, Action, ErrorInfo

@dataclass
class MonitoringResult:
    success: bool
    error: Optional[ErrorInfo]

class Evaluator(Protocol):
    def evaluate(self, state: State, action: Action, goal: Any) -> MonitoringResult:
        ...

class SimpleEvaluator:
    def evaluate(self, state: State, action: Action, goal: Any) -> MonitoringResult:
        return MonitoringResult(
            success=False,
            error=ErrorInfo(reason="missed_stop", metadata={"goal": goal}),
        )

__all__ = ["MonitoringResult", "Evaluator", "SimpleEvaluator"]

