class Facade:
    def __init__(self):
        self._firstSubsystem = firstSubsystem()
        self._secondSubsystem = secondSubsystem()

    def operation(self):
        self._firstSubsystem.firstOperation()
        self._firstSubsystem.secondOperation()
        self._secondSubsystem.firstOperation()
        self._secondSubsystem.secondOperation()


class firstSubsystem:
    def firstOperation(self):
        pass

    def secondOperation(self):
        pass

class secondSubsystem:
    def firstOperation(self):
        pass

    def secondOperation(self):
        pass


def main():
    facade = Facade()
    facade.operation()

if __name__ == "__main__":
    main()