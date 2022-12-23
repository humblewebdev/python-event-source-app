class PayrollrunController:

    def __init__(self, command_bus: CommandBus):
        self.command_bus = command_bus

    @classmethod
    def get_all(self):
        pass

    @classmethod
    def create(self):
        command = CreatePayrollRunCommand()
        payroll_run_id = cls.command_bus.handle(command)
        return payroll_run_id
