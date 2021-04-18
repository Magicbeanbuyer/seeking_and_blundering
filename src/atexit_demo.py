import atexit


class Meals:
    def __init__(self, name):
        self.name = name
        atexit.register(self.full)

    def full(self):
        print(f"{self.name}: I am stuffed.")

    def breakfast(self):
        print(f"{self.name} had breakfast.")

    def lunch(self):
        print(f"{self.name} had lunch.")


if __name__ == "__main__":
    a_meal = Meals("Ted")
    a_meal.breakfast()
    a_meal.lunch()
