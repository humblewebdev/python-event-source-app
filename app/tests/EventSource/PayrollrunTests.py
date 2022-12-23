import os
from unittest import TestCase
from uuid import uuid4

from eventsource.models.PayrollRun.aggregate import PayrollRunState
from eventsource.projectors.PayrollrunEventStream import PayrollRunEventStream


class PayrollRunTests(TestCase):
    def test_event_creation(self):
        os.environ["PERSISTENCE_MODULE"] = "eventsourcing.sqlite"
        os.environ["SQLITE_DBNAME"] = "payments.sqlite"
        eventstream = PayrollRunEventStream()

        payroll_run_id = eventstream.create_payroll_run(payroll_run_state=PayrollRunState.DRAFT)
        fake_employee_id = uuid4()
        eventstream.add_employees(payroll_run_id, [fake_employee_id])

        payroll_run = eventstream.get_payroll_run(payroll_run_id)
        self.assertEqual(payroll_run['state'], PayrollRunState.DRAFT)
        self.assertEqual(payroll_run['employees'], [fake_employee_id.__str__()])

        notifications = eventstream.notification_log.select(start=1, limit=10)
        self.assertEqual(len(notifications), 10)

        eventstream.take_snapshot(payroll_run_id, version=2)
        payroll_run = eventstream.get_payroll_run(payroll_run_id)
        self.assertEqual(payroll_run['state'], PayrollRunState.DRAFT)
        self.assertEqual(payroll_run['employees'], [fake_employee_id.__str__()])

        eventstream.approve_payroll_run(payroll_run_id)
        payroll_run = eventstream.get_payroll_run(payroll_run_id)
        self.assertEqual(payroll_run['state'], PayrollRunState.APPROVED)