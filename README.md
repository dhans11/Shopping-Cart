# 🚩 Project Name: Shopping Cart

🙋🏻‍♂️ Project Owner: Ahmad Dani Rifai  
🏁 Date Finished: May 2024  
📞 Contact: [LinkedIn](https://www.linkedin.com/in/ahmad-dhani-0b8b6a22b/); [E-mail](adhani866@gmail.com)

## Overview

This project implements a simple shopping cart system using Python. The system allows users to add items to their cart, remove items, view items in the cart, and see the total price of the items in the cart. The user interacts with the system through a text-based menu.

## Classes

### `CartItem`

Represents an individual item in the shopping cart.

**Attributes:**

- `nama` (str): The name of the item.
- `harga` (float): The price of the item.

**Methods:**

- `__init__(self, nama, harga)`: Initializes an item with a name and price.
- `__str__(self)`: Returns a string representation of the item in the format 'name: Rp.price'.

### `ShoppingCart`

Represents the shopping cart.

**Attributes:**

- `cart` (list): A list of items in the shopping cart.

**Methods:**

- `__init__(self)`: Initializes the shopping cart with an empty list.
- `display_menu(self)`: Displays the main menu to the user.
- `add_item(self)`: Adds a new item to the shopping cart.
- `remove_item(self)`: Removes an item from the shopping cart based on the item's name.
- `show_item_in_cart(self)`: Displays all items in the shopping cart.
- `total_price_item(self)`: Calculates and displays the total price of all items in the shopping cart.
- `exit_program(self)`: Displays a thank you message and exits the program.
- `process_choice(self, choice)`: Processes the user's menu choice.

## Main Function

### `main()`

The main function runs the shopping cart program. It creates an instance of `ShoppingCart` and enters a loop, displaying the menu and processing the user's choice until the user decides to exit the program.

## Usage

1. **Run the Program**: Execute the script. The main function will be called, starting the shopping cart program.
2. **Menu Options**:
   - `1. Menambah Barang`: Add a new item to the cart.
   - `2. Hapus Barang`: Remove an item from the cart.
   - `3. Tampilkan Barang di Keranjang`: Show all items currently in the cart.
   - `4. Lihat Total Belanja`: Display the total price of items in the cart.
   - `5. Exit`: Exit the program.

## Example

```python
if __name__ == "__main__":
    main()
```

When you run the script, follow the prompts to interact with the shopping cart system.

## Additional Information

- The program will continue to prompt the user for actions until the user chooses to exit by selecting option `5`.
- If an invalid menu choice is entered, the program will prompt the user to enter a valid choice.

## Notes

- Ensure Python 3.x is installed to run the script.
- The script is intended to be run in a terminal or command prompt.
