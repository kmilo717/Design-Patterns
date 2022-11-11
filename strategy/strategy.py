import abc


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def contextInterface(self):
        self._strategy.algorithmInterface()


class Strategy(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def algorithmInterface(self):
        pass


class ConcreteFirstStrategy(Strategy):
    def algorithmInterface(self):
        pass

class ConcreteSecondStrategy(Strategy):
    def algorithmInterface(self):
        pass


def main():
    concreteFirstStrategy = ConcreteFirstStrategy()
    context = Context(concreteFirstStrategy)
    context.contextInterface()

if __name__ == "__main__":
    main()