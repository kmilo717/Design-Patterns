import pickle


class Originator:
    def __init__(self):
        self.state = None

    def setMemento(self, memento):
        previousState = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previousState)

    def createMemento(self):
        return pickle.dumps(vars(self))


def main():
    originator = Originator()
    memento = originator.createMemento()
    originator.state = True
    originator.setMemento(memento)

if __name__ == "__main__":
    main()