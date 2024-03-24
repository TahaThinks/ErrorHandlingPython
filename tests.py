# FileNotFound Handling
try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["non_existent_key"])
except FileNotFoundError:
    file = open("a_file.txt", 'w')
    file.write("Hello Taha!")
except KeyError as error_message:
    print(f"The Key {error_message} doesn't Exist")



# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_exisitent_key"]
#
# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]
#
# # TypeError
# text = "abc"
# print(text + 5)
