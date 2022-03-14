"""Order system."""


class OrderItem:
    """Order Item requested by a customer."""

    def __init__(self, customer: str, name: str, quantity: int, one_item_volume: int):
        """
        Constructor that creates an order item.

        :param customer: requester name.
        :param name: the name of the item.
        :param quantity: quantity that shows how many such items customer needs.
        :param one_item_volume: the volume of one item.
        """
        self.customer = customer
        self.name = name
        self.quantity = quantity
        self.one_item_volume = one_item_volume

    @property
    def total_volume(self) -> int:
        """
        Calculate and return total volume the current order item.

        :return: Total volume (cm^3), int.
        """
        return self.quantity * self.one_item_volume


class Order:
    """Combination of order items of one customer."""

    def __init__(self, order_items: list):
        """
        Constructor that creates an order.

        :param order_items: list of order items.
        """
        self.order_items = order_items
        self.destination = None

    @property
    def total_quantity(self) -> int:
        """
        Calculate and return the sum of quantities of all items in the order.

        :return: Total quantity as int.
        """
        return sum(x.quantity for x in self.order_items)

    @property
    def total_volume(self) -> int:
        """
        Calculate and return the total volume of all items in the order.

        :return: Total volume (cm^3) as int.
        """
        return sum(x.total_volume for x in self.order_items)


class Container:
    """Container to transport orders."""

    def __init__(self, volume: int, orders: list):
        """Initialize Container."""
        self.volume = volume
        self.orders = orders

    @property
    def volume_left(self) -> int:
        """
        Calculate and return the volume left in the container.

        :return: volume left (cm^3) as int.
        """
        return self.volume - sum(x.total_volume for x in self.orders)


class OrderAggregator:
    """Algorithm of aggregating orders."""

    def __init__(self):
        """Initialize order aggregator."""
        self.order_items = list()

    def add_item(self, item: OrderItem):
        """
        Add order item to the aggregator.

        :param item: Item to add.
        :return: None
        """
        self.order_items.append(item)

    def aggregate_order(self, customer: str, max_items_quantity: int, max_volume: int):
        """
        Create an order for customer which contains order lines added by add_item method.

        Iterate over added orders items and add them to order if they are for given customer
        and can fit to the order.

        :param customer: Customer's name to create an order for.
        :param max_items_quantity: Maximum amount on items in order.
        :param max_volume: Maximum volume of order. All items volumes must not exceed this value.
        :return: Order.
        """
        items = list()
        volume = 0
        quantity = 0

        for item in list(self.order_items):
            if item.customer != customer or item.quantity > max_items_quantity:
                continue

            tmp_volume = volume + item.one_item_volume * item.quantity
            tmp_quantity = quantity + item.quantity

            if max_volume >= tmp_volume and max_items_quantity >= tmp_quantity:
                items.append(item)
                volume += tmp_volume
                quantity += tmp_quantity
                self.order_items.remove(item)

        return Order(items)


class ContainerAggregator:
    """Algorithm to prepare containers."""

    def __init__(self, container_volume: int):
        """
        Initialize Container Aggregator.

        :param container_volume: Volume of each container created by this aggregator.
        """
        self.container_volume = container_volume
        self.not_used_orders = list()

    def prepare_containers(self, orders: tuple) -> dict:
        """
        Create containers and put orders to them.

        If order cannot be put to a container, it is added to self.not_used_orders list.

        :param orders: tuple of orders.
        :return: dict where keys are destinations and values are containers to that destination with orders.
        """
        all_containers = dict()

        for order in orders:
            containers = all_containers.get(order.destination)

            if containers:
                did_fit = False

                for i, container in enumerate(containers):
                    if container.volume_left >= order.total_volume:
                        container.orders.append(order)
                        all_containers[order.destination][i] = container
                        did_fit = True
                        break

                if not did_fit and self.container_volume >= order.total_volume:
                    all_containers[order.destination].append(Container(self.container_volume, [order]))
                elif not did_fit:
                    self.not_used_orders.append(order)
            else:
                if self.container_volume >= order.total_volume:
                    all_containers[order.destination] = [Container(self.container_volume, [order])]
                else:
                    self.not_used_orders.append(order)

        return all_containers


if __name__ == '__main__':
    print("Order items")

    order_item1 = OrderItem("Apple", "iPhone 11", 100, 10)
    order_item2 = OrderItem("Samsung", "Samsung Galaxy Note 10", 80, 10)
    order_item3 = OrderItem("Mööbel 24", "Laud", 300, 200)
    order_item4 = OrderItem("Apple", "iPhone 11 Pro", 200, 10)
    order_item5 = OrderItem("Mööbel 24", "Diivan", 20, 200)
    order_item6 = OrderItem("Mööbel 24", "Midagi väga suurt", 20, 400)

    print(order_item3.total_volume)  # 60000

    print("\nOrder Aggregator")
    oa = OrderAggregator()
    oa.add_item(order_item1)
    oa.add_item(order_item2)
    oa.add_item(order_item3)
    oa.add_item(order_item4)
    oa.add_item(order_item5)
    oa.add_item(order_item6)
    print(f'Added {len(oa.order_items)} (6 is correct) order items')

    order1 = oa.aggregate_order("Apple", 350, 3000)
    order1.destination = "Tallinn"
    print(f'order1 has {len(order1.order_items)} (2 is correct) order items')

    order2 = oa.aggregate_order("Mööbel 24", 325, 64100)
    order2.destination = "Tallinn"
    print(f'order2 has {len(order2.order_items)} (2 is correct) order items')

    print(f'after orders creation, aggregator has only {len(oa.order_items)} (2 is correct) order items left.')

    print("\nContainer Aggregator")
    ca = ContainerAggregator(70000)
    too_big_order = Order([OrderItem("Apple", "Apple Car", 10000, 300)])
    too_big_order.destination = "Somewhere"
    containers = ca.prepare_containers((order1, order2, too_big_order))
    print(f'prepare_containers produced containers to {len(containers)} (1 is correct) different destination(s)')

    try:
        containers_to_tallinn = containers['Tallinn']
        print(f'volume of the container to tallinn is {containers_to_tallinn[0].volume} (70000 is correct) cm^3')
        print(f'container to tallinn has {len(containers_to_tallinn[0].orders)} (2 is correct) orders')
    except KeyError:
        print('Container to Tallinn not found!')
    print(f'{len(ca.not_used_orders)} (1 is correct) cannot be added to containers')
