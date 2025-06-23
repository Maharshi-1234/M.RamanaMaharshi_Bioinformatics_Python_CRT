#Write a python program to Simulate a Behaviour of a Web Page or Web Browsers, Back button when a user visits
#a new page push it to the stack, when the user clicks back pop the top page and go back to the previous page.
class Browser:
    def __init__(self):
        self.history = []
    def visit(self,page):
        self.history.append(page)
        print(f"Visited {page}")
    def Undo(self):
        if len(self.history)>1:
            self.history.pop()
            print(f"Back is {self.history[-1]}")
        else:
            print("No Pages to comeback")
browser = Browser()
browser.visit('google.com')
browser.visit('linkedIn.com')
browser.visit('github.com')
browser.Undo()