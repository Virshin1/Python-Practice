# Complex Python Program #19

```python
import logging
from typing import List, Dict, Tuple

logger = logging.getLogger(__name__)

class BagelShop:
    """
    A class representing a bagel shop that sells various types and toppings of bagels.
    """

    def __init__(self, bagels: List[str], toppings: List[str]):
        """
        Initialize the bagel shop with a list of available bagels and toppings.

        Args:
            bagels (List[str]): A list of bagel types.
            toppings (List[str]): A list of topping options.
        """
        self.bagels = bagels
        self.toppings = toppings

    def create_order(self, bagel_type: str, toppings: List[str]) -> Dict[str, int]:
        """
        Create an order for a specified bagel type with a list of toppings.

        Args:
            bagel_type (str): The type of bagel to order.
            toppings (List[str]): A list of toppings to add to the bagel.

        Returns:
            Dict[str, int]: A dictionary representing the order, with the bagel type as the key and
            the number of toppings as the value.
        """
        if bagel_type not in self.bagels:
            raise ValueError(f"Invalid bagel type: {bagel_type}")

        for topping in toppings:
            if topping not in self.toppings:
                raise ValueError(f"Invalid topping: {topping}")

        order = {bagel_type: len(toppings)}
        return order

    def process_order(self, order: Dict[str, int]) -> Tuple[str, int]:
        """
        Process an order and return the total cost and a description of the order.

        Args:
            order (Dict[str, int]): The order to process.

        Returns:
            Tuple[str, int]: A tuple containing the description of the order and the total cost.
        """
        bagel_type = list(order.keys())[0]
        num_toppings = list(order.values())[0]
        total_cost = 1 + num_toppings * 0.5
        description = f"{bagel_type} bagel with {num_toppings} toppings"

        return description, total_cost

class Customer:
    """
    A class representing a customer placing an order at the bagel shop.
    """

    def __init__(self, name: str, order: Dict[str, int]):
        """
        Initialize the customer with a name and an order.

        Args:
            name (str): The name of the customer.
            order (Dict[str, int]): The order placed by the customer.
        """
        self.name = name
        self.order = order

class OrderProcessor:
    """
    A class responsible for processing orders placed by customers.
    """

    def __init__(self, bagel_shop: BagelShop):
        """
        Initialize the order processor with a reference to the bagel shop.

        Args:
            bagel_shop (BagelShop): The bagel shop where orders are placed.
        """
        self.bagel_shop = bagel_shop

    def process_orders(self, customers: List[Customer]) -> List[Tuple[str, int]]:
        """
        Process a list of orders placed by customers.

        Args:
            customers (List[Customer]): A list of customers with their orders.

        Returns:
            List[Tuple[str, int]]: A list of tuples containing the description of each order and its total cost.
        """
        processed_orders = []
        for customer in customers:
            try:
                description, total_cost = self.bagel_shop.process_order(customer.order)
                processed_orders.append((f"{customer.name}: {description}", total_cost))
            except ValueError as e:
                logger.error(f"Error processing order for customer {customer.name}: {e}")

        return processed_orders

if __name__ == "__main__":
    bagel_shop = BagelShop(["Plain", "Whole Wheat", "Everything"], ["Cream Cheese", "Butter", "Jelly"])
    order_processor = OrderProcessor(bagel_shop)

    customers = [
        Customer("John", bagel_shop.create_order("Plain", ["Cream Cheese"])),
        Customer("Mary", bagel_shop.create_order("Whole Wheat", ["Butter", "Jelly"])),
        Customer("Bob", bagel_shop.create_order("Everything", ["Cream Cheese", "Butter", "Jelly"]))
    ]

    processed_orders = order_processor.process_orders(customers)
    for order, total_cost in processed_orders:
        print(f"{order} - Total Cost: ${total_cost}")
```