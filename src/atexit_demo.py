"""Demonstrate how to use atexit."""
import atexit


class Meals:
    """A meal class."""

    def __init__(self, name):
        """Instantiate a meal.

        Args:
            name: the name of a person
        """
        self.name = name
        atexit.register(self.full)

    def full(self):
        """Declare full status."""
        print(f"{self.name}: I am stuffed.")

    def breakfast(self):
        """Break the fast."""
        print(f"{self.name} had breakfast.")

    def lunch(self):
        """Luncheon."""
        print(f"{self.name} had lunch.")


if __name__ == "__main__":
    a_meal = Meals("Ted")
    a_meal.breakfast()
    a_meal.lunch()
