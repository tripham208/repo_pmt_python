class A:
    class_name = "A"

    def a(self):
        print(f"{self.class_name}.a")


def b(self):
    print(f"{self.class_name}.b")

def c(self, param = "addition param"):
    print(f"{self.class_name}.{param}")


setattr(A, "b", b)  # extension method
setattr(A, "c", c)  # extension method

if __name__ == '__main__':
    a = A()
    a.a()
    a.b()
    c(a,"addition param")
