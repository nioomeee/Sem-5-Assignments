# Create a dictionary: inventory = {'pen': 50, 'notebook': 20, 'eraser': 5}.

# Use a lambda function with sorted() to print the inventory items sorted by quantity (descending).

# Create two sets: store_A_items and store_B_items. Find the Symmetric Difference (items in A or B, but not both).

# Convert the result to a frozenset and try to .add() a new item inside a try/except block to catch the error.

inventory = {"pen": 50, "notebook": 20, "eraser": 5}
print(f"\n Og inventory: {inventory}")

sorted_inventory = sorted(inventory.items(), key = lambda x: x[1], reverse = True)
print(f"\n Sorted inventory: {sorted_inventory}")

store_A_items = {"notebook", "eraser", "pen"}
store_B_items = {"pencil", "bag", "eraser"}

sym_diff = store_A_items.symmetric_difference(store_B_items)

print(f"\n Symmetric difference between store A items and store B items: \n {sym_diff}")

frozen_res = frozenset(sym_diff)

print(f"\n Frozen items: {frozen_res}")

try:
    print(f"\n Attempting to add pouch in frozen set...")
    frozen_res.add("pouch")

except AttributeError as e:
    print(f"\n Caught error as expected: {e}")
except ValueError as e:
    print(f"\n Unexpected error occured: {e}")

