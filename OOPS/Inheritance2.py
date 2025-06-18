class Father:
    def __init__(self):
        pass
    @staticmethod
    def Work():
        print("Working Father")
class Son(Father):
    def __init__(self):
        super().__init__()
    @staticmethod
    def Work():
        print("Enjoying Son")
Father.Work()
Son.Work()