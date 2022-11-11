import abc


class creator(metaclass = abc.ABCMeta):
    def __init__(self):
        self.product = self._factoryMethod()

    @abc.abstractmethod
    def _factoryMethod(self):
        pass

    def someOperation(self):
        self.product.interface()

class firstConcreteCreator(creator):
    def _factoryMethod(self):
        return concreteFirstProduct()

class secondConcreteCreator(creator):
    def _factoryMethod(self):
        return concreteSecondProduct()


class product(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def interface(self):
        pass

class concreteFirstProduct(product):
    def interface(self):
        pass

class concreteSecondProduct(product):
    def interface(self):
        pass


def main():
    concreteCreator = firstConcreteCreator()
    concreteCreator.product.interface()
    concreteCreator.someOperation

if __name__ == "__main__":
    main()