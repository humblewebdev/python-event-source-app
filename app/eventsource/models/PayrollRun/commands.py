import typing
from uuid import UUID


class CreatePayrollRunCommand(typing.NamedTuple):
    status: str
    employees: typing.List


class AddEmployeeToPayrollrunCommand(typing.NamedTuple):
    payroll_run_id: UUID
    employee_id: UUID


class RemoveEmployeeFromPayrollRunCommand(typing.NamedTuple):
    payroll_run_id: UUID
    employee_id: UUID


