class Foo:
    def __init__(self, data):
        self.data = data


class Bar:
    def __init__(self, foo):
        self.foo = foo


f = Foo(123)
b = Bar(f)
