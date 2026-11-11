# Start with items = ["milk", "bread", "eggs"] . Add “tea”, remove “bread”, sort the list,
# and print each item with its number using enumerate .
#list of items
items = ["milk", "bread", "eggs"]
#use append() to add "tea" to the list
items.append("tea")
#use remove() to remove "bread" from the list
items.remove("bread")
#use sort() to sort the list
items.sort()
#use enumerate() to print each item with its number
for i, item in enumerate(items):
    #print the item with its number
    print(f"{i}: {item}")