from typing import List
from uuid import UUID

from eventsourcing.application import Application
from eventsourcing.persistence import Transcoder, Mapper

from eventsource.infrastructure.persistence import OrjsonTranscoder, PydanticMapper
from eventsource.models.DomainModel import Snapshot
from eventsource.models.PayrollRun.aggregate import PayrollRunState, PayrollRun


class PayrollRunEventStream(Application):
    is_snapshotting_enabled = True
    snapshot_class = Snapshot

    def create_payroll_run(self, payroll_run_state: PayrollRunState, employees: List[UUID] = []):
        payroll_run = PayrollRun(state=payroll_run_state, employees=employees)
        self.save(payroll_run)
        return payroll_run.id

    def add_employees(self, payroll_run_id: UUID, employees: List[UUID]):
        payroll_run: PayrollRun = self.repository.get(payroll_run_id)
        payroll_run.add_employees(employees)
        self.save(payroll_run)

    def get_payroll_run(self, payroll_run_id):
        payroll_run: PayrollRun = self.repository.get(payroll_run_id)
        return {"state": payroll_run.state, "employees": payroll_run.employees}

    def construct_mapper(self) -> Mapper:
        return self.factory.mapper(
            transcoder=self.construct_transcoder(),
            mapper_class=PydanticMapper,
        )

    def construct_transcoder(self) -> Transcoder:
        return OrjsonTranscoder()
