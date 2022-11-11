import abc


class subject(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def request(self):
        pass


class Proxy(subject):
    def __init__(self, realSubject):
        self._realSubject = realSubject

    def request(self):
        self._realSubject.request()


class RealSubject(subject):
    def request(self):
        pass


def main():
    realSubject = RealSubject()
    proxy = Proxy(realSubject)
    proxy.request()

if __name__ == "__main__":
    main()