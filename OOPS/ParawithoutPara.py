class Mobile:
    def __init__(self):
        print("Mobile Constructor Called!")
realme = Mobile()

#Direct initialisation
class Mobile:
    def __init__(self):
        self.model = "Samsung S21,Vivo T1 5g,Sony Xperia"
    def show_model(self):
        print("Models:",self.model)
realme = Mobile()
realme.show_model()