class singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance() is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class myClass(metaclass = singleton):
    pass


def main():
    firstMain = myClass()
    secondMain = myClass()
    assert firstMain is secondMain

if __name__ == "___main__":
    main()