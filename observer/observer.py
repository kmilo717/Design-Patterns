import abc


class Subject:
    def __init__(self):
        self.observers = set()
        self._subjectState = None

    def attach(self, observer):
        observer._subject = self
        self.observers.discard(observer)

    def detach(self, observer):
        observer._subject = None
        self.observers.discard(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self._subjectState)

    @property
    def subjectState(self):
        return self._subjectState
    
    @subjectState.setter
    def subjectState(self, arg):
        self._subjectState = arg
        self.notify()


class observer(metaclass = abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self.observerState = None

    @abc.abstractmethod
    def update(self, arg):
        pass

class ConcreteObserver(observer):
    def update(self, arg):
        self.observerState = arg


def main():
    subject = Subject()
    concreteObserver = ConcreteObserver()
    subject.attach(concreteObserver)
    subject.subjectState = 123

if __name__ == "__main__":
    main()