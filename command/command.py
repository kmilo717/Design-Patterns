import abc


class Invoker:
    def __init__(self):
        self.commands = []

    def storeCommand(self, command):
        self.commands.append(command)

    def executeCommands(self):
        for command in self.commands:
            command.execute()


class Command(metaclass = abc.ABCMeta):
    def __init__(self, receiver):
        self._receiver = receiver

    @abc.abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def execute(self):
        self._receiver.action()


class Receiver:
    def action(self):
        pass


def main():
    receiver = Receiver()
    concreteCommand = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.storeCommand(concreteCommand)
    invoker.executeCommands()

if __name__ == "__main__":
    main()