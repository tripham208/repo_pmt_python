class ClassicClass:
    attr1: str
    attr2: int

    def __init__(self, attr1: str, attr2: int):
        self.attr1 = attr1
        self.attr2 = attr2

    @property
    def attr3(self) -> int:
        return self.attr3

    @attr3.setter
    def attr3(self, attr3: int):
        self.attr3 = attr3
