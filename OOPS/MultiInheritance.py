class GrandFather():
    def __init__(self):
        pass
    @staticmethod
    def Properties():
        print("100 Acres of Land")
class Father(GrandFather):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Properties():
        print("50 Acres of Land")
class Yourself(Father):
    def __init__(self):
        super().__init__()
    def Properties():
        print("A Btech Degree")
GrandFather.Properties()
Father.Properties()
Yourself.Properties()