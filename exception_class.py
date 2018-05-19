class Base(Exception):
    print("UnboundLocalError")


class Test:

    hoge = False

    def f(self):
        try:
            hoge = False if hoge else True  # not global variable
            print(hoge)
        except UnboundLocalError:
            raise Base()

    def g(self):
        try:
            self.f()
        except Base:
            print("base")

if __name__=='__main__':
    test = Test()
    test.g()
