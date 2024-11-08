from dataclasses import dataclass


class Old:
   def __init__(self, name:str, weight:float):
       self.name = name
       self.weight = weight

@dataclass
class New:
   name: str
   weight: float


def test_dataclass():
    old = Old('A', 1.5)
    new = New('A', 2.0)
    print(old.name, old.weight, new.name, new.weight)