import abc


class component(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def operation(self):
        pass


class decorator(component, metaclass = abc.ABCMeta):
    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class concreteFirstDecorator(decorator):
    @abc.abstractmethod
    def operation(self):
        self._component.operation()

class concreteSecondDecorator(decorator):
    @abc.abstractmethod
    def operation(self):
        self._component.operation()


class concreteComponent(component):
    def operation(self):
        pass


def main():
    concrete_component = concreteComponent()
    concrete_first_decorator = concreteFirstDecorator(concrete_component)
    concrete_second_decorator = concreteSecondDecorator(concrete_first_decorator)
    concrete_second_decorator.operation()

if __name__ == "__main__":
    main()
