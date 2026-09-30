#Add key-value pair in a nested dictionary
given_dict={
    "user1": {"name": "Alice", "age": 25},
    "user2": {"name": "Bob", "age": 30}
    }
print(f"The given dictionary: {given_dict}")
given_dict["user3"]={"name": "Charlie", "age": 35}
updated_dict=given_dict
print(f"The updated dictionary: {updated_dict}")
