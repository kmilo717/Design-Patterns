import abc


class abstractFactory(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def createFirstProduct(self):
        pass

    @abc.abstractmethod
    def createSecondProduct(self):
        pass

class concreteFactory1(abstractFactory):
    def createFirstProduct(self):
        return concreteFirstProduct1()

    def createSecondProduct(self):
        return concreteSecondProduct1()

class concreteFactory2(abstractFactory):
    def createFirstProduct(self):
        return concreteFirstProduct2()

    def createSecondProduct(self):
        return concreteSecondProduct2()


class abstractFirstProduct(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def interfaceA(self):
        pass

class concreteFirstProduct1(abstractFirstProduct):
    def interfaceA(self):
        pass

class concreteFirstProduct2(abstractFirstProduct):
    def interfaceA(self):
        pass


class abstractSecondProduct(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def interfaceB(self):
        pass

class concreteSecondProduct1(abstractSecondProduct):
    def interfaceB(self):
        pass

class concreteSecondProduct2(abstractSecondProduct):
    def interfaceB(self):
        pass


def main():
    for factory in (concreteFactory1(), concreteFactory2()):
        firstProduct = factory.createFirstProduct()
        secondProduct = factory.createSecondProduct()
        firstProduct.interfaceA()
        secondProduct.interfaceB()

if __name__ == "__main__":
    main()