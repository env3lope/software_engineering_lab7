# Процедурний
def greet(name):
    print(f"Hello, {name}!")

def main():
    name = "Anna"
    greet(name)

main()

# ООП
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

def main():
    greeter = Greeter("Anna")
    greeter.greet()

main()
