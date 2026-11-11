# Start with items = ["milk", "bread", "eggs"] . Add “tea”, remove “bread”, sort the list,
# and print each item with its number using enumerate .
items = ["milk", "bread", "eggs"]
items.append("tea")
items.remove("bread")
items.sort()
for i, item in enumerate(items):
    print(f"{i}: {item}")