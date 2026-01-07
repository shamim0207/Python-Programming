info={
    "name":"Shamim",
    "ID" : "0112230207",
    "Age": 25,
    "Department":"CSE",
    "University":"UIU"

    
    }
print("Original Dictionary:",info)
# Accessing value using key
print("Name:",info["name"])
# Adding a new key-value pair
info["Semester"]="Spring 2024"
print("Dictionary after adding Semester:",info)

# Updating an existing value
info["Age"]=26

print("Dictionary after updating Age:",info)

# Removing a key-value pair using del
del info["ID"]


print("Dictionary after deleting ID:",info)# Using pop() method to remove a key-value pair
removed_value=info.pop("Department")    