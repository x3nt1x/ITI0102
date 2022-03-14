"""Fruits delivery application."""


class Customer:
    """Customer class."""

    def __init__(self, name: str, address: str):
        """Customer constructor."""
        self.__name = name
        self.__address = address
        self.__orders = list()

    def __repr__(self):
        """Representation of the customer."""
        return f"{self.__name} @{self.__address} with {len(self.__orders)} orders."

    def get_name(self):
        """Customer name."""
        return self.__name

    def get_address(self):
        """Customer address."""
        return self.__address

    def get_orders(self):
        """Customer orders."""
        return self.__orders

    def add_new_order(self, order):
        """Add new order to orders."""
        self.__orders.append(order)


class Product:
    """Product class."""

    def __init__(self, name: str, price: float):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.name = name
        self.price = price

    def __repr__(self):
        """Representation of the product."""
        return f"{self.name}: {self.price}"

    def get_name(self):
        """Product name."""
        return self.name

    def get_price(self):
        """Product price."""
        return self.price


class Order:
    """Order class."""

    def __init__(self, customer: Customer = None):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.__customer = customer
        self.__products_to_order = dict()

    def get_customer(self):
        """Getter for customer."""
        return self.__customer

    def get_products(self) -> dict:
        """Getter for products to order list."""
        return self.__products_to_order

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        return ", ".join([f"{product}: {quantity} kg" for product, quantity in self.get_products().items()])

    def add_product(self, products: tuple):
        """Method for adding a single product to the dictionary."""
        product = products[0]
        quantity = products[1]

        if product in self.get_products():
            self.__products_to_order[product] += quantity
        else:
            self.__products_to_order[product] = quantity

    def add_products(self, products: list):
        """Method for adding several products to the dictionary."""
        for product in products:
            self.add_product(product)


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.__products = self.import_products("pricelist.txt")
        self.__customers: list[Customer] = list()
        self.__orders: list[Order] = list()

    def get_products(self) -> list:
        """Getter for products."""
        return self.__products

    def get_customers(self):
        """Getter for customers."""
        return self.__customers

    def get_orders(self) -> list:
        """Getter for orders."""
        return self.__orders

    def import_products(self, filename: str) -> list:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        products = list()

        with open(filename) as file:
            for product in file.readlines():
                name_price = product.split(" - ")
                products.append(Product(name_price[0], float(name_price[1])))

        return products

    def find_product_by_name(self, name: str):
        """Find product by name."""
        for product in self.get_products():
            if product.get_name() == name:
                return product

        return None

    def order_products(self, products):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        """
        order = Order()

        if isinstance(products, list):
            order.add_products(products)
        else:
            order.add_product(products)

        self.__orders.append(order)

    def order(self, name: str, products: list):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        for product in products:
            product_name = product[0]

            if not self.find_product_by_name(product_name):
                raise Exception(f"Woopsie. There is no such product as {product_name}")

        for customer in self.get_customers():
            if customer.get_name() == name:
                order = Order(customer)
                order.add_products(products)
                customer.add_new_order(order)

    def add_customer(self, customer: Customer):
        """Method for adding a customer to the list."""
        self.__customers.append(customer)

    def add_customers(self, customers: list):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.add_customer(customer)

    def show_all_orders(self, is_summary: bool) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        output = str()

        for i, customer in enumerate(self.get_customers()):
            output += f"{customer.get_name()}:\n"
            total = self.calculate_total(customer)

            output += "\n".join([f"{order.get_products_string()}" for order in customer.get_orders()]) if total else "nothing"

            if is_summary:
                output += "\nTotal: {:.2f}".format(round(total, 2))

            if i != len(self.get_customers()) - 1:
                output += "\n\n"

        return output

    def calculate_total(self, customer: Customer) -> float:
        """Method for calculating total price for all customer's orders."""
        total = float()

        for order in customer.get_orders():
            for name, quantity in order.get_products().items():
                product = self.find_product_by_name(name)

                if product:
                    total += product.get_price() * quantity

        return total

    def calculate_summary(self) -> str:
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        return f"{self.show_all_orders(True)}\nALL ORDERS TOTAL: {sum(self.calculate_total(customer) for customer in self.get_customers())}"


if __name__ == '__main__':
    app = App()

    # Adding default customers to our app.
    app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
                       Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])

    # Ordering some food for everyone.
    app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Rubber Duck", [("Mango Irwin", 6)])
    app.order("Svetozar", [("Lemon", 1)])
    app.order("Svetozar", [("Grapefruit", 10)])
    app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])

    # Checking products dictionary format (we want numeric price, not string).
    print(app.get_products())
    print("=======")

    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    print(app.calculate_summary())
