from enum import Enum
from typing import List
from uuid import UUID

from eventsource.models.DomainModel import Aggregate

from eventsourcing.domain import event


class PayrollRunState(Enum):
    DRAFT = 1
    APPROVED = 2


class PayrollRun(Aggregate):
    @event('Create')
    def __init__(self, state: PayrollRunState, employees: List[UUID] = []) -> None:
        self.state = state
        self.employees: List[UUID] = employees

    @event('AddEmployees')
    def add_employees(self, employees: list):
        self.employees = employees
