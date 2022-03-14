"""Solution."""


class Factory:
    """Factory class."""

    def __init__(self):
        """Init."""
        self.cakes = list()

    def bake_cake(self, toppings: int, base: int) -> int:
        """Bake cakes."""
        count = 0

        while toppings >= 5 and base >= 5:
            self.cakes.append(Cake(5, 5))
            toppings -= 5
            base -= 5
            count += 1

        while toppings >= 2 and base >= 2:
            self.cakes.append(Cake(2, 2))
            toppings -= 2
            base -= 2
            count += 1

        while toppings > 0 and base > 0:
            self.cakes.append(Cake(1, 1))
            toppings -= 1
            base -= 1
            count += 1

        return count

    def get_last_cakes(self, n: int) -> list:
        """Get last cakes."""
        return self.cakes[:n]

    def get_cakes_baked(self) -> list:
        """Get amount of cakes."""
        return self.cakes

    def __str__(self):
        """Get factory with cakes amount."""
        amount = len(self.cakes)

        if amount == 1:
            return "Factory with 1 cake."

        return f"Factory with {amount} cakes."


class Cake:
    """Cake class."""

    def __init__(self, base_amount, toppings_amount):
        """Init."""
        if (base_amount != 1 and toppings_amount != 1) and (base_amount != 2 and toppings_amount != 2) and (base_amount != 5 and toppings_amount != 5):
            raise WrongIngredientsAmountException("Wrong base or toppings")

        self.base = base_amount
        self.toppings = toppings_amount

    @property
    def type(self):
        """Get cake type."""
        if self.base == 5 and self.toppings == 5:
            return "large"

        if self.base == 2 and self.toppings == 2:
            return "medium"

        if self.base == 1 and self.toppings == 1:
            return "basic"

    def __repr__(self):
        """Object representation."""
        return f"Cake({self.type})"

    def __eq__(self, other):
        """Compare two entries."""
        return self.type == other.type and self.base == other.base and self.toppings == other.toppings


class WrongIngredientsAmountException(Exception):
    """Custom Exception."""

    pass


if __name__ == '__main__':
    print(Cake(1, 3))
