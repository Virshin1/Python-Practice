# Complex Python Program #18

```python
import logging
from typing import List, Dict, Any

class InventoryItem:
    def __init__(self, name: str, quantity: int, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self) -> str:
        return f"Item: {self.name}, Quantity: {self.quantity}, Price: {self.price}"


class Inventory:
    def __init__(self) -> None:
        self._items: List[InventoryItem] = []
        self._logger = logging.getLogger(__name__)

    def add_item(self, item: InventoryItem) -> None:
        try:
            if item.quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if item.price < 0:
                raise ValueError("Price cannot be negative")
            self._items.append(item)
        except ValueError as e:
            self._logger.error("Error adding item: %s", e)

    def get_total_value(self) -> float:
        try:
            return sum(item.quantity * item.price for item in self._items)
        except Exception:
            self._logger.error("Error calculating total value", exc_info=True)
            return 0.0

    def get_items_by_name(self, name: str) -> List[InventoryItem]:
        try:
            return [item for item in self._items if item.name == name]
        except Exception:
            self._logger.error("Error getting items by name", exc_info=True)
            return []


class ShoppingCart:
    def __init__(self) -> None:
        self._items: Dict[str, int] = {}

    def add_item(self, item_name: str, quantity: int) -> None:
        try:
            if quantity < 0:
                raise ValueError("Quantity cannot be negative")
            if item_name not in self._items:
                self._items[item_name] = 0
            self._items[item_name] += quantity
        except ValueError:
            logging.getLogger(__name__).error("Error adding item to shopping cart", exc_info=True)

    def get_total_price(self, inventory: Inventory) -> float:
        try:
            total_price = 0.0
            for item_name, quantity in self._items.items():
                items = inventory.get_items_by_name(item_name)
                if not items:
                    raise ValueError(f"Item {item_name} not found in inventory")
                item = items[0]
                total_price += item.price * quantity
            return total_price
        except ValueError as e:
            logging.getLogger(__name__).error("Error getting total price", exc_info=True)
            return 0.0


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    inventory = Inventory()
    inventory.add_item(InventoryItem("Apple", 10, 1.5))
    inventory.add_item(InventoryItem("Banana", 20, 2.0))
    inventory.add_item(InventoryItem("Orange", 15, 2.5))
    print(f"Total value of inventory: {inventory.get_total_value()}")

    shopping_cart = ShoppingCart()
    shopping_cart.add_item("Apple", 3)
    shopping_cart.add_item("Banana", 2)
    shopping_cart.add_item("Orange", 1)
    total_price = shopping_cart.get_total_price(inventory)
    print(f"Total price of shopping cart: {total_price}")


if __name__ == "__main__":
    main()
```