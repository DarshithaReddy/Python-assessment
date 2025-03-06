class PublicDemo:
    def __init__(self):
        self.public_field = "This is a Public Field"

    def public_method(self):
        print("This is a Public Method")

class OtherClass:
    def access_public(self):
        obj = PublicDemo()
        print(obj.public_field)  # Accessible from anywhere
        obj.public_method()

if __name__ == "__main__":
    print("\nAccessing Public Members from Another Class:")
    other = OtherClass()
    other.access_public()
