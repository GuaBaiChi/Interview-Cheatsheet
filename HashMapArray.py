# Create an empty hashmap
hashmap = {}

# Add key-value pairs to the hashmap
hashmap["apple"] = 4
hashmap["banana"] = 6
hashmap["orange"] = 2

# Retrieve values from the hashmap
apple_quantity = hashmap["apple"]
banana_quantity = hashmap.get("banana")
orange_quantity = hashmap.get("orange", 0)
# Provide a default value if the key doesn't exist

# Update a value in the hashmap
hashmap["banana"] = 8

# Remove a key-value pair from the hashmap
del hashmap["orange"]

# Print the hashmap and the retrieved values
print("Hashmap:", hashmap)
print("Apple quantity:", apple_quantity)
print("Banana quantity:", banana_quantity)
print("Orange quantity:", orange_quantity)
