from typing import Any, Dict, Tuple, Optional
from .missed_stop import MissedStop
from .monitor import Evaluator, SimpleEvaluator, MonitoringResult
from .types import Planner, State, Action, ErrorInfo


class PlanDisruptionModel:
    def __init__(
        self,
        planner: Planner,
        missed_stop: MissedStop,
        evaluator: Optional[Evaluator] = None,
    ) -> None:
        self.planner = planner
        self.missed_stop = missed_stop
        self.evaluator = evaluator or SimpleEvaluator()

    def step(self, state: State, goal: Any) -> Tuple[Action, Dict[str, Any]]:
        plan = self.planner.make_plan(state, goal)
        action = self.planner.act(state, plan)

        monitoring = self._evaluate(state, action, goal)

        if monitoring.success:
            return action, {"status": "ok"}

        if monitoring.error is None:
            monitoring.error = ErrorInfo(reason="unknown_failure")

        recovery = self.missed_stop.reflect_and_recover(
            state=state,
            plan=plan,
            error=monitoring.error,
        )
        new_action = self._apply_recovery(state, recovery)

        return new_action, {
            "status": "recovered",
            "recovery": recovery,
        }

    def _evaluate(
        self,
        state: State,
        action: Action,
        goal: Any,
    ) -> MonitoringResult:
        return self.evaluator.evaluate(state, action, goal)

    def _apply_recovery(self, state: State, recovery: Dict[str, Any]) -> Action:
        return {"do": recovery.get("action", "noop"), "meta": recovery}

