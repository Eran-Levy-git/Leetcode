class Singleton:
    _instance = None  # Private instance variable to store the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def some_method(self):
        print("Singleton method called")


# Create instances
singleton1 = Singleton()
singleton2 = Singleton()

# Both variables point to the same instance
print(singleton1 is singleton2)  # Output: True

# Call a method on the singleton instance
singleton1.some_method()  # Output: Singleton method called
